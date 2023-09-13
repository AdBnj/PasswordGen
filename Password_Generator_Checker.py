import random
import re
from tkinter import Tk, Button, Text, Label, Entry, Frame, messagebox, WORD, FALSE

CHARACTERS = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!$%^&*()-_=+"

class PasswordApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Password Generator and Checker")
        self.frame = Frame(self.root)

        self.setup_menu()

    def setup_menu(self):
        Label(self.root, text="Please choose one of the options:").pack()
        
        Button(self.frame, text='Password Generator', command=self.generate_password_gui).pack(side='left')
        Button(self.frame, text='Password Checker', command=self.check_password_gui).pack(side='left')
        Button(self.frame, text='Exit the Program', command=self.exit_program).pack(side='left')

        self.frame.pack()

    def generate_password_gui(self):
        self.window = Tk()
        self.window.title("Password Generator")
        self.window.geometry("250x150")
        self.window.resizable(width=FALSE, height=FALSE)
        
        Button(self.window, text="Generate", command=self.generate_password).pack()
        
        self.results = Text(self.window, width=35, height=5, wrap=WORD)
        self.results.pack()

    def check_password_gui(self):
        self.window = Tk()
        self.window.title("Password Checker")
        self.window.geometry("250x150")
        self.window.resizable(width=FALSE, height=FALSE)
        
        Label(self.window, text="Password:").pack()
        
        self.password_guess = Entry(self.window)
        self.password_guess.pack()
        
        Button(self.window, text="Submit", command=self.check_password).pack()
        
        self.result = Text(self.window, width=35, height=5, wrap=WORD)
        self.result.pack()

    def generate_password(self):
        pass_length = random.randint(8, 12)
        while True:
            password = "".join(random.sample(CHARACTERS, pass_length))
            score = self.calculate_score(password)
            if score > 20:
                message = f"Password: {password}"
                self.results.delete(0.0, 'end')
                self.results.insert(0.0, message)
                break

    def check_password(self):
        user_input = self.password_guess.get()
        message = self.check_password_strength(user_input)
        
        self.result.insert('end', message)
        self.result.see('end')

    def check_password_strength(self, user_input):
        score = self.calculate_score(user_input)
        if score > 20:
            message = f"Your Password is Strong! It scored {score} points!"
        else:
            message = f"Your Password is Weak, it only scored {score} points!"
        return message

    def calculate_score(self, password):
        score = len(password)
        if re.search("[A-Z]", password): score += 5
        if re.search("[a-z]", password): score += 5
        if re.search("[0-9]", password): score += 5
        if re.search("[!$%^&*()-_=+]", password): score += 5
        if all(re.search(pattern, password) for pattern in ("[A-Z]", "[a-z]", "[0-9]", "[!$%^&*()-_=+]")):
            score += 10
        if password.isdigit() or password.isalpha(): score -= 5
        return score

    def exit_program(self):
        if messagebox.askquestion('EXIT', 'Are you sure?') == 'yes':
            self.root.destroy()

if __name__ == '__main__':
    app = PasswordApp()
    app.root.mainloop()
