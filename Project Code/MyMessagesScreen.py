import tkinter as tk
from tkinter import ttk
import DBManager

class MyMessagesScreen:
    def __init__(self, top, username):
        self.top = top
        self.username = username

        self.top.title(f"Μηνύματα του {username}")
        self.top.geometry("500x600")
        self.top.configure(bg="#f0f0f0")

        
        self.canvas = tk.Canvas(self.top, bg="#f0f0f0")
        self.scrollbar = ttk.Scrollbar(self.top, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#f0f0f0")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.load_messages()

    def load_messages(self):
        db = DBManager.DBManager(host='localhost', user='root', password='', database='petato_db')
        db.connect()

        query = """
            SELECT msg_sender, msg_text, msg_date
            FROM messages
            WHERE msg_receiver = %s
            ORDER BY msg_date DESC
        """

        cursor = db.execute_query(query, (self.username,))
        if cursor is None:
            print("You don't have messages.")
            db.close()
            return

        
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for i, (sender, text, date) in enumerate(cursor.fetchall()):
            
            msg_frame = tk.Frame(self.scrollable_frame, bg="white", bd=1, relief="solid")
            msg_frame.pack(fill="x", padx=5, pady=5)

            sender_label = tk.Label(msg_frame, text=f"Από: {sender}", font=("Segoe UI", 10, "bold"), bg="white")
            sender_label.pack(anchor="w", padx=5, pady=(5,0))

            date_label = tk.Label(msg_frame, text=f"Ημερομηνία: {date}", font=("Segoe UI", 8), fg="gray", bg="white")
            date_label.pack(anchor="w", padx=5)

            text_label = tk.Label(msg_frame, text=text, font=("Segoe UI", 10), bg="white", wraplength=450, justify="left")
            text_label.pack(anchor="w", padx=5, pady=5)

        cursor.close()
        db.close()

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    username = "giwrgos2"
    window = MyMessagesScreen(top, username)
    root.mainloop()
