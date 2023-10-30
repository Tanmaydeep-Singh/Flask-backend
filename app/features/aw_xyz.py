import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt

def aw_new_xyz(data):
    time = np.array(data['Time'].values[1:] , dtype=float)
    ax = np.array(data['X'].values[1:]  , dtype=float)
    ay = np.array(data['Y'].values[1:]  , dtype=float)
    az = np.array(data['Z'].values[1:]  , dtype=float)

    # Butterworth band-pass filter
    t1 = time[2]
    t0 = time[1]
    
    f1, f2 = 0.4, 100  
    b_s, a_s = butter(2, [f1, f2], btype='bandpass', fs=1.0/( t1 - t0 ))
    b = np.array(b_s , dtype=float)
    a = np.array(a_s , dtype=float)
    ax_filtered = filtfilt(b, a, ax)
    ay_filtered = filtfilt(b, a, ay)
    az_filtered = filtfilt(b, a, az)

    # Compute the squared weighted acceleration for each series
    aw2_x = (1.4 * ax_filtered)**2
    aw2_y = (1.4 * ay_filtered)**2
    aw2_z = az_filtered**2  # Already includes Wk weighting

    # Compute the weighted acceleration for each value

    T = time[-1] - time[0]
    aw_x_values = [np.sqrt(np.trapz(aw2_x[:i+1], dx=(t1-t0)) / T) for i in range(len(time))]
    aw_y_values = [np.sqrt(np.trapz(aw2_y[:i+1], dx=(t1-t0)) / T) for i in range(len(time))]
    aw_z_values = [np.sqrt(np.trapz(aw2_z[:i+1], dx=(t1-t0)) / T) for i in range(len(time))]


    # Append results to your DataFrame
    # data['aw_Xnew'] = aw_x_values
    # data['aw_Ynew'] = aw_y_values
    # data['aw_Znew'] = aw_z_values

    awx = np.mean(aw_x_values)
    awy = np.mean(aw_y_values)
    awz = np.mean(aw_z_values)

    return { "aw_Xnew": aw_x_values,
             "aw_Ynew": aw_y_values,
             "aw_Znew": aw_z_values,
             "awx": awx,
             "awy": awy,
             "awz": awz,
           }