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
	

