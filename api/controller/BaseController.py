# from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource
from flask import request
# from src.commons.request import get_auth_token
from payload.ResponsePayload import ResponsePayload
from werkzeug.exceptions import default_exceptions, NotFound

class BaseController(Resource):

    def __init__(self):
        pass

    @classmethod
    def auth_token(cls, key: str = None):
        return ""
        # return get_auth_token(key=key)

    @property
    def account_id(self):
        return "";
        # return get_auth_token("_id")

    # auth = HTTPBasicAuth()

    def get_payload_json(self):
        if not request.is_json:
            return ResponsePayload.abort(400, "Only Allowed Application/Json")
        content = request.json
        return content

    '''
    @auth.error_handler
    def unauthorized(self):
        """
        return unauthorized_result(
            code="handler.auth.unauthorized",
            message="The token is unauthorized",
            description=""
        )
        """
        pass
    '''
