## Audio utilities to handle music production code
from math import log10

def linear_amplitude_to_dBFS(amplitude):
    return 20 * log10(amplitude)

def dBFS_to_linear_amplitude(dBFS):
    return pow(10, dBFS/20)