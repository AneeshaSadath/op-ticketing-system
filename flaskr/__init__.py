from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flaskr.register import register_api
from flaskr.get_patient import get_patient_api

config = None

db = MongoEngine()
app = Flask(__name__, instance_relative_config=True)
CORS(app)
app.config.from_mapping(SECRET_KEY="dev")
if config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_object("config.DevelopmentConfig")
else:
    # load the config if passed in
    app.config.from_object(config)
db.init_app(app)

app.register_blueprint(register_api)
app.register_blueprint(get_patient_api)
