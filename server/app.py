from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
from model.listing import Listing
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
     


@app.route('/login',methods=["POST"])
def loginUser():
    try:
        # Retrieve request data
        admin_json = request.json
        email = admin_json['email']
        password = admin_json['password']

        if not email or not password:
            return jsonify({"message": "Email and password are required"}), 400
        
        #Call the login method
        result = User.login(email, password)

        return jsonify(result), 200

    except Exception as err:
        print(err)
        return jsonify({"Message": "Error"}), 500

@app.route('/travel', methods=["POST"])
@login_required
def insertListing():

    try:
            # retrieve required data
            travelJSON=request.json
            title=travelJSON['title']
            description=travelJSON['description']
            price=travelJSON['price']
            country=travelJSON['country']
            travelPeriod=travelJSON['travel_period']
            imageURL=travelJSON['imageURL']

            #call model
            recs=Listing.insertListing(title, description, price, country, travelPeriod,imageURL)

            msg=str(recs)+" record(s) inserted"
            return jsonify({"message":msg}),201

    except Exception as err:

            print(err)
            return jsonify ({"Message": "Error"}), 500
       
@app.route('/updatelisting/<int:travelID>', methods=['PUT'])
@login_required
def updateListing(travelID): #dateInserted
    
    print(g.role)
    print(g.userid)

    if g.role!="admin":
        return jsonify({"Message":"You are not authorized"}),401

    try:
        #retrieve req data
        listingJSON=request.json

        title = listingJSON ['title']
        description = listingJSON ['description']
        price = listingJSON ['price']
        country = listingJSON ['country']
        travelPeriod = listingJSON ['travel_period']
        imageURL = listingJSON ['imageURL']
        
        #call model 
        recs=Listing.updateListing(title, description, price, country, travelPeriod, imageURL, travelID) #dateInserted

        return jsonify(recs),200

    except Exception as err:

        print(err)
        return jsonify({"Message":"Error"}),500

if __name__ == "__main__":
    app.run(debug=True)
