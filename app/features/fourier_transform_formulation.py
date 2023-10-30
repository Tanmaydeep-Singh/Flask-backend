import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, welch

def fourier_transform_function(data):
  # print("hi")
  # print(data)
    # Extract the columns for time and acceleration
    time = np.array(data['Time'].values[1:], dtype=float)
    time = time - np.min(time)  # Adjust time to start from 0
    acc1 = np.array(data['X'].values[1:], dtype=float)
    acc2 = np.array(data['Z'].values[1:], dtype=float) - 1
  # print("check 1")

    # Use n data points
    nDataPts = 30000
    time1 = time[:nDataPts]
    ref1_unfiltered = acc1[:nDataPts]
    proto1_unfiltered = acc2[:nDataPts]

    # Remove outliers
    ref1_mean = np.mean(ref1_unfiltered)
    ref1_std = np.std(ref1_unfiltered)
    outlier_indices_ref1 = np.abs(ref1_unfiltered - ref1_mean) > 3 * ref1_std
    ref1_unfiltered[outlier_indices_ref1] = ref1_mean

    proto1_mean = np.mean(proto1_unfiltered)
    proto1_std = np.std(proto1_unfiltered)
    outlier_indices_proto1 = np.abs(proto1_unfiltered - proto1_mean) > 3 * proto1_std
    proto1_unfiltered[outlier_indices_proto1] = proto1_mean

    def low_pass_filter(cutoff, fs, order, data):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        y = filtfilt(b, a, data)
        return y

    ref1_filtered = low_pass_filter(50, 500, 2, ref1_unfiltered)
    proto1_filtered = low_pass_filter(50, 500, 2, proto1_unfiltered)

    N = len(time1)
    f = np.fft.fftfreq(N, 1/500)[:N//2]
    fft_ref1_unfiltered = np.fft.fft(ref1_unfiltered)[:N//2]
    fft_proto1_unfiltered = np.fft.fft(proto1_unfiltered)[:N//2]
    fft_ref1_filtered = np.fft.fft(ref1_filtered)[:N//2]
    fft_proto1_filtered = np.fft.fft(proto1_filtered)[:N//2]

    # Compute the magnitude spectrum
    magnitude_spectrum_ref1_unfiltered = np.abs(fft_ref1_unfiltered)/N
    magnitude_spectrum_proto1_unfiltered = np.abs(fft_proto1_unfiltered)/N
    magnitude_spectrum_ref1_filtered = np.abs(fft_ref1_filtered)/N
    magnitude_spectrum_proto1_filtered = np.abs(fft_proto1_filtered)/N

    f_psd, psd_ref1_unfiltered = welch(ref1_unfiltered, fs=500)
    _, psd_proto1_unfiltered = welch(proto1_unfiltered, fs=500)
    _, psd_ref1_filtered = welch(ref1_filtered, fs=500)
    _, psd_proto1_filtered = welch(proto1_filtered, fs=500)

    # Create a function to simplify the plotting
    def plot_setup(ax, xlabel, ylabel, xlim, xticks):
        ax.set_xlabel(xlabel, fontweight='bold', fontsize=20)
        ax.set_ylabel(ylabel, fontweight='bold', fontsize=20)
        ax.set_xlim(xlim)
        ax.set_xticks(xticks)
        ax.tick_params(axis='both', which='major', labelsize=18)
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    fig, ax = plt.subplots(3, 2, figsize=(14, 10))

    # Unfiltered data plots
    ax[0, 0].plot(time1, ref1_unfiltered, 'b', linewidth=3)
    plot_setup(ax[0, 0], "", "Amp. (m/s^2)", [0, 30], range(0, 32, 2))
    ax[0, 0].legend(['Reference'])

    ax[0, 1].plot(time1, proto1_unfiltered, 'r', linewidth=3)
    plot_setup(ax[0, 1], "", "Amp. (m/s^2)", [0, 30], range(0, 32, 2))
    ax[0, 1].legend(['Prototype'])

    ax[1, 0].plot(f, magnitude_spectrum_ref1_unfiltered, 'b', linewidth=3)
    plot_setup(ax[1, 0], "", "Magnitude", [0, 30], range(0, 32, 2))

    ax[1, 1].plot(f, magnitude_spectrum_proto1_unfiltered, 'r', linewidth=3)
    plot_setup(ax[1, 1], "", "Magnitude", [0, 30], range(0, 32, 2))

    ax[2, 0].plot(f_psd, 10*np.log10(psd_ref1_unfiltered), 'b', linewidth=3)
    plot_setup(ax[2, 0], "Frequency (Hz)", "PSD (dB/Hz)", [0, 30], range(0, 32, 2))

    ax[2, 1].plot(f_psd, 10*np.log10(psd_proto1_unfiltered), 'r', linewidth=3)
    plot_setup(ax[2, 1], "Frequency (Hz)", "PSD (dB/Hz)", [0, 30], range(0, 32, 2))
    data_dict = {}
    # plt.tight_layout()
    # plt.show() 

    print("time",time1)
    print("ref",ref1_unfiltered )
    print( "proto1_unfiltered",proto1_unfiltered)

    data_dict ={"Amp" : {"time":time1.tolist(), "ref1_unfiltered":ref1_unfiltered.tolist(), "proto1_unfiltered":proto1_unfiltered.tolist() }, "Magnitude": {"frequency":f.tolist(), "magnitude_spectrum_ref1_unfiltered":magnitude_spectrum_ref1_unfiltered.tolist(), "magnitude_spectrum_proto1_unfiltered":magnitude_spectrum_proto1_unfiltered.tolist()},"Frequency": {"f_psd":f_psd.tolist(), "psd_ref1_unfiltered":10*np.log10(psd_ref1_unfiltered).tolist(), "psd_proto1_unfiltered":10*np.log10(psd_proto1_unfiltered).tolist() }}

    return data_dict
