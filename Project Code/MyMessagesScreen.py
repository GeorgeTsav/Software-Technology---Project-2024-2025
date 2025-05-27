import tkinter as tk
from tkinter import ttk
import DBManager
import MessageTextScreen
from tkinter import messagebox

class MyMessagesScreen:
    def __init__(self, parent, username):
        self.parent = parent
        self.username = username

        self.top = tk.Toplevel(parent)
        self.top.title("My Messages")
        self.top.geometry("600x600")
        self.top.configure(bg="#f0f0f0")

        self.notebook = ttk.Notebook(self.top)
        self.inbox_tab = tk.Frame(self.notebook, bg="#f0f0f0")
        self.sent_tab = tk.Frame(self.notebook, bg="#f0f0f0")
        self.notebook.add(self.inbox_tab, text="Inbox")
        self.notebook.add(self.sent_tab, text="Sent")
        self.notebook.pack(expand=1, fill='both')

        
        self.inbox_canvas = tk.Canvas(self.inbox_tab, bg="#f0f0f0")
        self.inbox_scrollbar = ttk.Scrollbar(self.inbox_tab, orient="vertical", command=self.inbox_canvas.yview)
        self.inbox_frame = tk.Frame(self.inbox_canvas, bg="#f0f0f0")

        self.inbox_frame.bind(
            "<Configure>",
            lambda e: self.inbox_canvas.configure(scrollregion=self.inbox_canvas.bbox("all"))
        )

        self.inbox_canvas.create_window((0, 0), window=self.inbox_frame, anchor="nw")
        self.inbox_canvas.configure(yscrollcommand=self.inbox_scrollbar.set)

        self.inbox_canvas.pack(side="left", fill="both", expand=True)
        self.inbox_scrollbar.pack(side="right", fill="y")

        
        self.sent_canvas = tk.Canvas(self.sent_tab, bg="#f0f0f0")
        self.sent_scrollbar = ttk.Scrollbar(self.sent_tab, orient="vertical", command=self.sent_canvas.yview)
        self.sent_frame = tk.Frame(self.sent_canvas, bg="#f0f0f0")

        self.sent_frame.bind(
            "<Configure>",
            lambda e: self.sent_canvas.configure(scrollregion=self.sent_canvas.bbox("all"))
        )

        self.sent_canvas.create_window((0, 0), window=self.sent_frame, anchor="nw")
        self.sent_canvas.configure(yscrollcommand=self.sent_scrollbar.set)

        self.sent_canvas.pack(side="left", fill="both", expand=True)
        self.sent_scrollbar.pack(side="right", fill="y")

        self.load_messages()

    def load_messages(self):
        db = DBManager.DBManager(host='localhost', user='root', password='', database='petato_db')
        db.connect()

        
        inbox_query = """
            SELECT msg_sender, msg_text, msg_date
            FROM messages
            WHERE msg_receiver = %s
            ORDER BY msg_date DESC
        """
        cursor = db.execute_query(inbox_query, (self.username,))
        self.clear_frame(self.inbox_frame)

        if cursor:
            for sender, text, date in cursor.fetchall():
                self.create_message_box(self.inbox_frame, sender, text, date, reply_to=sender)
            cursor.close()

        
        sent_query = """
            SELECT msg_receiver, msg_text, msg_date
            FROM messages
            WHERE msg_sender = %s
            ORDER BY msg_date DESC
        """
        cursor = db.execute_query(sent_query, (self.username,))
        self.clear_frame(self.sent_frame)

        if cursor:
            for receiver, text, date in cursor.fetchall():
                self.create_message_box(self.sent_frame, receiver, text, date, sent=True)
            cursor.close()

        db.close()

    def create_message_box(self, parent, user, text, date, reply_to=None, sent=False):
        preview_text = (text[:50] + '...') if len(text) > 50 else text

        msg_frame = tk.Frame(parent, bg="white", bd=1, relief="solid")
        msg_frame.pack(fill="x", padx=5, pady=5)

        label_text = f"{'To' if sent else 'From'}: {user}"
        user_label = tk.Label(msg_frame, text=label_text, font=("Segoe UI", 10, "bold"), bg="white")
        user_label.pack(anchor="w", padx=5, pady=(5, 0))

        date_label = tk.Label(msg_frame, text=f"Date: {date}", font=("Segoe UI", 8), fg="gray", bg="white")
        date_label.pack(anchor="w", padx=5)

        preview_label = tk.Label(msg_frame, text=preview_text, font=("Segoe UI", 10), bg="white",
                                 wraplength=520, justify="left", fg="black", cursor="hand2")
        preview_label.pack(anchor="w", padx=5, pady=(5, 5))
        preview_label.bind("<Button-1>", lambda e, full_text=text: self.show_full_message(user, full_text, date))

        if reply_to and not sent:
            reply_btn = tk.Button(msg_frame, text="Reply", font=("Segoe UI", 9), bg="#0078d7", fg="white",
                                  command=lambda: MessageTextScreen.MessageTextScreen(self.top, self.username, reply_to))
            reply_btn.pack(anchor="e", padx=5, pady=(0, 5))

    def show_full_message(self, user, text, date):
        full_msg_window = tk.Toplevel(self.top)
        full_msg_window.title("Full Message")
        full_msg_window.geometry("400x300")
        full_msg_window.configure(bg="#f5f5f5")

        tk.Label(full_msg_window, text=f"From/To: {user}", font=("Segoe UI", 10, "bold"), bg="#f5f5f5").pack(pady=(10, 2))
        tk.Label(full_msg_window, text=f"Date: {date}", font=("Segoe UI", 8), bg="#f5f5f5", fg="gray").pack(pady=(0, 10))

        text_widget = tk.Text(full_msg_window, height=10, wrap="word", font=("Segoe UI", 10))
        text_widget.pack(padx=10, pady=5, fill="both", expand=True)
        text_widget.insert("1.0", text)
        text_widget.config(state="disabled")

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    username = "giwrgos2"
    window = MyMessagesScreen(top, username)
    root.mainloop()