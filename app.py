from db import *
from spectrogram import *
import sounddevice as sd
import time
import sys

fs = 44100
sd.default.samplerate = fs
sd.default.channels = 2
duration = 10


def welcome_screen():
    print('''~~~~~~~~~~~~~~~~ Welcome to PiedPiper ~~~~~~~~~~~~~~~~''')    

def display_menu():
    print('''
                What would you like to do?

                1) Recognise a song
                2) Fingerprint a song
                3) Search for a song
                4) Quit
            ''')

welcome_screen()
display_menu()
value = int(input('Enter your desired operation:- '))

try:
    while value is not 4:

        if value == 1:
            print('Audio will be recorded in ')
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')

        
            print('Recording Started')
            # recording = sd.rec(int(duration * fs))
            # sd.play(recording)
            # print(recording)

        elif value == 2:
            print('Fingerprint a song')

        elif value == 3:
            print('Search for the song')

        elif value == 4:
            print('Thank you for using PiedPiper')
            sys.exit()

    display_menu()
    value = int(input('Enter your desired operation:- '))
    
except Exception as e:
    print('Exception Raised: ' + str(e))

        
