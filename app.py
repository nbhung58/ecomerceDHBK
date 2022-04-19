from ecomere import create_app

if __name__ == "__main__":
    app= create_app()
    app.run(host="0.0.0.0", port =5000, debug=True)

# from django.shortcuts import render
# from flask import Flask, render_template
# import os

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return render_template('index.html', title='Docker Python', name='James')

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=os.environ[9999])