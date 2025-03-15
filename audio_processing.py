import librosa
import matplotlib.pyplot as plt
import numpy as np

filename = "./assets/songs/khileya.mp3"

y,sr = librosa.load(filename)

print(y,len(y))

x = np.array(range(len(y)))

print(x)

plt.plot(x,y,c='r')
plt.title('Initial Audio Processing')
plt.show()