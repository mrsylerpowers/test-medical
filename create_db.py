import os

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()



def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db.init_app(app)



    with app.app_context():
        # Create tables for our models
        db.create_all(Config.SQLALCHEMY_BINDS.keys())

        return app
