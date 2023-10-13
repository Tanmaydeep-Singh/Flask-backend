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

	N = request.form.get('N')
	i = request.form.get('i')
	n = request.form.get('n')
	c = request.form.get('c')
	b = request.form.get('b')

	print('TD',td)
	print('TM',tm)
	print('N',N)
	print('i',i)
	print('n',n)
	print('c',c)
	print('b',b)

	file = request.files['file']
	f = pd.read_csv(file)
	trans = calculate(f,tm,td,N,i,n,c,b)
   
	return {"data" : trans}
