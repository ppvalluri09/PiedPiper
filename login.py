import sqlite3
import hashlib
import getpass
from db import *
from os import system, name
from time import sleep 

def login_page():
    print('''
            Login to use PiedPiper

            1) Login
            2) Sign Up
        ''')

def welcome_screen():
    print('~~~~~~~~~~~~~~~~ Welcome to PiedPiper ~~~~~~~~~~~~~~~~'.center(24))    

def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 
        

def login_menu():

    login_page()
    value = int(input('Choose you option: '))
    connection = connect_to_database("PiedPiper.db")
    cursor = connection.cursor()
    try:
        if value == 1:
            username = str(input('Username: '))
            password = hashlib.sha256(getpass.getpass().encode()).hexdigest()
            ans = get_data('credentials', 'username', username)
            #ans = get_data('credentials')
            if password == ans[0][1]:
                clear()
                print('Log In successful, redirecting to app')
                sleep(1)
                clear()
                welcome_screen()
                return username
                
        elif value == 2:
            username = str(input('Username: '))
            password = str(hashlib.sha256(getpass.getpass().encode()).hexdigest())
            print('---Confirm Password---')
            while True:
                confirm_password = str(hashlib.sha256(getpass.getpass().encode()).hexdigest())
                print(password)
                print(confirm_password)
                if password != confirm_password:
                    print('Passwords dont match')
                else:
                    break
            if password == confirm_password:
                insert_into('credentials', "{}".format(username), "{}".format(password))
                clear()
                print('Registration Successfull, please log in with your credentials')
                sleep(1)
                clear()
                welcome_screen()
                login_menu()
                

    except Exception as e:
        print('Exception Raised: ' + str(e))
 
        
