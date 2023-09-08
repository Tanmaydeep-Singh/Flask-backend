from flask import jsonify, request
from app import app
from ..features.authentication import *
from ..features.calculations import *
import csv
import io
import pandas as pd


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
	td = request.form.get('td')
	tm = request.form.get('tm')

	file = request.files['file']
	f = pd.read_csv(file)
	print("PD",f)
	trans = calculate(f,tm,td)
   
	return {"data" : trans}
