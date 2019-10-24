from db import *
import time
import sys
from login import *
from piedpiper import *

duration = 3

def display_menu():
    print('''
                What would you like to do?

                1) Recognise a song
                2) Fingerprint a song
                3) Search for a song
                4) Quit
            ''')    

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
            recording = record_audio(duration)
            print('Recorded')
            #sd.play(recording)

            recording = recording.tolist()
            amplitude = get_amplitude(recording)    # From the Piedpiper library
            plot_data(amplitude)
            
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

