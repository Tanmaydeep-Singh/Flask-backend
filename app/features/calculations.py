import pandas as pd
import numpy as np
from .raw_peak_data import *

def calculate(f,tm,td,N,i,n,c,b):
    df = f
    df

    time = df['Time'][2]
    
    alX_list, alY_list, alZ_list = df['Seatpad-X'].to_list(), df['Seatpad-Y'].to_list(), df['Seatpad-Z'].to_list()
    alX_list = [float(x) for x in alX_list[1:]]
    alY_list = [float(x) for x in alY_list[1:]]
    alZ_list = [float(x) for x in alZ_list[1:]]

    def has_same_sign(num1, num2):
        return (num1 >= 0 and num2 >= 0) or (num1 < 0 and num2 < 0)

    def getLists(al_list):
      splitted = []
      nums = [al_list[0]]
      for i in range(1, len(al_list)):
        if(has_same_sign(al_list[i], al_list[i-1]) == True):
          nums.append(al_list[i])
        else:
          splitted.append(nums)
          nums = [al_list[i]]
      return splitted


    splitted_x = getLists(alX_list)
    splitted_y = getLists(alY_list)
    splitted_z = getLists(alZ_list)

    raw_peak_x, raw_time_x, raw_pos_x ,raw_neg_x = raw_data_peak(alX_list,time)
    raw_peak_y, raw_time_y, raw_pos_y ,raw_neg_y  = raw_data_peak(alY_list,time)
    raw_peak_z, raw_time_z, raw_pos_z ,raw_neg_z  = raw_data_peak(alZ_list,time)

    print("pos", raw_pos_x)
    print("neg", raw_neg_x)

    raw_max_pos = max([raw_pos_x, raw_pos_y, raw_pos_z])
    raw_max_neg = min([raw_neg_x, raw_neg_y, raw_neg_z])

    print(len(raw_peak_x))
    print(len(raw_time_x))

    def splitPosNeg(splitted):
      pos, neg = [], []
      for l in splitted:
        if(l[0] > 0):
          pos.append(l)
        else:
          neg.append(l)
      return pos, neg

    pos_x, neg_x = splitPosNeg(splitted_x)
    pos_y, neg_y = splitPosNeg(splitted_y)

    listX, listY, listZ = [], [], []

    for i in range(min(len(pos_x), len(neg_x))):
      listX.append(max(max(pos_x[i]), max(neg_x[i])))

    for i in range(min(len(pos_y), len(neg_y))):
      listY.append(max(max(pos_y[i]), max(neg_y[i])))

    for l in splitted_z:
      if(l[0] > 0):
        listZ.append(max(l))

    {'Column1': listX}  
    {'Column1': listY}
    {'Column1': listZ}
  
    sixthPowerX, sixthPowerY, sixthPowerZ = 0, 0, 0

    for i in listX:
        sixthPowerX = sixthPowerX + pow(i, 6)

    for i in listY:
        sixthPowerY = sixthPowerY + pow(i, 6)

    for i in listZ:
        sixthPowerZ = sixthPowerZ + pow(i, 6)

    print("SIXTHPOWER X-Y-Z")
    print(sixthPowerX, sixthPowerY, sixthPowerZ)

    dx, dy, dz = pow(sixthPowerX, 1/6), pow(sixthPowerY, 1/6), pow(sixthPowerZ, 1/6)
    print("DX-DY-DZ")
    print(dx, dy, dz)

    print("tm 7 td")
    tm = float(tm)
    td = float(td)  
    
    print("TD/TM power 1/6")
    print(pow(td/tm, 1/6))

    print("DX-DY-DX * TD/TM power 1/6")
    print(dx*pow(td/tm, 1/6), dy*pow(td/tm, 1/6), dz*pow(td/tm, 1/6))

    mx = 0.015
    my = 0.035
    mz = 0.032

    print("MX*DX MY*DY MZ*DX")
    print(mx*dx, my*dy, mz*dz)

    print("MX*DX MY*DY MZ*DX POWER 6")
    print(pow(mx*dx, 6), pow(my*dy, 6), pow(mz*dz, 6))

    s = pow(mx*dx, 6) + pow(my*dy, 6) + pow(mz*dz, 6)
    sc = pow(s, 1/6)
    print("SE")
    print(sc)

    std = pow(mx*dx*pow(td/tm, 1/6), 6) + pow(my*dy*pow(td/tm, 1/6), 6) + pow(mz*dz*pow(td/tm, 1/6), 6)
    std = pow(std, 1/6)
    print("STD")
    print(std)

    N =	float(N)
    e = int(n)
    n = float(n)
    i =	float(i)
    c =	float(c)
    b = float(b)

    suis = []

    for i in range(1,e+1):
        suis.append(6.75 - 0.066*(b+i))
    
    print(6.75 - 0.066*(b+i))

    suics = []
    for i in range(len(suis)):
        suics.append(suis[i] - c)

    print(suics)

    rs = []

    for i in suics:
        rs.append(pow(std*pow(N, 1/6)/(i), 6))
    
    print("RS")
    print(rs)

    print("RS POW 1/6")
    print(pow(sum(rs), 1/6))
    r=pow(sum(rs), 1/6)
    data = {} 
    data = {"se":sc, "sed": std, "r": r, "raw_peak_x": raw_peak_x, "raw_time_x": raw_time_x, "raw_peak_y": raw_peak_y, "raw_time_y": raw_time_y, "raw_peak_z": raw_peak_z, "raw_time_z": raw_time_z, "raw_pos_x":raw_pos_x ,"raw_neg_x": raw_neg_x,"raw_pos_y":raw_pos_y ,"raw_neg_y": raw_neg_y, "raw_pos_z":raw_pos_z ,"raw_neg_z": raw_neg_z, "raw_max_pos":raw_max_pos,"raw_max_neg": raw_max_neg }
    return data


