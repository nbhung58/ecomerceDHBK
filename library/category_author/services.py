from unicodedata import category
from library.extension import db
from library.library_ma import AuthorSchema, CategorySchema
from library.model import Category, Author
from flask import request, jsonify

category_schema = CategorySchema()
categorys_schema = CategorySchema(many = True)

author_chema = AuthorSchema()
authors_chema = AuthorSchema(many = True)

def add_category_service():
    data = request.json
    if data and 'name' in data:
        name = data['name']
        try:
            new_category = Category(name)
            db.session.add(new_category)
            db.session.commit()
            return "Add success"
        except IndentationError:
            db.session.rollback()
            return "Can not ad category"
    else: 
        return "Request error"




def add_author_service():
    data = request.json
    if data and 'name' in data:
        name = data['name']
        try:
            new_author = Author(name)
            db.session.add(new_author)
            db.session.commit()
            return "Add success"
        except IndentationError:
            db.session.rollback()
            return "Can not ad category"
    else: 
        return "Request error"


#Delete Author
def delete_author_by_id_service(id):
    author = Author.query.get(id)
    if author:
        try:
            db.session.delete(author)
            db.session.commit()
            return "Author deleted"
        except IndentationError():
            db.session.rollback()
            return "Can not delete author"
        finally:
            db.session.close()
    else:
        return "Not found author"
