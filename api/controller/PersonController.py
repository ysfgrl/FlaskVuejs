from flask_jwt_extended import jwt_required
from controller.BaseController import BaseController
from payload.ResponsePayload import ResponsePayload
from services.PersonService import PersonService


class PersonAddController(BaseController):
    def __init__(self):
        super().__init__()
        self.person_service = PersonService()

    @jwt_required()
    def post(self):
        payload = self.get_payload_json()
        data = self.person_service.add_person(payload)
        return ResponsePayload.success("test",data)


class PersonEditController(BaseController):
    def __init__(self):
        super().__init__()
        self.person_service = PersonService()

    @jwt_required()
    def put(self):
        payload = self.get_payload_json()
        data = self.person_service.edit_person(payload)
        return ResponsePayload.success("test", data)


class PersonGetController(BaseController):
    def __init__(self):
        super().__init__()
        self.person_service = PersonService()

    @jwt_required()
    def get(self, tckn):
        data = self.person_service.find_tckn(tckn)
        return ResponsePayload.success("test",data)


class PersonDeleteController(BaseController):
    def __init__(self):
        super().__init__()
        self.person_service = PersonService()

    @jwt_required()
    def delete(self, tckn):
        data = self.person_service.delete_person(tckn)
        return ResponsePayload.success("test", data)


class PersonListController(BaseController):
    def __init__(self):
        super().__init__()
        self.person_service = PersonService()

    @jwt_required()
    def post(self):
        payload = self.get_payload_json()
        data = self.person_service.get_person_list(payload)
        return ResponsePayload.success("test",data)
