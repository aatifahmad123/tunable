import librosa
import matplotlib.pyplot as plt
import numpy as np

song_filename = "./data/songs/saajna.mp3"

def get_waveform(filename):

    y,sr = librosa.load(filename)

    return y

def visualize_waveform(y):

    print(f'y : {y}')

    print(f'Length of y : {len(y)}')

    x = np.array(range(len(y)))

    print(f'x : {x}')

    plt.plot(x,y,c='r')
    plt.title('Song File Processing')
    plt.xlabel('Samples')
    plt.ylabel('Amplitude')
    plt.show()

y = get_waveform(song_filename)
visualize_waveform(y)

