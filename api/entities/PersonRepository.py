from entities.Person import Person
import json
import traceback
import logging

class PersonRepository:

    def find_person_by_tckn(self, tckn: str):

        try:
            person = Person.objects.get(tckn=tckn)
            return json.loads(person.to_json())
        except Exception as e:
            return None


    def get_all_person(self, page: int = 1, limit: int = 50):
        try:
            persons = Person.objects()
            return json.loads(persons.to_json())
        except Exception as e:
            return None


    def add_person(self, payload):
        try:
            person = Person(
                name=payload["name"],
                surname=payload["surname"],
                tckn=payload["tckn"],
                username=payload["username"],
                password=payload["password"]
            )
            person.save()
            return True
        except Exception as e:
            return None


    def edit_person(self, payload):
        try:
            person = Person.objects.get(tckn=payload["tckn"])
            person.name = payload["name"]
            person.surname = payload["surname"]
            person.save()
            return True
        except Exception as e:
            return None

    def delete_person(self, tckn):
        try:
            person = Person.objects.get(tckn=tckn)
            person.delete()
            return True
        except Exception as e:
            return None


