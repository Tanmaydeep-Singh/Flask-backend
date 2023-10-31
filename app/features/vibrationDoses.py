import numpy as np
import pandas as pd

def vibration_doses_xyz(data, aw, awx, awy, awz):
    time = float(data['Time'].iloc[-1])  # Gets the last time value
    
    # Calculate VDV for each axis
    VDV = lambda a: (a**4 * time)**(1/4)
    
    return {
        "VDV": VDV(aw),
        "VDV_X": VDV(awx),
        "VDV_Y": VDV(awy),
        "VDV_Z": VDV(awz)
    }
