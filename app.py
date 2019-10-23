from db import *
from spectrogram import *
import sounddevice as sd
import time
import sys
from login import *
import numpy as np

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
    return sd.rec(int(duration * fs))
    

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
            sd.wait()
            sd.play(recording)
            #print(row for row in recording)

            '''recording = recording.tolist()
            transformed_array = []
            for row in recording:
                transformed_array.append(cooley_tukey(list(row)))
            #ftt_array = np.array(transformed_array).T
            print(fft_array)'''
            # Error with the Cooley-Tukey Algorithm
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

