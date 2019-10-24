from db import *
import time
import sys
from login import *
from piedpiper import *


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

            duration, recording = record_audio()
            #amplitude = get_amplitude(recording)    # From the Piedpiper library
            #plot_data(amplitude)
            #chunk_peaks = get_chunks(amplitude, duration)
            #plot_data(to_list(chunk_peaks))
            #dist = calculate_peak_distance(amplitude, duration)
            confidence = fingerprint(recording, duration)
            
            input('Press any key to continue...')
            clear()

            display_menu()
            value = int(input('Enter your desired operation:- '))
        elif value == 2:

            d = 3
            duration, recording = record_audio(d)
            confidence = fingerprint(recording, duration)
            print(confidence)
            print('Please enter the following data: \n')
            song_name = '"{}"'.format(str(input('Song Name: ')))
            album = '"{}"'.format(str(input('Album: ')))
            artist = '"{}"'.format(str(input('Artist: ')))
            genre = '"{}"'.format(str(input('Genre: ')))
            duration = '"{}"'.format(str(input('Duration: ')))
            donwloads = int(input('Downloads: '))
            rank = int(input('Billboards Rank: '))
            year = int(input('Year: '))
            likes = int(input('Likes(%): '))
            apple_music = '"{}"'.format(str(input('Apple Music Link: ')))
            spotify = '"{}"'.format(str(input('Spotify Link: ')))


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

