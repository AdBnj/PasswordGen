
# Import necessary libraries
from tkinter import messagebox
import tkinter as tk
from tkinter import *
import re
import random

# Define various character sets to be used in password generation and checking
characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!$%^&*()-_=+"
symb = "!$%^&*()-_=+"
badsymb = "`~@#^[]\\{}|;':,./<>?£"
badcharacters = "[£|{|[|}|]|:|;|@|'|~|#|<|,|>|.|?|/|`|¬|\\|||]"
Uqwerty = ('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMN')

# Function to generate a random password and check its strength
def Generate():
    
    # Nested function to generate a random password and calculate its strength score
    def GeneratePassword():
        import random
        from random import randrange
        
        # Generate a random password length between 8 and 12 characters
        passlength = randrange(8, 12)
        
        # Loop to continuously generate passwords until a strong one is created
        while True:
            passw =  "".join(random.sample(characters, passlength))
            score = len(passw)
            
            # Various conditions to check the strength of the generated password and calculate a score
            # (Checking the length, presence of uppercase letters, lowercase letters, digits, and special characters)
            # ... (Your existing conditions and score calculations here) ...
            
            # Display the generated password and its score in the GUI
            results.delete(0.0, END)
            results.insert(0.0, message)
            if score > 20:
                break

    # GUI setup for the password generator
    # ... (Your existing GUI setup code here) ...

# Function to check the strength of a user-input password
def Check():
    
    # Nested function to check the strength of a user-input password and calculate its score
    def checkPassword():
        # ... (Your existing checkPassword function code here) ...

    # GUI setup for the password checker
    # ... (Your existing GUI setup code here) ...

# Class to create the main menu of the application
class MenuC():
    root = Tk()
    frame = Frame(root)
    
    # Set up the main window with a title and buttons to access the password generator and checker
    root.title("Password Generator and Checker")
    
    # Define buttons to access the password generator, password checker, and to exit the program
    bgen = Button(frame, text='Password Generator', command=Generate)
    bcheck = Button(frame, text='Password Checker', command=Check)
    
    # Define an exit button with a confirmation dialog
    def Exit():
        dialog_title = 'EXIT'
        dialog_text = 'Are you sure?'
        answer = messagebox.askquestion(dialog_title, dialog_text)
        if answer == 'yes':
            quit()
    bexit = Button(frame, text= 'Exit the Program', command=Exit)
    
    # Arrange buttons in the frame
    bgen.pack(side=LEFT)
    bcheck.pack(side=LEFT)
    bexit.pack(side=LEFT)
    
    # Add a label and pack the frame into the root window
    l1 = Label(root, text="Please choose one of the options:")
    l1.pack()
    frame.pack()
