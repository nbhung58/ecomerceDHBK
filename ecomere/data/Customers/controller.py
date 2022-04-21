from cv2 import add
from flask import Blueprint, jsonify
from .services import (add_customer_service, get_customer_service_by_id, get__all_customer_service,
update_address_customer_by_id_service, delete_customer_by_id_service)


customer =Blueprint("Customer", __name__)

@customer.route("/customer",methods=["GET","POST"])
def index():
    return "hello"

@customer.route("/customer-management/customer", methods = ["POST"])
def add_customer():
    return add_customer_service()

@customer.route("/customer-management/customer/<int:id>", methods = ["GET"])
def get_customer_by_id(id):
    return get_customer_service_by_id(id)

@customer.route("/customer-management/customers", methods = ["GET"])
def get_all_customer():
    return get__all_customer_service()

@customer.route("/customer-management/<int:id>", methods = ["PUT"])
def update_address_customer(id,):
    return update_address_customer_by_id_service(id)

@customer.route("/customer-management/customer/<int:id>", methods = ["DELETE"])
def delete_customer_by_id(id):
    return delete_customer_by_id_service(id)
