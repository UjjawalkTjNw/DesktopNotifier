import tkinter as tk
from tkinter import messagebox

def show_notification(title, message, duration=5000):
    root = tk.Tk()
    root.withdraw()  # This will prevent from creating multiple instance of window

    def close_notification():
        root.destroy()

    #remove messagebox.showinfo(title,message)
    #better make a new child window as below:
    #create a new window that is child of root
    new_window = tk.Toplevel(root)
    #set the title of new window created
    new_window.title(title)
    
    #Add label to show the message
    label = tk.Label(new_window, text = message)
    label.pack(padx=10, pady=10)
    
    
    
    # Close the notification window after the duration
    root.after(duration, close_notification)

    root.mainloop()

if __name__ == "__main__":
    show_notification("Hello", "This is a notification", duration=5000)
