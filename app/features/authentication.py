import pyrebase

config = {
    "apiKey": "AIzaSyA7zeXn4hCOKmB_Ju2cW408Q4b2-FY6dY0",
    "authDomain": "spotify-adder-cc943.firebaseapp.com",
    "projectId": "spotify-adder-cc943",
    "storageBucket": "spotify-adder-cc943.appspot.com",
    "messagingSenderId": "979522366996",
    "appId": "1:979522366996:web:ce888684c93e376c1e4101",
    "measurementId": "G-1X4NZZ8Y2H",
    "databaseURL":"https://spotify-adder-cc943-default-rtdb.asia-southeast1.firebasedatabase.app/",
  }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

def authanticateUser(email,password):
    user =auth.create_user_with_email_and_password(email,password)
    user_id = user.get('localId')
    data = {
        "email":email,
        "username":"name",
        "message":"HelloBitch"
    }
    db.child("users").child(user_id).push(data)
    print("SUCCESS")

def loginUser(email,password):
    print("called")
    user = auth.sign_in_with_email_and_password(email, password)
    user_id = user.get('localId')
    print(user_id)
    all_user = db.child("users").child(user_id).get()
    return all_user.val()

def reset(email):
    auth.send_password_reset_email(email)
   
   