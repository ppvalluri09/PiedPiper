import sounddevice as sd
from spectrogram import *
from matplotlib import pyplot as plt
from itertools import chain

fs = 44100
sd.default.samplerate = fs
sd.default.channels = 2

def record_audio(duration):
    recording = sd.rec(int(duration * fs))
    sd.wait()
    return recording

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
        prev = prev + duration + 1
    return list(chain.from_iterable(chunk_peaks))
        
