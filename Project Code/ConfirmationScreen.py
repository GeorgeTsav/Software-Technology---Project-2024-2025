import tkinter as tk

import DBManager
from MessageScreen import MessageScreen

class ConfirmationScreen:
    def __init__(self, top, root, username, app_id, time, vet, previous_window=None):
        self.top = top
        self.root = root
        self.username = username
        self.app_id = app_id
        self.time = time
        self.vet = vet
        self.previous_window = previous_window

        self.top.title("Confirmation")
        self.top.geometry("600x450")
        self.top.configure(background="#d9d9d9")

        self.message_label = tk.Label(
            self.top,
            text=f"Do you want to confirm your appointment at {time} with {vet}?",
            font=("Segoe UI", 12),
            bg="#d9d9d9"
        )
        self.message_label.pack(pady=40)

        self.confirm_btn = tk.Button(self.top, text="Confirm", command=self.InsertAppointment)
        self.confirm_btn.pack(pady=5)

        self.back_btn = tk.Button(self.top, text="Cancel", command=self.go_back)
        self.back_btn.pack()

    def InsertAppointment(self):
        db = DBManager.DBManager(database="petato_db")
        db.connect()
        try:
            update_query = "UPDATE appointments SET app_type = 'RESERVED' WHERE app_id = %s"
            db.execute_query(update_query, (self.app_id,))

            insert_query = """
            INSERT INTO my_appointments (my_app_user, my_app_id, my_app_date)
            VALUES (%s, %s, NOW())
            """
            db.execute_query(insert_query, (self.username, self.app_id))

            db.connection.commit()
            MessageScreen().display(f"Appointment at {self.time} with {self.vet} successfully reserved!")
            self.go_home()
        except Exception as e:
            MessageScreen().display(f"Something went wrong:\n{e}")
        finally:
            db.close()

    def go_back(self):
        self.top.destroy()
        if self.previous_window:
            self.previous_window.deiconify()

    def go_home(self):
        self.top.destroy()
        self.previous_window.deiconify()