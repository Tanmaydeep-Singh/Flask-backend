from flask import jsonify, request
from app import app
from ..features.authentication import *
import csv
import io

@app.route('/user', methods = ['GET'])
def user():
	return "USER"

@app.route('/auth', methods = ['POST'])
def authUser():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	authanticateUser(email, password)
	return data

@app.route('/login', methods = ['POST'])
def userLogin():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	userData = loginUser(email,password)
	return userData

@app.route('/reset-password', methods=['POST'])
def resetPassword():
	data = request.get_json()
	email = data.get('email')
	reset(email)
	return data
	
@app.route('/upload', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        csv_data = file.read().decode("ISO-8859-1")  # Use the appropriate encoding
        csv_reader = csv.reader(csv_data)
        rows = list(csv_reader)
        return {"data": rows}
