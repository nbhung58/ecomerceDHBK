from library.extension import db
from library.library_ma import StudentSchema
from library.model import Students
from flask import request, jsonify
from datetime import datetime
import json

student_schema = StudentSchema()
students_schema = StudentSchema(many = True)

def add_student_service():
    data = request.json
    print(data)
    if ((data and 'name' in data) and ('birth_date' in data) 
    and ('gender' in data) and ('class_name' in data)):
        name = data['name']
        birth_date_str = data['birth_date']
        birth_date = datetime.strptime(birth_date_str,'%d/%m/%y')
        gender = data['gender']
        class_name = data['class_name']
        try:
            new_student = Students(name, birth_date, gender, class_name)
            db.session.add(new_student)
            db.session.commit()
            return "Add success"
        except IndentationError:
            db.session.rollback()
            return "Can not add student"
    else:
        return "Request Error"

def get_student_by_id_service(id):
    student = Students.query.get(id)
    print(student)
    if student:
        return student_schema.jsonify(student)
    else:
        return "Not found student"

def get_all_students_service():
    students = Students.query.all()
    print(students)
    if students:
        return students_schema.jsonify(students)
    else:
        return "Not found student"

#Update thông tin student
def update_student_by_id_service(id):
    student = Students.query.get(id)
    data = request.json
    if student:
        if data and "class_name" in data:
            try:
                student.class_name = data["class_name"]
                db.session.commit()
                return "Student updated"
            except IndentationError:
                db.session.rollback()
                return "Can not update student"
            finally:
                db.session.close()
    else:
        return "Not found student!"

#Delete student
def delete_student_by_id_service(id):
    student = Students.query.get(id)
    if student:
        try:
            db.session.delete(student)
            db.session.commit()
            return "Student deteted"
        except IndentationError:
            db.session.rollback()
            return "Can not delete student"
        finally:
            db.session.close()
    else:
        return "Not found student"
