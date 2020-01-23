
from flask import (
    # abort,
    jsonify,
    request,
    make_response,
)

from flask.views import View

class BaseEndpoint(View):
    def __init__(self, cls_controller):
        self.user = None
        self.request = None
        self.controller = None
        self.cls_controller = cls_controller

    @property
    def request_payload(self):
        """Get the payload of the request. The payload is a dict of the complete request.

        The order that the dict is built is important! Items added later override items
        added earlier.
            1. defaults
            2. args (querystring)
            3. form
            4. json
        """
        payload = {}

        # update with json data
        json_payload = self.request.get_json(silent=True)
        if json_payload:
            payload.update(json_payload)

        # update with request args/form data
        request_data = self.request.form.to_dict()
        payload.update(request_data)
        request_data = self.request.args.to_dict()
        payload.update(request_data)

        # !! THIS MUST BE ADDED LAST to insure it's not overridden
        # update with url segments and defaults
        if self.request.view_args:
            # don't add any keys that start with underscore
            request_data_defaults = {k: v for k, v in self.request.view_args.items() if not k.startswith('_')}
            payload.update(request_data_defaults)

        return payload

    def dispatch_request(self, *args, **kwargs):
        """Main entry point for a view called by Flask."""
        self.request = request

        # TODO: set the user object to self.user
        # try:
        #     self.user = self.current_user()
        # except Exception as error:
        #     return self.process_error(error)

        return self.handle_request(*args, **kwargs)

    def handle_request(self, *args, **kwargs):
        """Return the rendered response."""

        # TODO: authorize the endpoint

        self.init_controller()
        
        try:
            response_data = self.process()
        except Exception as error:
            return self.process_error(error)

        # render response
        if isinstance(response_data, dict):
            try:
                response = self.render(response_data)
            except Exception as error:
                return self.process_error(error)
        else:
            response = response_data

        return response

    def init_controller(self):
        """Initialize controller."""
        self.controller = self.cls_controller(self.user, request_object=self.request)

    def process(self):
        """Process the request."""
        controller_method = getattr(self.controller, request.method.lower(), None)

        # raise NotImplementedError if controller does not support the HTTP method used
        if controller_method is None:
            raise NotImplementedError()

        result = controller_method(self.request_payload)
        return result

    def process_error(self, error):
        # TODO: Implement handling of top high level errors and set http status codes
        # error_type = type(error)
        # if error_type is UserPermissionError:
        #     abort(404)
        # elif error_type is NotFoundError:
        #     abort(404)
        # elif error_type is ValidationError:
        #     return str(error), 400
        # elif error_type is GatewayError:
        #     return str(error), 502
        # else:
        raise error

    def render(self, **data):
        """Return rendered response."""
        raise NotImplementedError("render() must be implemented on all endpoint classes")


class JsonEndpoint(BaseEndpoint):
    """Endpoint for JSON api."""

    def render(self, data):
        """Return response rendered as JSON."""
        return make_response(jsonify(data), data.get('status_code', 200))