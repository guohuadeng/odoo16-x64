import json
from http import HTTPStatus

import requests

from dashscope.api_entities.base_request import BaseRequest
from dashscope.api_entities.dashscope_response import DashScopeAPIResponse
from dashscope.common.constants import (DEFAULT_REQUEST_TIMEOUT_SECONDS,
                                        SSE_CONTENT_TYPE, HTTPMethod,
                                        StreamResultMode)
from dashscope.common.error import UnsupportedHTTPMethod
from dashscope.common.logging import logger


class HttpRequest(BaseRequest):
    def __init__(self,
                 url: str,
                 api_key: str,
                 http_method: str,
                 stream: bool = True,
                 async_request: bool = False,
                 query: bool = False,
                 stream_result_mode: str = StreamResultMode.ACCUMULATE,
                 timeout: int = DEFAULT_REQUEST_TIMEOUT_SECONDS,
                 task_id: str = None) -> None:
        """HttpSSERequest, processing http server sent event stream.

        Args:
            url (str): The request url.
            api_key (str): The api key.
            method (str): The http method(GET|POST).
            stream (bool, optional): Is stream request. Defaults to True.
            timeout (int, optional): Total request timeout.
                Defaults to DEFAULT_REQUEST_TIMEOUT_SECONDS.
        """

        super().__init__()
        self.url = url
        self.async_request = async_request
        self.headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer %s' % api_key,
            **self.headers,
        }
        self.query = query
        if self.async_request and self.query is False:
            self.headers = {
                'X-DashScope-Async': 'enable',
                **self.headers,
            }
        self.method = http_method
        if self.method == HTTPMethod.POST:
            self.headers['Content-Type'] = 'application/json'

        self.stream = stream
        if self.stream:
            self.headers['Accept'] = SSE_CONTENT_TYPE
            self.headers['X-Accel-Buffering'] = 'no'
            self.headers['X-DashScope-SSE'] = 'enable'
        if self.query:
            self.url = self.url.replace('api', 'api-task')
            self.url += '%s' % task_id
        if timeout is None:
            self.timeout = DEFAULT_REQUEST_TIMEOUT_SECONDS
        else:
            self.timeout = timeout

    def add_header(self, key, value):
        self.headers[key] = value

    def add_headers(self, headers):
        self.headers = {**self.headers, **headers}

    def call(self):
        response = self._handle_request()
        if self.stream:
            return (item for item in response)
        else:
            output = next(response)
            try:
                next(response)
            except StopIteration:
                pass
            return output

    def _handle_stream(self, response: requests.Response):
        # TODO define done message.
        is_error = False
        status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        for line in response.iter_lines():
            if line:
                line = line.decode('utf8')
                line = line.rstrip('\n').rstrip('\r')
                if line.startswith('event:error'):
                    is_error = True
                elif line.startswith('status:'):
                    status_code = line[len('status:'):]
                    status_code = int(status_code.strip())
                elif line.startswith('data:'):
                    line = line[len('data:'):]
                    yield (is_error, status_code, line)
                    if is_error:
                        break
                else:
                    continue  # ignore heartbeat...

    def _handle_response(self, response: requests.Response):
        request_id = ''
        if (response.status_code == HTTPStatus.OK and self.stream
                and SSE_CONTENT_TYPE in response.headers.get(
                    'content-type', '')):
            for is_error, status_code, data in self._handle_stream(response):
                try:
                    output = None
                    usage = None
                    msg = json.loads(data)
                    logger.debug('Stream message: %s' % msg)
                    if not is_error:
                        if 'output' in msg:
                            output = msg['output']
                        if 'usage' in msg:
                            usage = msg['usage']
                    if 'request_id' in msg:
                        request_id = msg['request_id']
                except json.JSONDecodeError:
                    yield DashScopeAPIResponse(
                        request_id=request_id,
                        status_code=HTTPStatus.BAD_REQUEST,
                        output=None,
                        code='Unknown',
                        message=data)
                    continue
                if is_error:
                    yield DashScopeAPIResponse(
                        request_id=request_id,
                        status_code=status_code,
                        output=None,
                        code=msg['code']
                        if 'code' in msg else None,  # noqa E501
                        message=msg['message']
                        if 'message' in msg else None)  # noqa E501
                else:
                    yield DashScopeAPIResponse(request_id=request_id,
                                               status_code=HTTPStatus.OK,
                                               output=output,
                                               usage=usage)
        elif response.status_code == HTTPStatus.OK:
            json_content = response.json()
            logger.debug('Response: %s' % json_content)
            output = None
            usage = None
            if 'task_id' in json_content:
                output = {'task_id': json_content['task_id']}
            if 'output' in json_content:
                output = json_content['output']
            if 'usage' in json_content:
                usage = json_content['usage']
            if 'request_id' in json_content:
                request_id = json_content['request_id']
            yield DashScopeAPIResponse(request_id=request_id,
                                       status_code=HTTPStatus.OK,
                                       output=output,
                                       usage=usage)
        else:
            if 'application/json' in response.headers.get('content-type', ''):
                error = response.json()
                if 'request_id' in error:
                    request_id = error['request_id']
                if 'message' not in error:
                    message = ''
                    logger.error('Request: %s failed, status: %s' %
                                 (self.url, response.status_code))
                else:
                    message = error['message']
                    logger.error(
                        'Request: %s failed, status: %s, message: %s' %
                        (self.url, response.status_code, error['message']))
                yield DashScopeAPIResponse(
                    request_id=request_id,
                    status_code=response.status_code,
                    output=None,
                    code=error['code']
                    if 'code' in error else None,  # noqa E501
                    message=message)
            else:
                msg = response.content
                yield DashScopeAPIResponse(request_id=request_id,
                                           status_code=response.status_code,
                                           output=None,
                                           code='Unknown',
                                           message=msg.decode('utf-8'))

    def _handle_request(self):
        try:
            with requests.Session() as session:
                if self.method == HTTPMethod.POST:
                    is_form, form, obj = self.data.get_http_payload()
                    if is_form:
                        headers = {**self.headers}
                        headers.pop('Content-Type')
                        response = session.post(url=self.url,
                                                data=obj,
                                                files=form,
                                                headers=headers,
                                                timeout=self.timeout)
                    else:
                        logger.debug('Request body: %s' % obj)
                        response = session.post(url=self.url,
                                                stream=self.stream,
                                                json=obj,
                                                headers={**self.headers},
                                                timeout=self.timeout)
                elif self.method == HTTPMethod.GET:
                    response = session.get(url=self.url,
                                           params=self.data.parameters,
                                           headers=self.headers,
                                           timeout=self.timeout)
                else:
                    raise UnsupportedHTTPMethod('Unsupported http method: %s' %
                                                self.method)
                for rsp in self._handle_response(response):
                    yield rsp
        except Exception as e:
            logger.error(e)
            raise e
