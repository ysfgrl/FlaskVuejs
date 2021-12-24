
from payload.ResponsePayload import ResponsePayload
from controller.BaseController import BaseController
from services.AuthService import AuthService


class AuthController(BaseController):
    def __init__(self):
        super().__init__()
        self._auth_service = AuthService()

    def post(self):
        payload = self.get_payload_json()
        if payload is not None:
            return self._auth_service.login(payload)
        else:
            ResponsePayload.abort(404, "Not Found User")

class UserController(BaseController):

    # @inject
    # def __init__(self, auth_service: AuthService):
    #     super().__init__()
    #     self._auth_service = auth_service

    def __init__(self):
        super().__init__()
        self._auth_service = AuthService()

    def post(self):
        payload = self.get_payload_json()
        return self._auth_service.add_user(payload)
