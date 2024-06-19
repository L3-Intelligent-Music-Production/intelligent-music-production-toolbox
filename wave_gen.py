import numpy as np


def audio_specs(sr, freq, duration):
    length = int(sr * duration)
    t = np.arange(length)/sr
    x = t * freq * np.pi * 2
    return x

def sin_gen(sr, freq, duration):
    x = audio_specs(sr, freq, duration)
    sin = np.sin(x)
    return sin

def saw_gen(sr, freq, duration):
    x = audio_specs(sr, freq, duration)
    saw = -((x/np.pi) % 2) + 1
    return saw

def tri_gen(sr, freq, duration):
    x = audio_specs(sr, freq, duration)
    tri = np.abs((x/np.pi)% 2 - 1) * 2 - 1
    return tri

def sqr_gen(sr, freq, duration):
    x = audio_specs(sr, freq, duration)
    sqr = np.where(x/np.pi % 2 < 1, -1, 1)
    return sqr
