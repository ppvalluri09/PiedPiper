import sounddevice as sd
import time
#from matplotlib import pyplot as plt
from math import log2
from cmath import exp, pi
from random import random
import numpy as np
from itertools import chain
from scipy.io import wavfile
import pydub

fs = 44100
sd.default.samplerate = fs
sd.default.channels = 2

#normal slow dft
def dft(X):
    N = len(X)
    temp  = [0]*N
    for i in range(N):
        for k in range(N):
            temp[i] += X[k] * exp(-2j*pi*i*k/N)

    result = np.asarray(temp)
    return result

#cooley tukey for calculating dft(O(nlogn)) 
def cooley_tukey(X):
    N = len(X)
    if N<=1:
        return X
    even = cooley_tukey(X[0::2])
    odd = cooley_tukey(X[1::2])

    temp = [i for i in range(N)]
    for k in range(N//2):
        temp[k] = even[k] + exp(-2.0j*pi*k/N)*odd[k]
        temp[k+N//2] = even[k] - exp(-2.0j*pi*k/N)*odd[k]
    result = np.asarray(temp)
    return result

def record_audio(d = -1):
    if d == -1:
        duration = int(input('Enter the duration of recording: '))
    else:
        duration = d
    print('I\'m all ears ')
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
        
    print('Listening...')
    
    recording = sd.rec(int(duration * fs))
    sd.wait()
    print('Ahaan, got that')
    return duration, recording.tolist()

def get_amplitude(sample):
    transformed_array = []
    magnitude_fft = []
    for row in sample:
        transformed_array.append(cooley_tukey(list(row)))
        magnitude_fft.append(np.absolute(row))
                
    transformed_array = np.array(transformed_array)
    magnitude_fft = np.array(magnitude_fft)
    amplitude = []
    for row in magnitude_fft:
        amplitude.append((row[0] + row[1]) / 2.0)

    return amplitude

def plot_data(data):
    plt.plot([x for x in range(len(data))], data)
    plt.show()

def scatter_data(data):
    plt.scatter([x for x in range(len(data))], data, s = 1, c = 'r')
    plt.show()

def to_mel(data):
    for i in range(len(data)):
        data[i] = 2595 * np.log10(1 + (data[i]/700))
    return data

def to_list(data):
    return list(chain.from_iterable(data))

def get_chunks(data, duration):
    duration = duration * 1000
    n_chunks = int(len(data) / duration)
    chunk_peaks = []
    prev = 0
    for i in range(n_chunks):
        row = list(data[prev:prev + duration])
        row.sort(reverse=True)
        row = list(row[:50])    
        chunk_peaks.append(row)
        prev = prev + duration
    return chunk_peaks

def calculate_confidence(data, duration):
        chunk_peaks = get_chunks(data, duration)
        confidence = 0

        for row in chunk_peaks:
            confidence = confidence + sum(abs(row - max(row)))

        return confidence


def fingerprint(recording, duration):
    print('Generating Fingerprint')
    amplitude = get_amplitude(recording)
    confidence = calculate_confidence(amplitude, duration)
    return confidence

