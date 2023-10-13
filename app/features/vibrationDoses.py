import numpy as np
import pandas as pd

def vibration_doses_xyz(data,aw,awx,awy,awz):
    # aw = 0.0768150248245908
    time = float(data['Time'].iloc[-1])  # Gets the last time value
    # Compute VDV
    VDV = (aw**4 * time)**(1/4)

    # print(f"Vibration Dose Value (VDV): {VDV}")

    # awx = 0.0280107419762848
    # awy = 0.0187199996886411
    # awz = 0.0705823494490521
    # Compute VDV for each axis
    VDV_x = (awx**4 * time)**(1/4)
    VDV_y = (awy**4 * time)**(1/4)
    VDV_z = (awz**4 * time)**(1/4)
    # print(f"Vibration Dose Value (VDV_x): {VDV_x}")
    # print(f"Vibration Dose Value (VDV_y): {VDV_y}")
    # print(f"Vibration Dose Value (VDV_z): {VDV_z}")
    
    return { "VDV": VDV, "VDV_X": VDV_x, "VDV_Y": VDV_y, "VDV_Z": VDV_z}