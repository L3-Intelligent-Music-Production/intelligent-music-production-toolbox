class AudioFile:
    """
    Class for audio files that includes basic operations

    Imports
    -------
    import numpy as np
    import torchaudio
    import librosa
    import plotly.express as px
    import torch
    import sys, os
    import pathlib
    """
    def __init__(self, file_path):

        format, audio_data, sample_rate, metadata = self.__load_audio(file_path)

        self.file_path = file_path
        self.format = format
        self.audio_data = audio_data
        self.sample_rate = sample_rate
        self.num_frames = metadata.num_frames
        self.num_channels = metadata.num_channels
        self.bits_per_sample = metadata.bits_per_sample
        self.encoding = metadata.encoding

        

    # Read audio file
    def __load_audio(self, file_path):
        # full_path = os.path.abspath('') + filepath
        full_path = file_path
        
        format = pathlib.Path(file_path).suffix[1:] # Substring to remove period
        print(f'Reading {format} file at {full_path}\n')

        audio_data, sample_rate = torchaudio.load(full_path)

        metadata = torchaudio.info(file_path)
        print(f'\nAudio metadata:\n {metadata}')
        
        print(f'Read {audio_data.size()} samples of audio with a sample rate of {sample_rate}\n')
        print(f'\n\nAudio data: \n{audio_data}\n\n')
        
        return format, audio_data, sample_rate, metadata

    def plot_audio(self):
        fig = px.scatter(self.audio_data)
        fig.show()
    

    def get_notes(self):
        fmin = librosa.note_to_hz('C0')
        fmax = librosa.note_to_hz('C7')

        pitches = librosa.pyin(self.audio_data.numpy(), fmin=fmin, fmax=fmax)
        notes = [librosa.hz_to_note(pitch) if not np.isnan(pitch) else 'NA' for pitch in pitches[0][0]]