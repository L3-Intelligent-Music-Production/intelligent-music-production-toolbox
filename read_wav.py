from scipy.io import wavfile

# Bit Depth 
# Channel NUM

def read_audio_file(file_path):
    try:
        sample_rate, audio_data = wavfile.read(file_path)
        
        audio_length = audio_data.shape[0] / sample_rate

        return audio_data, audio_length, sample_rate
    except Exception as e:
        print("An error occurred:", e)
        return None, None, None



 
