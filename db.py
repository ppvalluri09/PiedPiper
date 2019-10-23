import sqlite3


# Function to connect to a required Database
def connect_to_database(database):
    connection = sqlite3.connect(str(database))
    print('Connection Established')
    return connection


def create_table(table_name):

    # Establishing Connection to Database
    connection = connect_to_database("PiedPiper.db")
    cursor = connection.cursor()
    
    commands = ['create table song_info(song_id number(4) primary key, song_name varchar not null, album varchar, artist varchar, genre varchar, duration varchar(4));',
                'create table stats(song_id number(4), downloads number, billboards_rank number, year number(4) not null, likes number(3), constraint fk_stats foreign key(song_id) references song_info(song_id));',
                'create table links(song_id number(4), apple_music varchar, spotify varchar, constraint fk_links foreign key(song_id) references song_info(song_id));',
                'create table credentials(username varchar primary key, password varchar(64) not null);']

    try:
        if table_name == 'song_info':
            cursor.execute(commands[0])
        elif table_name == 'stats':
            cursor.execute(commands[1])
        elif table_name == 'links':
            cursor.execute(commands[2])
        elif table_name == 'credentials':
            cursor.execute(commands[3])

        print('Table {} created'.format(table_name))

    except Exception as e:
        print('Exeption Raised: ' + str(e))

    connection.commit()
    connection.close()

def insert_into(table_name, *args):

    # Establishing Connection to Database
    connection = connect_to_database("PiedPiper.db")
    cursor = connection.cursor()

    try:
        command = 'insert into {} values{};'.format(table_name, args)
        cursor.execute(command)
        print('Data Inserted')
    except Exception as e:
        print('Exception raised: ' + str(e))

    connection.commit()
    connection.close()

def get_data(table_name = 'total', condition = 'None', condition_value = 'None'):

    # Establishing Connection to Database
    connection = connect_to_database("PiedPiper.db")
    cursor = connection.cursor()

    if table_name == 'total':

        song_data_command = 'select song_info.song_name, song_info.album, song_info.artist, song_info.genre, song_info.duration, stats.downloads, stats.billboards_rank, stats.year, stats.likes from song_info inner join stats on song_info.song_id = stats.song_id where song_info.song_id = ' + str(condition_value)
        link_data_command = 'select links.apple_music, links.spotify from song_info inner join links on song_info.song_id = links.song_id where song_info.song_id = ' + str(condition_value)

        try:
            cursor.execute(song_data_command)
            song_data = cursor.fetchall()
            cursor.execute(link_data_command)
            link_data = cursor.fetchall()

            return (song_data, link_data)

        except Exception as e:
            print('Exception Raised: ' + str(e))

    elif table_name != 'total' and condition != 'None':
        try:
            command = 'select * from {} where {} = "{}"'.format(table_name, condition, condition_value)
            cursor.execute(command)
            ans = cursor.fetchall()
            return ans
        except Exception as e:
            print('Exception Raised: ' + str(e))

    else:
        try:
            command = 'select * from {}'.format(table_name)
            cursor.execute(command)
            ans = cursor.fetchall()
            return ans
        except Exception as e:
            print('Exception Raised: ' + str(e))

def modify_data(table_name, column_name, value, condition, condition_value):

    #Establishing Connection to Database
    connection = connect_to_database("PiedPiper.db")
    cursor = connection.cursor()

    try:
        command = 'update {} set {} = {} where {} = "{}"'.format(table_name, column_name, value, condition, condition_value)
        cursor.execute(command)
        print('Data Updated')
    except Exception as e:
        print('Exception Raised: ' + str(e))
    
