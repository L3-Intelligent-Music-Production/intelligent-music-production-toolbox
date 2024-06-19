# intelligent-music-production-toolbox
A set of audio and midi utilities for music production in python.

AudioFile.py:
  A class to store and process audio data
  - load_audio(file_path)
  - plot_audio()
  - get_notes()
     
audio_utilities.py:
- linear_amplitude_to_dBFS(amplitude)
- dBFS_to_linear_amplitude(dBFS)

audio_plots.py
- plot_waveform(audio_data, sample_rate)
- plot_fft_spectrum(left_freq, left_mag)
- plot_spectrogram(audio_data, sample_rate)
- plot_mfccs(mfccs, sample_rate)

audio_preprocesing.py
- get_fft(audio_data, sample_rate)
- get_mfcc(audio_data, sample_rate, n_mfcc)

midi_utilities.py:
- read_from_midi(file = './miditest.mid')
- write_to_midi(newFile = './new_song.mid')

read_wav.py:
- read_audio_file(file_path)

wave_gen.py:
- audio_specs(sr, freq, duration)
- sin_gen(sample_rate, frequency, duration)
- saw_gen(sample_rate, frequency, duration)
- tri_gen(sample_rate, frequency, duration)
- sqr_gen(sample_rate, frequency, duration)

**TODO:**
- get_bit_detph
- resample
- get_num_channels
- stereo_to_mono
- mono_to_dual_mono
- mono_to_stereo
- bit_depth_conversion
- dithering
- peak_normalize
- floating_point_normalization
