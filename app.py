from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import routes
import database

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    database.configure(app)
    routes.configure(app)
    return app


