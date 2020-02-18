import numpy as np # This is the main numerical library we will use
import matplotlib.pyplot as plt # This is the main plotting library we will use
import skimage # A library for doing some extra stuff with image processing
import scipy.io.wavfile as wavfile # We will use this library to load in audio
import IPython.display as ipd # This is a library that allows us to play audio samples in Jupyter

def save_wavfile(filename, fs, x):
    """
    Save audio to a wave file
    Parameters
    ----------
    filename: string
        Name of the file you want to save to
    fs: int
        Sample rate
    x: ndarray(N)
        Numpy array of audio samples
    """
    y = x-np.mean(x)
    y = y/np.max(np.abs(y))
    y = np.array(y*32768, dtype=np.int16)
    print(np.min(y))
    print(np.max(y))
    wavfile.write(filename, fs, y)
    


## TODO: Fill this in.  zred should hold the audio
fs = 44100
save_wavfile("red.wav", fs, zred)
