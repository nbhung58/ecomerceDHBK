from numpy import append
import psycopg2
from ecomere.setting import conn
from flask import request, jsonify
from ecomere.library_ma import CustomersSchema
import json
from psycopg2.extras import DictCursor

customer_schema = CustomersSchema()

def add_customer_service():
    data = request.json
    query = "INSERT INTO customers (customer_name,contact_name,address,city,postalcode,country) VALUES (%s,%s,%s,%s,%s,%s)"
    if ((data and 'customer_name' in data)and('contact_name' in data) and ('address'in data) 
    and ('city' in data) and ('postalcode'in data) and ('country' in data)):
        customer_name = data['customer_name']
        contact_name = data['contact_name']
        address = data['address']
        city = data['city']
        postalcode = data['postalcode']
        country = data['country']  
        data = (customer_name, contact_name, address, city, postalcode, country)
        print(data)
        try:
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            cursor.close()
            return "Add success"
        except Exception as e:
            print(e)
            conn.rollback()
            return "Can not add Customer"
    else:
        return "Request error"

def get_customer_service_by_id(id):
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM customers WHERE customerid = {id}")
        rows = cur.fetchall()
        #print(rows[0])
        for row in rows:
            data = {
                "Customer name": row[1],
                "Contact name": row[2],
                "Address": row[3],
                "City": row[4],
                "Postal Code": row[5],
                "Country": row[6]
            }
        #print(data)
        if rows:
            return data
        else:
            return "Not found customer"
    except IndentationError:
        print(IndentationError)
        return "Request error"

def get__all_customer_service():
    try:
        data = []
        #cur = conn.cursor()
        #cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur = conn.cursor(cursor_factory=DictCursor)
        cur.execute("SELECT * FROM customers")
        rows = cur.fetchall()
        #print(rows[0])
        # keys =  ["Customer Id", "Customer name", "Contact name", "Address", "City", "Postal Code", "Country"]
        # data = [{k: v for k, v in zip(keys, tup)} for tup in rows]
        # data_json =json.dumps(data, indent=6)
        for row in rows:
            data.append(dict(row))
        #data = json.dumps(data, indent=6)
        cur.close()
        #print(data_json)
        if rows:
            return jsonify(data)
        else:
            return "Not found customer"
        
    except IndentationError:
        print(IndentationError)
        return "Request error"

def update_address_customer_by_id_service(id):
    data = request.json
    #print(data["address"])
    query = "UPDATE customers SET address = %s WHERE customerid = %s "
    updated_rows = 0
    try:
        cur = conn.cursor()
        cur.execute(query, (data["address"], id))
        updated_rows = cur.rowcount
        print(updated_rows)
        conn.commit()
        cur.close()
        return  f"Updated address to Customer-{id} successfully "
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return "Can not updated address customer"
    finally:
        if conn is not None:
            conn.close()

def  delete_customer_by_id_service(id):
    try: 
        cur = conn.cursor()
        cur.execute(f"DELETE FROM customers WHERE customerid = {id}")
        conn.commit()
        conn.close()
        return "Delete customer success",200
    except Exception as e:
        return f"Delete fail, {e}"



    
