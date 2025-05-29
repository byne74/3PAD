import pygame
from os.path import join
from random import randint, uniform
import tkinter as tk
from tkinter import messagebox
import json
import sys

#------- TKinter GUI Section ------#
class GameMenu():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Arthimetrek")
        self.window.geometry("300x500")
        self.window.configure(bg='#2C2F33')

        #screen_width = self.window.winfo_screenwidth()
        #screen_height = self.window.winfo_screenheight()
        #x = (screen_width/2) - (300/2)
        #y = (screen_height/2) - (400/2)
        #self.window.geometry(f'300x450+{int(x)}+{int(y)}')

        self.users = self.load_users()

        self.create_widgets()

    def load_users(self):
        try:
            with open('users.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        
    def save_users(self):
        with open('users.json', 'w') as f:
            json.dump(self.user, f)

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.window, text="Asteroid Game", font=("Arial", 24, "bold"), bg='#2C2F33', fg='white')
        title_label.pack(pady=20)
            
        # Username Entry
        self.username_var = tk.StringVar()
        username_entry = tk.Entry(self.window, textvariable=self.username_var, width=30)
        username_entry.insert(0, "Username")
        username_entry.bind('<FocusIn>', lambda e: self.on_entry_click(username_entry, "Username"))
        username_entry.bind('<FocusOut>', lambda e: self.on_focus_out(username_entry, "Username"))
        username_entry.pack(pady=10)
            
        # Password Entry
        self.password_var = tk.StringVar()
        password_frame = tk.Frame(self.window, bg='#2C2F33')
        password_frame.pack(pady=10)
            
        self.password_entry = tk.Entry(password_frame, textvariable=self.password_var, width=24)
        self.password_entry.insert(0, "Password")
        self.password_entry.bind('<FocusIn>', lambda e: self.on_entry_click(self.password_entry, "Password"))
        self.password_entry.bind('<FocusOut>', lambda e: self.on_focus_out(self.password_entry, "Password"))
        self.password_entry.pack(side=tk.LEFT)
            
        # Show/Hide Password Button
        self.show_password = tk.BooleanVar(value=False)
        self.show_password_button = tk.Button(password_frame, text="👁", command=self.toggle_password_visibility,
                                                bg='#2C2F33', fg='white', width=3, padx=5)
        self.show_password_button.pack(side=tk.RIGHT)
            
        # Sign Up Button
        signup_button = tk.Button(self.window, text="Sign Up", command=self.sign_up,
                                    bg='#43B581', fg='white', width=25)
        signup_button.pack(pady=10)
            
        # Login Button
        login_button = tk.Button(self.window, text="Login", command=self.login,
                                bg='#7289DA', fg='white', width=25)
        login_button.pack(pady=10)
            
        # Settings Button
        settings_button = tk.Button(self.window, text="Settings", command=self.show_settings,
                                    bg='#727E96', fg='white', width=25)
        settings_button.pack(pady=10)
            
        # Exit Button
        exit_button = tk.Button(self.window, text="Exit", command=self.exit_game,
                                bg='#F04747', fg='white', width=25)
        exit_button.pack(pady=10)     
            
    def sign_up(self):
        username = self.username_var.get()
        password = self.password_var.get()
        
        if username == "Username" or not username:
            messagebox.showerror("Error", "Please enter a valid username!")
            return
            
        if not password:
            messagebox.showerror("Error", "Please enter a password!")
            return
            
        if username in self.users:
            messagebox.showerror("Error", "Username already exists!")
            return
            
        self.users[username] = password
        self.save_users()
        messagebox.showinfo("Success", "Account created successfully!")
        
        # Clear the entry boxes
        self.username_var.set("")
        self.password_var.set("")
        
    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()
        
        if username == "Username" or not username:
            messagebox.showerror("Error", "Please enter a valid username!")
            return
            
        if not password:
            messagebox.showerror("Error", "Please enter a password!")
            return
            
        if username not in self.users:
            messagebox.showerror("Error", "Username does not exist! Please sign up first.")
            return
            
        if self.users[username] != password:
            messagebox.showerror("Error", "Incorrect password!")
            self.password_var.set("")
            return
            
        messagebox.showinfo("Success", "Login successful!")
        self.window.destroy()
        pass # I will add the pygame window in the next version

    def show_settings(self):
        messagebox.showinfo("Settings", "Settings feature coming soon!")
        
    def exit_game(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.window.destroy()
            sys.exit()
            
    def on_entry_click(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            if entry == self.password_entry:
                entry.config(show="*")
                
    def on_focus_out(self, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            if entry == self.password_entry:
                entry.config(show="")    
        

    def toggle_password_visibility(self):
            if self.show_password.get():
                self.password_entry.config(show="*")
                self.show_password.set(False)
            else:
                self.password_entry.config(show="")
                self.show_password.set(True)

    def run(self):
        self.window.mainloop()



def main():
    GameMenu().run()

if __name__ == "__main__":
    main()


    
