# import collections
# from app import app
# import pyrebase
# from pymongo import MongoClient
# from datetime import datetime

# config = {
#     "apiKey": "AIzaSyA7zeXn4hCOKmB_Ju2cW408Q4b2-FY6dY0",
#     "authDomain": "spotify-adder-cc943.firebaseapp.com",
#     "projectId": "spotify-adder-cc943",
#     "storageBucket": "spotify-adder-cc943.appspot.com",
#     "messagingSenderId": "979522366996",
#     "appId": "1:979522366996:web:ce888684c93e376c1e4101",
#     "measurementId": "G-1X4NZZ8Y2H",
#     "databaseURL": ""
#   }

# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()

# client = MongoClient('mongodb+srv://Tanmaydeep:tanmay@cluster1.vcm3w.mongodb.net/Lumber-spine')
# db = client["mydatabase"]
# collection = db["collection"]


# def authanticateUser(email,password):
#     # user =auth.create_user_with_email_and_password(email,password)
#     # user_id = user.get('localId')
#     # result = collection.insert_one({ "user_id": user_id, "data_list": []})
#     return "user_id"

# def loginUser(email,password):
#     # user = auth.sign_in_with_email_and_password(email, password)
#     # user_id = user.get('localId')
#     return "user_id"

# def reset(email):
#     auth.send_password_reset_email(email)
   
# def addUserData(user_id, data):
#     user = collection.find_one({"user_id":user_id})
#     current_datetime = datetime.now()
#     current_timestamp = current_datetime.timestamp()
#     new_block = {
#         "Time":current_timestamp,
#         "data": data
#     }
#     new_data_list = user.get("data_list")
#     new_data_list.append(new_block)

#     collection.update_one({"user_id": user_id}, {"$set": {"data_list" :new_data_list}})

#     return "ok"

# def getUserHistory(user_id):

#     user = collection.find_one({"user_id":user_id})
#     return user

