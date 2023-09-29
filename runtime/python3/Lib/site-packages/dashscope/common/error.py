class AuthenticationError(Exception):
    pass


class InvalidParameter(Exception):
    pass


class InvalidTask(Exception):
    pass


class UnsupportedModel(Exception):
    pass


class UnsupportedTask(Exception):
    pass


class ModelRequired(Exception):
    pass


class InvalidModel(Exception):
    pass


class InvalidInput(Exception):
    pass


class InvalidFileFormat(Exception):
    pass


class UnsupportedApiProtocol(Exception):
    pass


class NotImplemented(Exception):
    pass


class MultiInputsWithBinaryNotSupported(Exception):
    pass


class UnexpectedMessageReceived(Exception):
    pass


class UnsupportedData(Exception):
    pass


# for server send generation or inference error.
class RequestFailure(Exception):
    def __init__(self,
                 request_id=None,
                 message=None,
                 name=None,
                 http_code=None):
        self.request_id = request_id
        self.message = message
        self.name = name
        self.http_code = http_code

    def __str__(self):
        msg = 'Request failed, request_id: %s, http_code: %s error_name: %s, error_message: %s' % (  # noqa E501
            self.request_id, self.http_code, self.name, self.message)
        return msg


class UnknownMessageReceived(Exception):
    pass


class InputDataRequired(Exception):
    pass


class InputRequired(Exception):
    pass


class UnsupportedDataType(Exception):
    pass


class ServiceUnavailableError(Exception):
    pass


class UnsupportedHTTPMethod(Exception):
    pass


class AsyncTaskCreateFailed(Exception):
    pass
