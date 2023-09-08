import pandas as pd
import numpy as np

def calculate(f):
    df = f
    df

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

    data = {'Column1': listX}
    df = pd.DataFrame(data)

    csv_file_path = 'my_dataX.csv'

    df.to_csv(csv_file_path, index=False)

    data = {'Column1': listY}
    df = pd.DataFrame(data)

    csv_file_path = 'my_dataY.csv'

    df.to_csv(csv_file_path, index=False)

    data = {'Column1': listZ}
    df = pd.DataFrame(data)

    csv_file_path = 'my_dataZ.csv'

    df.to_csv(csv_file_path, index=False)

    sixthPowerX, sixthPowerY, sixthPowerZ = 0, 0, 0

    for i in listX:
        sixthPowerX = sixthPowerX + pow(i, 6)

    for i in listY:
        sixthPowerY = sixthPowerY + pow(i, 6)

    for i in listZ:
        sixthPowerZ = sixthPowerZ + pow(i, 6)

    print(sixthPowerX, sixthPowerY, sixthPowerZ)

    dx, dy, dz = pow(sixthPowerX, 1/6), pow(sixthPowerY, 1/6), pow(sixthPowerZ, 1/6)
    print(dx, dy, dz)

    tm = 0.017252778
    td = 8

    print(pow(td/tm, 1/6))

    print(dx*pow(td/tm, 1/6), dy*pow(td/tm, 1/6), dz*pow(td/tm, 1/6))

    mx = 0.015
    my = 0.035
    mz = 0.032

    print(mx*dx, my*dy, mz*dz)

    print(pow(mx*dx, 6), pow(my*dy, 6), pow(mz*dz, 6))

    s = pow(mx*dx, 6) + pow(my*dy, 6) + pow(mz*dz, 6)
    sc = pow(s, 1/6)
    print(sc)

    std = pow(mx*dx*pow(td/tm, 1/6), 6) + pow(my*dy*pow(td/tm, 1/6), 6) + pow(mz*dz*pow(td/tm, 1/6), 6)
    std = pow(std, 1/6)
    print(std)

    N =	100
    e = 5
    i =	3
    n =	5
    c =	0.25
    b = 25

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

    print(rs)

    print(pow(sum(rs), 1/6))

    return "CALCULATE FUNCTION CALLED"



