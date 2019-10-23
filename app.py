from db import *
from spectrogram import *
import sounddevice as sd
import time
import sys
from login import *
import tkinter as tk

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
            duration = 10
            #recording = record_audio()
            recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
            sd.stop()
            sd.play(recording)
            print(recording)

            display_menu()
            value = int(input('Enter your desired operation:- '))
        elif value == 2:
            print('Fingerprint a song')

            display_menu()
            value = int(input('Enter your desired operation:- '))

        elif value == 3:
            print('Search for the song')

            display_menu()
            value = int(input('Enter your desired operation:- '))
        elif value == 4:
            print('Thank you for using PiedPiper ' + username)
            sys.exit()
    
except Exception as e:
    print('Exception Raised: ' + str(e))

