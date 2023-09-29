import asyncio
import json
import os
import platform
from http import HTTPStatus
from typing import Dict
from urllib.parse import urlparse

import aiohttp
import requests

from dashscope.api_entities.dashscope_response import DashScopeAPIResponse
from dashscope.common.api_key import get_default_api_key
from dashscope.version import __version__


def is_validate_fine_tune_file(file_path):
    with open(file_path) as f:
        for line in f:
            try:
                json.loads(line)
            except json.decoder.JSONDecodeError:
                return False
    return True


def _get_task_group_and_task(module_name):
    """Get task_group and task name.
    get task_group and task name based on api file __name__

    Args:
        module_name (str): The api file __name__

    Returns:
        (str, str): task_group and task
    """
    pkg, task = module_name.rsplit('.', 1)
    task = task.replace('_', '-')
    _, task_group = pkg.rsplit('.', 1)
    return task_group, task


def is_path(path: str):
    """Check the input path is valid local path.

    Args:
        path_or_url (str): The path.

    Returns:
        bool: If path return True, otherwise False.
    """
    url_parsed = urlparse(path)
    if url_parsed.scheme in ('file', ''):
        return os.path.exists(url_parsed.path)
    else:
        return False


def is_url(url: str):
    """Check the input url is valid url.

    Args:
        url (str): The url

    Returns:
        bool: If is url return True, otherwise False.
    """
    url_parsed = urlparse(url)
    if url_parsed.scheme in ('http', 'https', 'oss'):
        return True
    else:
        return False


def iter_over_async(ait, loop):
    ait = ait.__aiter__()

    async def get_next():
        try:
            obj = await ait.__anext__()
            return False, obj
        except StopAsyncIteration:
            return True, None

    while True:
        done, obj = loop.run_until_complete(get_next())
        if done:
            loop.close()
            break
        yield obj


def async_to_sync(async_generator):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    asyncio.set_event_loop(loop)
    for message in iter_over_async(async_generator, loop):
        yield message


def default_headers(api_key: str = None) -> Dict[str, str]:
    ua = 'dashscope/%s; python/%s; platform/%s; processor/%s' % (
        __version__,
        platform.python_version(),
        platform.platform(),
        platform.processor(),
    )
    headers = {'user-agent': ua}
    if api_key is None:
        api_key = get_default_api_key()
    headers['Authorization'] = 'Bearer %s' % api_key
    headers['Accept'] = 'application/json'
    return headers


def join_url(base_url, *args):
    if not base_url.endswith('/'):
        base_url = base_url + '/'
    url = base_url
    for arg in args:
        url += arg + '/'
    return url[:-1]


async def _handle_aiohttp_response(response: aiohttp.ClientResponse):
    request_id = ''
    if response.status == HTTPStatus.OK:
        json_content = await response.json()
        if 'request_id' in json_content:
            request_id = json_content['request_id']
        return DashScopeAPIResponse(request_id=request_id,
                                    status_code=HTTPStatus.OK,
                                    output=json_content)
    else:
        if 'application/json' in response.content_type:
            error = await response.json()
            msg = ''
            if 'message' in error:
                msg = error['message']
            if 'request_id' in error:
                request_id = error['request_id']
            return DashScopeAPIResponse(request_id=request_id,
                                        status_code=response.status,
                                        output=None,
                                        code=error['code'],
                                        message=msg)
        else:
            msg = await response.read()
            return DashScopeAPIResponse(request_id=request_id,
                                        status_code=response.status,
                                        output=None,
                                        code='Unknown',
                                        message=msg)


def _handle_http_failed_response(
        response: requests.Response) -> DashScopeAPIResponse:
    msg = ''
    code = None
    request_id = ''
    if 'application/json' in response.headers.get('content-type', ''):
        error = response.json()
        if 'message' in error:
            msg = error['message']
        if 'msg' in error:
            msg = error['msg']
        if 'code' in error:
            code = error['code']
        if 'request_id' in error:
            request_id = error['request_id']
        return DashScopeAPIResponse(request_id=request_id,
                                    status_code=response.status_code,
                                    code=code,
                                    message=msg)
    else:
        msg = response.content.decode('utf-8')
        return DashScopeAPIResponse(request_id=request_id,
                                    status_code=response.status_code,
                                    code='Unknown',
                                    message=msg)


def _handle_http_response(response: requests.Response):
    request_id = ''
    if response.status_code == HTTPStatus.OK:
        output = None
        usage = None
        code = None
        msg = ''
        json_content = response.json()
        if 'data' in json_content:
            output = json_content['data']
        if 'code' in json_content:
            code = json_content['code']
        if 'message' in json_content:
            msg = json_content['message']
        if 'output' in json_content:
            output = json_content['output']
        if 'usage' in json_content:
            usage = json_content['usage']
        if 'request_id' in json_content:
            request_id = json_content['request_id']
        return DashScopeAPIResponse(request_id=request_id,
                                    status_code=response.status_code,
                                    code=code,
                                    output=output,
                                    usage=usage,
                                    message=msg)
    else:
        return _handle_http_failed_response(response)
