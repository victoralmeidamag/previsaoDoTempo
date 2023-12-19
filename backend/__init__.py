from flask import Flask
from flask_migrate import Migrate



def create_app():
    app = Flask(__name__)
    Migrate(app)
