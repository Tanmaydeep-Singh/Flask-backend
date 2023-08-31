import pyrebase

config = {
    "apiKey": "AIzaSyA7zeXn4hCOKmB_Ju2cW408Q4b2-FY6dY0",
    "authDomain": "spotify-adder-cc943.firebaseapp.com",
    "projectId": "spotify-adder-cc943",
    "storageBucket": "spotify-adder-cc943.appspot.com",
    "messagingSenderId": "979522366996",
    "appId": "1:979522366996:web:ce888684c93e376c1e4101",
    "measurementId": "G-1X4NZZ8Y2H",
    "databaseURL":"",
  };


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def authanticateUser(email,password):
    auth.create_user_with_email_and_password(email,password)
    print("SUCCESS")

# user = auth.sign_in_with_email_and_password(email, password)

# print(user)