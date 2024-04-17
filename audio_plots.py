import matplotlib.pyplot as plt
from scipy.signal import spectrogram
import numpy as np
import librosa
import librosa.display

def plot_waveform(audio_data, sample_rate):
    audio_data_float = audio_data.astype(float)

    librosa.display.waveshow(audio_data_float, sr=sample_rate, color = "blue", alpha = 0.4)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Waveform")
    plt.savefig("Waveform.png")

def plot_fft_spectrum(left_freq, left_mag):

    #LOG SCALE

    plt.figure(figsize=(10, 5))
    plt.plot(left_freq, left_mag)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.xscale('log')
    plt.xlim([20, 20000])
    plt.title('FFT Spectrum')
    plt.grid(True)
    plt.savefig('fft_spectrum')

def plot_spectrogram(audio_data, sample_rate):
    nperseg = 512  # Window size
    noverlap = nperseg // 2  # Overlap between windows

    # Compute spectrogram
    f, t, Sxx = spectrogram(audio_data, fs=sample_rate, nperseg=nperseg, noverlap=noverlap)

    # Plot spectrogram
    plt.figure(figsize=(10, 5))
    plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
    
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [s]')
    plt.title('Spectrogram')
    plt.colorbar(label='Intensity [dB]')
    plt.savefig('spectrogram')

def plot_mfccs(mfccs, sample_rate):
    plt.figure(figsize=(10, 5))
    librosa.display.specshow(mfccs, sr=sample_rate, x_axis='time')
    plt.ylabel("MFCC Coefficients")
    plt.colorbar()
    plt.savefig("MFCCs.png")