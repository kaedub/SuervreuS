class BaseController:
    def __init__(self, user, request_object=None):
        # TODO: set the user object to self.user
        # self.user = user
        self.request_object = request_object
        self.init()

    def init(self):
        """Override this to perform init items without having to override __init__."""
        pass

    def response(self, data=None, meta=None, error=None):
        raise NotImplementedError("response() must be implemented on all base controller classes")


class ApiController(BaseController):
    def response(self, data=None, meta=None, errors=None):
        response = {}

        if data:
            response['data'] = data
        if meta:
            response['meta'] = meta
        if errors:
            response['errors'] = errors

        return response
