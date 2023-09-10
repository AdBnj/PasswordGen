
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
            passw =  "".join(random.sample(characters,passlength))
            score = len(passw)
            if len(passw) < 8:
                window2.destroy()
            if len(passw) > 24:
                window2.destroy()
            if re.search("[A-Z]", passw):
                score += 5
            if re.search("[a-z]", passw):
                score += 5
            if re.search("[0-9]", passw):
                score += 5
            if re.search("[|!|$|%|^|&|*|(|)|-|_|=|+|]", passw):
                score += 5
            if re.search("[a-z]", passw) and re.search("[A-Z]", passw) and re.search("[0-9]", passw)and re.search("[|!|$|%|^|&|*|(|)|-|_|=|+|]", passw):
                score += 10
            if passw.isdigit():
                score+=-5
            if passw.isalpha():
                score+=-5
            if score > 20:
                message = "Passowrd:  " + passw

            # Various conditions to check the strength of the generated password and calculate a score 
            # (Checking the length, presence of uppercase letters, lowercase letters, digits, and special characters)
            # ... (Your existing conditions and score calculations here) ...
            
            # Display the generated password and its score in the GUI
            results.delete(0.0, END)
            results.insert(0.0, message)
            if score > 20:
                break

# GUI setup for the password generator
    window2 = Tk()
    window2.resizable(width=FALSE, height=FALSE)
    window2.title("Password Generator")
    window2.geometry("250x150")
#Generate Button
    bttnGenerate = Button(window2, text="Generate", command=GeneratePassword)
    bttnGenerate.pack()
#Creating Text Grid
    results = Text(window2, width = 35, height = 5, wrap = WORD)
    results.pack()
#Main Starter
    window2.mainloop()

 # Function to check the strength of a user-input password
def Check():
    
    # Nested function to check the strength of a user-input password and calculate its score
    def checkPassword():
        Upassw = password_guess.get()
        Uscore = len(Upassw)
        import re
        if len(Upassw) < 8:
            dialog_title = 'Returning to Menu.'
            dialog_text = 'Error 1: Password too small.'
            answer = messagebox.showinfo(dialog_title, dialog_text)
            window.destroy()
        if len(Upassw) > 24:
            Uscore +=-1000
            dialog_title = 'Returning to Menu.'
            dialog_text = 'Error 2: Password too large.'
            answer = messagebox.showinfo(dialog_title, dialog_text)
            window.destroy()
        if re.search("[A-Z]", Upassw):
            Uscore += 5
        if re.search("[a-z]", Upassw):
            Uscore += 5
        if re.search("[0-9]", Upassw):
            Uscore += 5
        if re.search("[|!|$|%|^|&|*|(|)|-|_|=|+|]", Upassw):
            Uscore += 5
        if re.search("[a-z]", Upassw) and re.search("[A-Z]", Upassw) and re.search("[0-9]", Upassw)and re.search("[|!|$|%|^|&|*|(|)|-|_|=|+|]", Upassw):
            Uscore += 10
        if Upassw.isdigit():
            Uscore+=-5
        if Upassw.isalpha():
            Uscore+=-5
        if Uscore > 20:
            write = "Your Password is Strong! It scored",Uscore,"points!"
        if Uscore > 0 and Uscore < 20:
            write = "Your Password is Weak, it onlyscored",Uscore,"points!"
        if Uscore <= 0:
            write = "Your Password is Weak, it onlyscored",Uscore,"points!"
        result.insert(tk.END, write)
        result.see(tk.END)
        
#Gui set up for the Password Checker
    window = Tk()
    window.resizable(width=FALSE, height=FALSE)
    window.title("Password Checker")
    window.geometry("250x150")

#Creating the password entry box
    password_text = Label(window, text="Password:")
    password_guess = Entry(window)

#Insert Password
    Submit = Button(window, text="Submit", command=checkPassword)
    password_text.pack()
    password_guess.pack()
    Submit.pack()

#Creating Text Grid
    result = Text(window, width = 35, height = 5, wrap = WORD)
    result.pack()
    
#Main Starter
    window.mainloop()# Class to create the main menu of the application
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
