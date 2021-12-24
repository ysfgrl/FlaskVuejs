
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)
from config import Config

print("..")
CORS(app)
jwt = JWTManager(app)
api = Api(app)

app.app_context().push()

# Config.exception_config(app)
db = MongoEngine()
Config.mongo_config(app,db)
Config.jwt_config(jwt,app)
Config.route_config(api)



def main():
    try:
        app.run(
            host="0.0.0.0",
            port=9005,
            debug=True
        )
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
