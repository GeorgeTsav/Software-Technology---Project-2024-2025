import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import DBManager
import MessageScreen
import SendMessage

class MessageTextScreen:
    def __init__(self, parent, username, receiver):
        self.username = username
        self.receiver = receiver

        self.top = tk.Toplevel(parent)
        self.top.title("Send Message")
        self.top.geometry("400x300")
        self.top.configure(bg="#f5f5f5")

        tk.Label(self.top, text="Write your message:", font=("Segoe UI", 10), bg="#f5f5f5").pack(pady=(15, 5))

        self.message_entry = tk.Text(self.top, height=8, width=40, font=("Segoe UI", 10))
        self.message_entry.pack(pady=5)

        send_btn = tk.Button(self.top, text="Send", bg="#0078d7", fg="white", font=("Segoe UI", 10),
                             command=self.send_message)
        send_btn.pack(pady=(10, 20))

    def send_message(self):
        content = self.message_entry.get("1.0", tk.END).strip()

        if not content:
            messagebox.showwarning("Empty Message", "Please enter a message.")
            return

        if len(content) > 150:
            MessageScreen.MessageScreen.display("Error", "Message must be 150 characters or fewer.")
            return
        
        if self.username == self.receiver:
             MessageScreen.MessageScreen.display("Error", "You cannot send a message to yourself.")
             return

        try:
            sender = SendMessage.SendMessage(content, self.username, self.receiver)
            sender.sendMsg()
            MessageScreen.MessageScreen.display("Message Sent", "Your message was sent successfully.")
            self.top.destroy()
        except Exception as e:
            MessageScreen.MessageScreen.display("Error", "Failed to send the message.")
