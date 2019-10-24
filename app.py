from db import *
from spectrogram import *
import sounddevice as sd
import time
import sys
from login import *
import numpy as np
from matplotlib import pyplot as plt

fs = 44100
sd.default.samplerate = fs
sd.default.channels = 2


def display_menu():
    print('''
                What would you like to do?

                1) Recognise a song
                2) Fingerprint a song
                3) Search for a song
                4) Quit
            ''')

def record_audio():
    recording = sd.rec(int(duration * fs))
    sd.wait()
    return recording
    

clear()
welcome_screen()
username = login_menu()

display_menu()
value = int(input('Enter your desired operation:- '))

try:
    while True:

        if value == 1:
            print('Audio will be recorded in ')
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')

        
            print('Recording Started')
            duration = 3
            #recording = record_audio()
            recording = record_audio()
            print('Recorded')
            #sd.play(recording)
            #print(row for row in recording)

            recording = recording.tolist()
            transformed_array = []
            magnitude_fft = []
            for row in recording:
                transformed_array.append(cooley_tukey(list(row)))
                magnitude_fft.append(np.absolute(row))
                
            transformed_array = np.array(transformed_array)
            magnitude_fft = np.array(magnitude_fft)
            #print(transformed_array)
            #print(magnitude_fft)
            amplitude = []
            for row in magnitude_fft:
                amplitude.append((row[0] + row[1]) / 2.0)
            print(amplitude)
            plt.plot([x for x in range(len(amplitude))], amplitude)
            plt.show()      
            input('Press any key to continue...')
            clear()

            display_menu()
            value = int(input('Enter your desired operation:- '))
        elif value == 2:
            print('Fingerprint a song')
            input('Press any key to continue...')
            clear()

            display_menu()
            value = int(input('Enter your desired operation:- '))

        elif value == 3:
            print('Search for the song')
            input('Press any key to continue...')
            clear()

            display_menu()
            value = int(input('Enter your desired operation:- '))
        elif value == 4:
            clear()
            print('Thank you for using PiedPiper {}'.format(username))
            time.sleep(2)
            sys.exit()
    
except Exception as e:
    print('Exception Raised: ' + str(e))

