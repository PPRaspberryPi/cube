import scipy.io.wavfile
import pydub
import matplotlib.pyplot as plt
import numpy as np
from numpy import fft as fft
mp3 = pydub.AudioSegment.from_mp3("music.mp3")

mp3.export("music.wav", format="wav")

rate, audData = scipy.io.wavfile.read("music.wav")

print(rate)
print(audData)

channel1=audData[:,0] #left
channel2=audData[:,1] #right

#create a time variable in seconds
time = np.arange(0, float(audData.shape[0]), 1) / rate

fourier=fft.fft(channel1)

#plot amplitude (or loudness) over time
plt.figure(1)
plt.subplot(211)
plt.plot(time, channel1, linewidth=0.01, alpha=0.7, color='#ff7f00')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.subplot(212)
plt.plot(time, channel2, linewidth=0.01, alpha=0.7, color='#ff7f00')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()