from payload.ResponsePayload import ResponsePayload

from controller.AuthController import AuthController
from controller.AuthController import UserController
from controller.PersonController import PersonGetController,PersonAddController,PersonEditController,PersonDeleteController,PersonListController




class Config:


    @staticmethod
    def mongo_config(app, db):
        app.config["MONGODB_PORT"] = 27017
        app.config["MONGODB_DB"] = 'admin'
        app.config["MONGODB_USERNAME"] = 'devroot'
        app.config["MONGODB_PASSWORD"] = 'devroot'
        app.config['MONGODB_HOST'] = "mongodb://devroot:devroot@mongodb/admin?retryWrites=true&w=majority"
        db.init_app(app)
    @staticmethod
    def exception_config(app):
        pass
    @staticmethod
    def route_config(api):
        api.add_resource(AuthController, "/Auth/getToken")
        api.add_resource(UserController, "/Auth/addUser")
        api.add_resource(PersonGetController, "/Person/Get")
        api.add_resource(PersonAddController, "/Person/Add")
        api.add_resource(PersonEditController, "/Person/Edit")
        api.add_resource(PersonDeleteController, "/Person/Delete/<string:tckn>")
        api.add_resource(PersonListController, "/Person/List")

    @staticmethod
    def jwt_config(jwt, app):
        app.config['JWT_ALGORITHM'] = 'HS256'
        app.config['JWT_SECRET_KEY'] = '123456'
        app.config['JWT_PRIVATE_KEY'] = '123456'
        app.config['JWT_PUBLIC_KEY'] = '12222'

        @jwt.expired_token_loader
        def my_expired_token_callback():
            return ResponsePayload.error(
                status=401,
                message="The token has expired"
            )

        @jwt.invalid_token_loader
        def my_invalid_token_loader(e):
            return ResponsePayload.error(
                status=401,
                message="The token is invalid:"
            )

        @jwt.unauthorized_loader
        def my_unauthorized_loader(fp):
            return ResponsePayload.error(
                status=401,
                message="The token is unauthorized"
            )

        @jwt.needs_fresh_token_loader
        def my_needs_fresh_token_loader():
            return ResponsePayload.error(
                status=401,
                message="Needs fresh token"
            )



