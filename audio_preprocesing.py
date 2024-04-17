import numpy as np
import librosa

def get_fft(audio_data, sample_rate):

    # Convert to dB full scale
    
    fft = np.fft.fft(audio_data, sample_rate)

    magnitude = np.abs(fft)
    frequency = np.linspace(0, sample_rate, len(magnitude))

    left_freq = frequency[:int(len(frequency)/2)]
    left_mag = magnitude[:int(len(frequency)/2)]
   
    return fft, left_freq, left_mag


def get_mfcc(audio_data, sample_rate, n_mfcc=13):

    audio_data_float = audio_data.astype(float)
    n_fft = 2048
    hop_length = 512

    mfccs = librosa.feature.mfcc(y=audio_data_float, sr=sample_rate, n_fft=n_fft, hop_length=hop_length, n_mfcc=13)

    
    return mfccs

