import tkinter as tk
from tkinter import messagebox

class MessageScreen:
    def display(self, message: str):
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        messagebox.showinfo("Message", message)
        root.destroy()

if __name__ == '__main__':
    message_screen = MessageScreen()
    message_screen.display("This is a test message.")