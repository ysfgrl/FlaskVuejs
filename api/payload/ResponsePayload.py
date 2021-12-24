from flask import json, Response ,abort, make_response, jsonify
from werkzeug.exceptions import BadRequest
import datetime

from bson import ObjectId


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):

        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        elif isinstance(obj, ObjectId):
            return str(obj)

        return json.JSONEncoder.default(self, obj)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class ResponsePayload:

    def __init__(
            self,
            data: object,
            status: int,
            message: str = None,
    ):
        self.data = data
        self.status = status
        self.message = message

    @staticmethod
    def result_ok(response_payload) -> Response:
        try:
            if response_payload is None:
                raise Exception("argument can not be null")

            result = {
                "data": response_payload.data,
                "status": response_payload.status,
                "message": response_payload.message,
            }

            return Response(
                json.dumps(result, cls=CustomJsonEncoder),
                status=response_payload.status,
                mimetype='application/json'
            )

        except Exception as ex:
            raise ex
    @staticmethod
    def result_ok2(response_payload) -> Response:
        try:
            if response_payload is None:
                raise Exception("argument can not be null")

            result = {
                "data": response_payload.data,
                "status": response_payload.status,
                "message": response_payload.message,
            }

            return Response(
                json.dumps(result, cls=CustomJsonEncoder),
                status=response_payload.status,
                mimetype='application/json'
            )
        except Exception as ex:
            raise ex
    @staticmethod
    def abort(status: int = 404, message: str = None):
        response = make_response(jsonify(message=message,status=status), status)
        abort(response)
        # raise InvalidUsage('This view is gone', status_code=status)

    @staticmethod
    def error(status: int = 404, message: str = None) -> Response:
        return ResponsePayload.result_ok(ResponsePayload(data=None, status=status, message=message))
    @staticmethod
    def success(message: str = None, data: object = None, code: int = 200) -> Response:
        return ResponsePayload.result_ok(ResponsePayload(data=data, status=code, message=message))

