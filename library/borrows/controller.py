from flask import Blueprint
from .services import (get_borrow_author_cat_gervice, add_borrow_service)

borrow = Blueprint("borrow", __name__)

@borrow.route("/borrow-management/borrow", methods = ['POST'])
def add_borrow():
    return add_borrow_service()

@borrow.route("/borrow-management/borrow/<string:student>", methods = ['GET'])
def get_borrow_author_cat(student):
    return get_borrow_author_cat_gervice(student)