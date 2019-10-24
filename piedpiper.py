import sounddevice as sd
from spectrogram import *
from matplotlib import pyplot as plt

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

def to_mel(data):
    for i in range(len(data)):
        data[i] = 2595 * np.log10(1 + (data[i]/700))
    return data
