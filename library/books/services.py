from library.extension import db
from library.library_ma import BooksSchema
from library.model import Books, Author
from flask import request, jsonify
from sqlalchemy.sql import func
import json

#Lấy ra 1 quyển sách thì dùng book_schema
book_schema = BooksSchema()
#Lấy ra nhiều quyển sách thì dùng books_schema
books_schema = BooksSchema(many = True)

#hàm add quyển sách 
def add_book_service():
    data = request.json
    #Nhận request từ postman thêm hàm request
    if ((data and 'name' in data) and ('page_count' in data) 
    and ('author_id'in data) and ('category_id'in data)):
        name = data['name']
        page_count = data['page_count']
        author_id = data['author_id']
        category_id = data['category_id']
        try:
            new_book = Books(name, page_count, author_id, category_id)
            #print(new_book)
            db.session.add(new_book)
            # Ghi nhận sự thay đổi
            db.session.commit()
            return "Add success"
        except IndentationError:
            db.session.rollback()
            print(IndentationError)
            return "Can not add book"
    else:
        return "Request error"

# #Hàm add nhiều quyển sách
# def add_books_service():
#     data = request.json


#Lấy ra 1 quyển sahcs
def get_book_by_id_service(id):
    book = Books.query.get(id)
    print(book)
    if book:
        #bookSchema sẽ mapping các trường của thằng book và các field của schema
        return book_schema.jsonify(book)
    else:
        return "Not found book"


#Lấy ra nhiều quyển sach
def get_all_book_service():
    books = Books.query.all()
    if books:
        #bookSchema sẽ mapping các trường của thằng book và các field của schema
        return books_schema.jsonify(books)
    else:
        return "Not found book"

#Update 1 quyển sách, update số trang
def update_book_by_id_service(id):
    book = Books.query.get(id)
    data = request.json
    if book:
        if data and "page_count" in data:
        #bookSchema sẽ mapping các trường của thằng book và các field của schema
            try:
                book.page_count = data["page_count"]
                db.session.commit()
                return "Book updated"
            except IndentationError:
                db.session.rollback()
                #print(IndentationError)
                return "Can not update book!"
            finally:
                db.session.close()
    else:
        return "Not found book"

#update 1 quyển sách, udpate category_id
def update_category_id_service(id):
    book = Books.query.get(id)
    data = request.json
    if book:
        if data and "category_id" in data:
            try:
                book.category_id = data["category_id"]
                db.session.commit()
                return "Book updated"
            except IndentationError:
                db.session.rollback()
                return "Can not update book!"
            finally:
                db.session.close()
    else:
        return "Not found book"

#update 1 quyển sách, update author
def update_author_id_service(id):
    book = Books.query.get(id)
    data = request.json
    if book:
        if data and "author_id" in data:
            try:
                book.category_id = data["author_id"]
                print(book.category_id)
                db.session.commit()
                return "Book updated"
            except IndentationError:
                db.session.rollback()
                return "Can not update book!"
            finally:
                db.session.close()
    else:
        return "Not found book"

#Delete 1 quyển sách
def delete_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            return "Book deleted"
        except IndentationError:
            db.session.rollback()
            #print(IndentationError)
            return "Can not delete book!"
        finally:
            db.session.close()
    else:
        return "Not found book"

#Get book by author
def get_book_by_author_service(author):
    books = Books.query.join(Author).filter(func.lower(Author.name) == author.lower()).all() #Làm cho cac chu cai chuyen het thanh chư viet thuong
    print(books)
    if books:
        return books_schema.jsonify(books)
    else:
        return jsonify({"message": f"Not found books by {author}"}), 404
