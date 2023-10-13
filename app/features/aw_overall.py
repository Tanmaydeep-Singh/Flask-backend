import numpy as np


def overall_aw_value(awx,awy,awz):
    # Assuming that wk values are for the z-axis and wd values are for the x and y axes
    wk = [
        31.2, 48.6, 79.0, 121, 182, 263, 352,
        418, 459, 477, 482, 484, 494, 531,
        631, 804, 967, 1039,1054, 1036,
        988, 902, 768, 636, 513, 405, 314,
        246, 186, 132, 88.7, 54.0, 28.5, 15.2,
        7.90, 3.98, 1.95
    ]

    wd = [
        62.4, 97.3, 158, 243, 365, 530, 713,
        853, 944, 992, 1011, 1008, 968, 890,
        776, 642, 512, 409, 323, 253, 212,
        161, 125, 100, 80.0, 63.2, 49.4, 38.8, 29.5,
        21.1, 14.1, 8.63, 4.55, 2.43, 1.26, 0.64,
        0.31
    ]

# Calculate the overall weighted acceleration using the given formula
    squared_sum = sum([(wk[i] * awz[i])**2 + (wd[i] * awx[i])**2 + (wd[i] * awy[i])**2 for i in range(len(wk))])
    aw = np.sqrt(squared_sum)

    return {"aw": aw}