#import pygame
from os.path import join
import tkinter as tk 
import json

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
        title_label = tk.Label(self.window, text="Arthimetrek", font=("Arial", 30, "bold"), bg='#2C2F33', fg='white')
        title_label.pack(pady=20)


    def run(self):
        self.window.mainloop()



def main():
    GameMenu().run()

if __name__ == "__main__":
    main()


    
