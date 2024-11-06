from flask import jsonify, request
from app import app
from app.features.aw_overall import overall_aw_value
from app.features.aw_xyz import aw_new_xyz
from app.features.fourier_transform_formulation import fourier_transform_function
from app.features.vibrationDoses import vibration_doses_xyz
from ..features.calculations import *
import pandas as pd

@app.route('/user', methods = ['GET'])
def user():
	return "USER"

@app.route('/upload', methods=['POST'])
def upload_csv():
	headers = request.headers
	user_id = headers.get('Userid')
	td = request.form.get('td')
	tm = request.form.get('tm')
	N = request.form.get('N')
	i = request.form.get('i')
	n = request.form.get('n')
	c = request.form.get('c')
	b = request.form.get('b')

	file = request.files['file']
	f = pd.read_csv(file)
	trans = calculate(f,tm,td,N,i,n,c,b)

	# aw 
	aw_new = aw_new_xyz(f)
	
	# aw xyz
	aw_value = overall_aw_value(aw_new['aw_Xnew'], aw_new['aw_Ynew'], aw_new['aw_Znew']);
	
	# VDV
	vdv_values = vibration_doses_xyz(f, aw_value['aw'], aw_new['awx'], aw_new['awy'], aw_new['awz'] )

	# Fourier Transform
	ft_values = fourier_transform_function(f)
		
	return {"data" : trans, "vdv_values": vdv_values, "aw_new" : aw_new, "aw": aw_value, "ft": ft_values}

@app.route('/se', methods=['POST'])
def upload_csv_for_se():
	headers = request.headers
	user_id = headers.get('Userid')
	# print("user_id HEADER", user_id)
	td = request.form.get('td')
	tm = request.form.get('tm')

	# print('TD',td)
	# print('TM',tm)

	file = request.files['file']
	f = pd.read_csv(file)
	trans = calculate_se(f,tm,td)
	# addUserData(user_id, trans)
   
	return {"data" : trans}

# @app.route('/user-history')
# def get_user_history():
# 	headers = request.headers
# 	user_id = headers.get('Userid')
# 	print("user_id HEADER", user_id)
# 	data = getUserHistory(user_id)
# 	return {"userData" : data}

