import tkinter as tk

import DBManager
from MessageScreen import MessageScreen

class CancelationScreen:
    def __init__(self, top, root, username, app_id, previous_window=None):
        self.top = top
        self.root = root
        self.username = username
        self.app_id = app_id
        self.previous_window = previous_window

        self.top.title("CancelationScreen")
        self.top.geometry("350x150")
        self.top.configure(background="#d9d9d9")

        self.label = tk.Label(self.top, text="Are you sure you want to cancel this appointment?", wraplength=300, bg="#d9d9d9", font=("Segoe UI", 10))
        self.label.pack(pady=20)

        self.btn_frame = tk.Frame(self.top, background="#d9d9d9")
        self.btn_frame.pack(pady=10)

        self.confirm_btn = tk.Button(self.btn_frame, text="Yes", command=self.delete_and_update)
        self.confirm_btn.pack(side=tk.LEFT, padx=10)

        self.cancel_btn = tk.Button(self.btn_frame, text="No", command=self.go_back)
        self.cancel_btn.pack(side=tk.LEFT, padx=10)

    def delete_and_update(self):
        db = DBManager.DBManager(database="petato_db")
        db.connect()
        try:
            db.execute_query("DELETE FROM my_appointments WHERE my_app_id = %s AND my_app_user = %s", (self.app_id, self.username))
            db.execute_query("UPDATE appointments SET app_type = 'FREE' WHERE app_id = %s", (self.app_id,))
            db.connection.commit()
            MessageScreen().display("Appointment cancelled successfully.")
            self.top.destroy()
            if self.previous_window:
                self.previous_window.deiconify()
        except Exception as e:
            MessageScreen().display(f"Error cancelling appointment: {e}")
        finally:
            db.close()

    def go_back(self):
        self.top.destroy()
        if self.previous_window:
            self.previous_window.deiconify()
