from flask import Flask, request, Blueprint
from .books.controller import books
from .students.controller import students
from .category_author.controller import category, author
from .borrows.controller import borrow
from .extension import db, ma
from .model import Students, Books, Author, Category, Borrow
import os


def create_db(app):
    #Nếu ko tồn tại 1 đường dẫn database, tạo 1 file database
    if not os.path.exists("library.db"):
        db.create_all(app = app)
        print("Created DB")

def create_app(config_file="config.py"):
    app = Flask(__name__)
    db.init_app(app)
    ma.init_app(app)
    app.config.from_pyfile(config_file)
    create_db(app)
    app.register_blueprint(books)
    app.register_blueprint(students)
    app.register_blueprint(category)
    app.register_blueprint(author)
    app.register_blueprint(borrow)
    #print(app.config["SECRET_KEY"])
    return app
