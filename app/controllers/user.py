from flask import jsonify, request
from app import app
from ..features.authentication import *

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
def loginUser():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	loginUser(email,password)
	return data

@app.route('/reset-password', methods=['POST'])
def resetPassword():
	data = request.get_json()
	email = data.get('email')
	reset(email)
	return data
	