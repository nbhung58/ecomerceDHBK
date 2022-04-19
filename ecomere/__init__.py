from flask import Flask, request, Blueprint
from .data.Customers.controller import customer

def create_app():
    app = Flask(__name__)
    app.register_blueprint(customer)
    return app


