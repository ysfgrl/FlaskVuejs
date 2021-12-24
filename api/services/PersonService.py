from entities.PersonRepository import PersonRepository
from services.BaseService import BaseService


class PersonService(BaseService):
    def __init__(self):
        super().__init__()
        self._person_repository = PersonRepository()

    def find_tckn(self, tckn):
        return self._person_repository.find_person_by_tckn(tckn)

    def add_person(self, payload):
        return self._person_repository.add_person(payload)

    def edit_person(self, payload):
        return self._person_repository.edit_person(payload)

    def delete_person(self, tckn):
        return self._person_repository.delete_person(tckn)

    def get_person_list(self,payload):
        return self._person_repository.get_all_person(payload["page"],payload["limit"])
