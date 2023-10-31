import numpy as np
from scipy.signal import butter, filtfilt

def aw_new_xyz(data):
    time = data['Time'].values[1:].astype(float)
    ax = data['X'].values[1:].astype(float)
    ay = data['Y'].values[1:].astype(float)
    az = data['Z'].values[1:].astype(float)

    # Butterworth band-pass filter
    t1 = time[2]
    t0 = time[1]
    
    f1, f2 = 0.4, 100  
    b, a = butter(2, [f1, f2], btype='bandpass', fs=1.0 / (t1 - t0))
    ax_filtered = filtfilt(b, a, ax)
    ay_filtered = filtfilt(b, a, ay)
    az_filtered = filtfilt(b, a, az)

    # Compute the squared weighted acceleration for each series
    aw2_x = (1.4 * ax_filtered) ** 2
    aw2_y = (1.4 * ay_filtered) ** 2
    aw2_z = az_filtered ** 2  # Already includes Wk weighting

    # Compute the weighted acceleration for each value
    T = time[-1] - time[0]
    aw_x_values = np.sqrt(np.cumsum(aw2_x) / T)
    aw_y_values = np.sqrt(np.cumsum(aw2_y) / T)
    aw_z_values = np.sqrt(np.cumsum(aw2_z) / T)

    awx = np.mean(aw_x_values)
    awy = np.mean(aw_y_values)
    awz = np.mean(aw_z_values)

    return {
        "aw_Xnew": aw_x_values.tolist(),
        "aw_Ynew": aw_y_values.tolist(),
        "aw_Znew": aw_z_values.tolist(),
        "awx": awx,
        "awy": awy,
        "awz": awz,
    }
