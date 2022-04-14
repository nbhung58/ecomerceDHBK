from library.extension import db
from library.library_ma import BorrowSchema
from library.model import Books, Borrow, Category, Author, Students
from flask import jsonify, request
from sqlalchemy.sql import func
import json
from datetime import datetime

#Mượn 1 quyển sách
borrow_schema  = BorrowSchema()
#Mượn nhiều quyển sách
borrows_schema = BorrowSchema(many = True)

# #Hàm mượn 1 quyển sách
# def borrow_book_service():
#     data = request.json

def add_borrow_service():
    data = request.json
    #print(data)
    if ((data and 'book_id' in data) and ('student_id' in data) 
    and ('borrow_date' in data) and ('return_date' in data)):
        book_id = data['book_id']
        student_id = data['student_id']
        borrow_date_str = data['borrow_date']
        borrow_date = datetime.strptime(borrow_date_str,'%d/%m/%y')
        return_date_str = data['return_date']
        return_date = datetime.strptime(return_date_str,'%d/%m/%y')
        try:
            new_borrow = Borrow(book_id, student_id, borrow_date, return_date)
            db.session.add(new_borrow)
            db.session.commit()
            return "Add success"
        except IndentationError:
            db.session.rollback()
            return "Can not add borrow"
    else:
        return "Request Error"



def get_borrow_author_cat_gervice(student_name):
    borrows = db.session.query(Borrow.id, Books.name, Category.name, Author.name).join(
        Students, Borrow.student_id == Students.id).join(Category.id == Books.category_id).join(
            Author, Author.id == Books.author_id
        ).filter(func.lower(Students.name) == student_name.lower()).all()
    if borrows:
        return jsonify({f"{student_name} borrowed": borrows})
    else:
        return jsonify({"message": "Not found borrow!"}), 404


