from http import HTTPStatus
from pathlib import Path

DASHSCOPE_API_KEY_ENV = 'DASHSCOPE_API_KEY'
DASHSCOPE_API_KEY_FILE_PATH_ENV = 'DASHSCOPE_API_KEY_FILE_PATH'
DASHSCOPE_API_REGION_ENV = 'DASHSCOPE_API_REGION'
DASHSCOPE_API_VERSION_ENV = 'DASHSCOPE_API_VERSION'
# to disable data inspection
# export DASHSCOPE_DISABLE_DATA_INSPECTION=true
DASHSCOPE_DISABLE_DATA_INSPECTION_ENV = 'DASHSCOPE_DISABLE_DATA_INSPECTION'
DEFAULT_DASHSCOPE_CACHE_PATH = Path.home().joinpath('.dashscope')
DEFAULT_DASHSCOPE_API_KEY_FILE_PATH = Path.joinpath(
    DEFAULT_DASHSCOPE_CACHE_PATH, 'api_key')

DEFAULT_REQUEST_TIMEOUT_SECONDS = 300
REQUEST_TIMEOUT_KEYWORD = 'request_timeout'
SERVICE_API_PATH = 'services'
DASHSCOPE_LOGGING_LEVEL_ENV = 'DASHSCOPE_LOGGING_LEVEL'
# task config keys.
PROMPT = 'prompt'
MESSAGES = 'messages'
NEGATIVE_PROMPT = 'negative_prompt'
HISTORY = 'history'
CUSTOMIZED_MODEL_ID = 'customized_model_id'
IMAGES = 'images'
TEXT_EMBEDDING_INPUT_KEY = 'texts'
SERVICE_503_MESSAGE = 'Service temporarily unavailable, possibly overloaded or not ready.'  # noqa E501
WEBSOCKET_ERROR_CODE = 44
SSE_CONTENT_TYPE = 'text/event-stream'
DEPRECATED_MESSAGE = 'history and auto_history are deprecated for qwen serial models and will be remove in future, use messages'  # noqa E501
SCENE = "scene"
MESSAGE = 'message'


REPEATABLE_STATUS = [
    HTTPStatus.SERVICE_UNAVAILABLE, HTTPStatus.GATEWAY_TIMEOUT
]


class FilePurpose:
    fine_tune = 'fine_tune'


class StreamResultMode:
    """Stream result mode.
        examples(I like apple)
            accumulate: will output
                I
                I like
                I like apple
            divide: will output
                I
                like
                apple
    """
    ACCUMULATE = 'accumulate'
    DIVIDE = 'divide'


class DeploymentStatus:
    DEPLOYING = 'DEPLOYING'
    SERVING = 'RUNNING'
    DELETING = 'DELETING'
    FAILED = 'FAILED'
    PENDING = 'PENDING'


class ApiProtocol:
    WEBSOCKET = 'websocket'
    HTTP = 'http'
    HTTPS = 'https'


class HTTPMethod:
    GET = 'GET'
    HEAD = 'HEAD'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    CONNECT = 'CONNECT'
    OPTIONS = 'OPTIONS'
    TRACE = 'TRACE'
    PATCH = 'PATCH'


class TaskStatus:
    PENDING = 'PENDING'
    SUSPENDED = 'SUSPENDED'
    SUCCEEDED = 'SUCCEEDED'
    CANCELED = 'CANCELED'
    RUNNING = 'RUNNING'
    FAILED = 'FAILED'
    UNKNOWN = 'UNKNOWN'


class Tasks(object):
    TextGeneration = 'text-generation'
    AutoSpeechRecognition = 'asr'
