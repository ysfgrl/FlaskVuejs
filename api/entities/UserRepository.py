from entities.User import User
import traceback
import logging

import json

class UserRepository:

    def find_user_by_username(self, username: str):
        try:
            user = User.objects.get(username=username)
            return json.loads(user.to_json())
        except Exception as e:
            logging.error(traceback.format_exc())
            return None

    def add_user(self, payload):
        try:
            person = User(
                name=payload["name"],
                surname=payload["surname"],
                username=payload["username"],
                password=payload["password"]
            )
            person.save()
            return True
        except Exception as e:
            logging.error(traceback.format_exc())
            return None
