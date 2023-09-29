import dashscope
from dashscope.api_entities.api_request_data import ApiRequestData
from dashscope.api_entities.http_request import HttpRequest
from dashscope.api_entities.websocket_request import WebSocketRequest
from dashscope.common.constants import (REQUEST_TIMEOUT_KEYWORD,
                                        SERVICE_API_PATH, ApiProtocol,
                                        HTTPMethod, StreamResultMode)
from dashscope.common.error import InputDataRequired, UnsupportedApiProtocol
from dashscope.protocol.websocket import WebsocketStreamingMode


def _get_protocol_params(kwargs):
    api_protocol = kwargs.pop('api_protocol', ApiProtocol.HTTPS)
    ws_stream_mode = kwargs.pop('ws_stream_mode', WebsocketStreamingMode.OUT)
    is_binary_input = kwargs.pop('is_binary_input', False)
    http_method = kwargs.pop('http_method', HTTPMethod.POST)
    stream = kwargs.pop('stream', False)
    async_request = kwargs.pop('async_request', False)
    query = kwargs.pop('query', False)
    headers = kwargs.pop('headers', None)
    request_timeout = kwargs.pop(REQUEST_TIMEOUT_KEYWORD, None)
    stream_result_mode = kwargs.pop('stream_result_mode',
                                    StreamResultMode.ACCUMULATE)
    form = kwargs.pop('form', None)
    resources = kwargs.pop('resources', None)
    return (api_protocol, ws_stream_mode, is_binary_input, http_method, stream,
            async_request, query, headers, request_timeout, stream_result_mode,
            form, resources)


def _build_api_request(model: str, input: object, task_group: str, task: str,
                       function: str, api_key: str, **kwargs):
    (api_protocol, ws_stream_mode, is_binary_input, http_method, stream,
     async_request, query, headers, request_timeout, stream_result_mode,
     form, resources) = _get_protocol_params(kwargs)
    task_id = kwargs.pop('task_id', None)
    if api_protocol in [ApiProtocol.HTTP, ApiProtocol.HTTPS]:
        if not dashscope.base_http_api_url.endswith('/'):
            http_url = dashscope.base_http_api_url + '/' + SERVICE_API_PATH
        else:
            http_url = dashscope.base_http_api_url + SERVICE_API_PATH
        http_url += '/'

        if task_group:
            http_url += '%s/' % task_group
        if task:
            http_url += '%s/' % task
        if function:
            http_url += function
        request = HttpRequest(url=http_url,
                              api_key=api_key,
                              http_method=http_method,
                              stream=stream,
                              async_request=async_request,
                              query=query,
                              stream_result_mode=stream_result_mode,
                              timeout=request_timeout,
                              task_id=task_id)
    elif api_protocol == ApiProtocol.WEBSOCKET:
        websocket_url = dashscope.base_websocket_api_url
        request = WebSocketRequest(url=websocket_url,
                                   api_key=api_key,
                                   stream=stream,
                                   ws_stream_mode=ws_stream_mode,
                                   is_binary_input=is_binary_input,
                                   stream_result_mode=stream_result_mode,
                                   timeout=request_timeout)
    else:
        raise UnsupportedApiProtocol(
            'Unsupported protocol: %s, support [http, https, websocket]' %
            api_protocol)

    if headers is not None:
        request.add_headers(headers=headers)

    if input is None and form is None:
        raise InputDataRequired('There is no input data and form data')

    request_data = ApiRequestData(model,
                                  task_group=task_group,
                                  task=task,
                                  function=function,
                                  input=input,
                                  form=form,
                                  is_binary_input=is_binary_input,
                                  api_protocol=api_protocol)
    request_data.add_resources(resources)
    request_data.add_parameters(**kwargs)
    request.data = request_data
    return request
