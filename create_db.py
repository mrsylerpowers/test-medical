from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import SQLALCHEMY_BINDS

app = Flask(__name__)
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
db = SQLAlchemy(app)

def create_app():
    return app