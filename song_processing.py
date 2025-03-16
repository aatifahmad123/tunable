import librosa
import matplotlib.pyplot as plt
import numpy as np

song_filename = "./data/songs/saajna.mp3"

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

def get_interesting_points(y,sr,threshold=0.5):

    amps = np.abs(y)
    d_amps = np.diff(amps)
    d_amps_abs = np.abs(d_amps)

    interesting_points = np.where(d_amps_abs > threshold)[0]

    timestamps = interesting_points / sr
    
    return timestamps

def visualize_stft(y,sr):

    stft = librosa.stft(y)
    stft_abs = np.abs(stft)

    spectrogram = librosa.amplitude_to_db(stft_abs, ref=np.max)

    librosa.display.specshow(spectrogram, sr=sr, x_axis="time", y_axis="log")

    plt.title('Spectrogram (STFT)')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.show()

def get_frequencies():
    pass


y,sr = librosa.load(song_filename)

visualize_waveform(y)

# timestamps = get_interesting_points(y,sr)

# frequencies = get_frequencies()

visualize_stft(y,sr)


