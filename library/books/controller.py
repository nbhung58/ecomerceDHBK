from flask import Blueprint
from .services import (add_book_service, get_book_by_id_service, 
get_all_book_service, update_book_by_id_service, delete_book_by_id_service,
get_book_by_author_service, update_category_id_service, update_author_id_service)

books = Blueprint("books", __name__)


#add a new book 
@books.route("/book-management/book", methods = ['POST'])
def add_book():
    return add_book_service()

#Get book by id

@books.route("/book-management/book/<int:id>", methods = ['GET'])
def get_book(id):
    return get_book_by_id_service(id)
#Get all book
@books.route("/book-management/books", methods = ['GET'])
def get_all_book():
    return get_all_book_service()

#Update book page count
@books.route("/book-management/book/page-count/<int:id>", methods = ['PUT'])
def update_book_pagecount_by_id(id):
    return update_book_by_id_service(id)

#Update book category-id
@books.route("/book-management/book/categoryid/<int:id>", methods = ['PUT'])
def update_book_category_by_id(id):
    return update_category_id_service(id)

#Update book author-id
@books.route("/book-management/book/author-id/<int:id>", methods = ['PUT'])
def update_book_author_id_by_id(id):
    return update_author_id_service(id)


#Delete all book
@books.route("/book-management/book/<int:id>", methods = ['DELETE'])
def delete_book_by_id(id):
    return delete_book_by_id_service(id)


@books.route("/book-management/book/<string:author>", methods = ['GET'])
def get_book_by_author(author):
    return get_book_by_author_service(author)



