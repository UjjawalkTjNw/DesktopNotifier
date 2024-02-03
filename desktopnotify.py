import tkinter as tk
from tkinter import messagebox

def show_notification(title, message):
    # create a new window for notification
    root= tk.Tk()
    #immmediately hide the window after notification
    root.withdraw()
    
    messagebox.showinfo(title, message)
    
if __name__ == "__main__":
    show_notification("Hello", "This is notification")
        
        