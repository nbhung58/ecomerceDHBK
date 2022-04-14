from unicodedata import category
from flask import Blueprint
from .services import(add_category_service, add_author_service, delete_author_by_id_service,
delete_author_by_id_service)

category = Blueprint("category", __name__)
author = Blueprint("author", __name__)

#Add a new category
@category.route("/category-management/category", methods = ['POST'])
def add_category():
    return add_category_service()



#Add an author
@author.route("/author-management/author", methods = ['POST'])
def add_author():
    return add_author_service()

#Delete author
@author.route("/author-management/author/<int:id>", methods = ['DELETE'])
def delete_author(id):
    return delete_author_by_id_service(id)


