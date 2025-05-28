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
                             command=self.forwardMessage)
        send_btn.pack(pady=(10, 20))

    def forwardMessage (self):
        content = self.message_entry.get("1.0", tk.END).strip()

        if not content:
            MessageScreen.MessageScreen.display("Message must not be empty.")
            return

        if len(content) > 150:
            MessageScreen.MessageScreen.display("Message must be 150 characters or fewer.")
            return
        
        if self.username == self.receiver:
            MessageScreen.MessageScreen.display("You cannot send a message to yourself.")
            return
        
        if self.receiver == "System":
            MessageScreen.MessageScreen.display("Error", "You cannot send a message to the System.")
            return

        try:
            sender = SendMessage.SendMessage(content, self.receiver, self.username)
            sender.sendMsg()
            MessageScreen.MessageScreen.display("Message Sent", "Your message was sent successfully.")
            self.top.destroy()
        except Exception as e:
            MessageScreen.MessageScreen.display("Failed to send the message.")
