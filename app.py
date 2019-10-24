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

def print_song_data(song_data):
    clear()
    print('PiedPiper results...')
    print('Song Name: ' + song_data[0])
    print('Album: ' + song_data[1])
    print('Artist: ' + song_data[2])
    print('Genre: ' + song_data[3])
    print('Duration: ' + song_data[4])
    print('Downloads: ' + str(song_data[5]))
    print('Billboards Rank: ' + str(song_data[6]))
    print('Year: ' + str(song_data[7]))
    print('Likes(%): ' + str(song_data[8]) + '%')
    print('~~~~~~~~~~~~ Links ~~~~~~~~~~~~')
    print('Apple Music: ' + song_data[9])
    print('Spotify: ' + song_data[10])

def compare_results(confidence):
    song_data = get_data(table_name='fingerprints')
    min_error = 100
    song_id = -9999

    for row in song_data:
        error_pct = (float(row[1]) - float(confidence)) / float(row[1])
        if error_pct * 100 < min_error:
            min_error = error_pct
            song_id = row[0]

    return song_id

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
            song_id = compare_results(confidence)
            song_data = get_data(table_name = 'total', condition = "song_id", song_id)
            print_song_data(song_data)

            input('Press any key to continue...')
            clear()

            display_menu()
            value = int(input('Enter your desired operation:- '))
        elif value == 2:

            d = 30
            duration, recording = record_audio(d)
            confidence = fingerprint(recording, duration)
            print(confidence)
            song_id = -9999
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

            existing = get_data('song_info')
            if len(existing) == 0:
                song_id = 1111
            else:
                song_id = int(existing[len(existing) - 1][0]) + 1

            insert_into('song_info', song_id, song_name, album, artist, genre, duration)
            insert_into('stats', song_id, downloads, rank, year, likes)
            insert_into('links', song_id, apple_music, spotify)
            insert_into('fingerprints', song_id, confidence)

            print('Song added to Database')

            input('Press any key to continue...')
            clear()

            display_menu()
            value = int(input('Enter your desired operation:- '))

        elif value == 3:
            song_name = '"{}"'.format(str(input('Enter the name of the song')))
            song_data = get_data(table_name='total', condition="song_name", song_name)
            print_song_data(song_data)
            
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

