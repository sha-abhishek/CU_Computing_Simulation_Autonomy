from matplotlib import pyplot as plt
import numpy as np 
#import scipy

#Frequency in terms of Hertz
fre  = 5 
#Sample rate
fre_samp = 50
t = np.linspace(0, 2, 2 * fre_samp, endpoint = False )
a = np.sin(fre  * 2 * np.pi * t)
figure, axis = plt.subplots()
axis.plot(t, a)
axis.set_xlabel ('Time (s)')
axis.set_ylabel ('Signal amplitude')
#plt.show()

#do DFT and visualize:
dft = np.fft.fft(a)/len(a)
N = len(dft)
n = np.arange(N)
f = n/(N/fre_samp)

figure, axis = plt.subplots()
axis.plot(f,np.abs(dft))
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude')
plt.show()