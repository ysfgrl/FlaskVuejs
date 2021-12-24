import datetime
from flask_jwt_extended import create_access_token, get_jwt_identity
from entities.UserRepository import UserRepository
from services.BaseService import BaseService
from payload.ResponsePayload import ResponsePayload


class AuthService(BaseService):

    def __init__(self):
        super().__init__()
        self._user_repository = UserRepository()

    def login(self, payload: object):

        if 'password' not in payload or 'username' not in payload:
            return ResponsePayload.error(404, message="UserName or Password empty")

        user = self._user_repository.find_user_by_username(payload['username'])

        if user is not None:
            if user["password"] == payload["password"] :
                return self.create_token(user)
            return None
        return None

    def add_user(self, payload):
        return self._user_repository.add_user(payload)

    def create_token(self, user):
        days = 1
        expires_delta = datetime.timedelta(days=days)
        access_token = create_access_token(identity=user["username"],
                                           expires_delta=expires_delta)
        token = {
            "access_token": access_token,
            "user": user
        }
        return ResponsePayload.success("Token Created", token, 200)
