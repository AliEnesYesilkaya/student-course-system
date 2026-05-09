from flask import Flask
from app.controllers.main_controller import main


def create_app():

    app = Flask(__name__)

    app.register_blueprint(main)

    return app