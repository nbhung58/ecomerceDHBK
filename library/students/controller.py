from flask import Blueprint

from library.model import Students
from .services import (add_student_service, get_student_by_id_service,
get_all_students_service, update_student_by_id_service, delete_student_by_id_service)

students = Blueprint("students", __name__)

#add a new student
@students.route("/student-management/student", methods = ['POST'])
def add_student():
    return add_student_service()

#Get student by id
@students.route("/student-management/student/<int:id>", methods=['GET'])
def get_student_by_id(id):
    return get_student_by_id_service(id)

#Get all students
@students.route("/student-management/students", methods=['GET'])
def get_all_student():
    return get_all_students_service()

#Update student by id
@students.route("/student-management/student/<int:id>", methods=['PUT'])
def update_student_student_by_id(id):
    return update_student_by_id_service(id)

#Delete student by id
@students.route("/student-management/student/<int:id>", methods=['DELETE'])
def delete_student_by_id(id):
    return delete_student_by_id_service(id)

