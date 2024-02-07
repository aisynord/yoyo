from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
# from model.listing import Listing
from model.User import User
from validation.Authorisation import *

from dotenv import load_dotenv
load_dotenv() #to load environment variables from .env file

app = Flask(__name__, template_folder='../website', static_folder='../website')
CORS(app)

#Aisyah: HTML/JAVASCRIPT (return home)
#registerpage
@app.route('/register')
def register ():
     return render_template('registerpage/register.html')
#loginpage
@app.route('/log')
def log ():
     return render_template('template/login.html')

@app.route('/registerUser', methods=['POST'])
def registerNewUser():
     try:
          userJSON = request.json
          email = userJSON['email']
          name = userJSON['name']
          password = userJSON['password']
          role = userJSON['role']
          
          newUser = User.registerUser(email, name, password, role)
          msg = str(newUser) + " User Registered"
          return jsonify({"message":msg}), 201
     
     except Exception as err:
          print(err)
          return jsonify({"Message":"Error"}),500

if __name__ == "__main__":
    app.run(debug=True)