import tkinter as tk
from CancelationScreen import CancelScreen
from MakeAppointment import MakeAppointmentScreen
from MessageScreen import MessageScreen
from datetime import datetime, timedelta

class ScrSelection:
    def __init__(self, top, root, username, app_id, app_datetime, previous_window=None):
        self.top = top
        self.root = root
        self.username = username
        self.app_id = app_id
        self.app_datetime = app_datetime
        self.previous_window = previous_window

        self.top.title("ScreenSelection")
        self.top.geometry("400x200")
        self.top.configure(background="#d9d9d9")

        self.title_label = tk.Label(self.top, text="Choose an action", font=("Segoe UI", 14, "bold"), bg="#d9d9d9")
        self.title_label.pack(pady=20)

        self.cancel_btn = tk.Button(self.top, text="Cancel", width=25, command=self.goto_cancelation)
        self.cancel_btn.pack(pady=10)

        self.reschedule_btn = tk.Button(self.top, text="Reschedule", width=25, command=self.checkReschedulingDate)
        self.reschedule_btn.pack(pady=10)

    def goto_cancelation(self):
        self.top.withdraw()
        new_top = tk.Toplevel(self.root)
        CancelScreen(new_top, self.root, self.username, self.app_id, previous_window=self.top)

    def checkReschedulingDate(self):
        now = datetime.now()
        if (self.app_datetime - now).days < 2:
            MessageScreen().display("You cannot reschedule less than 2 days before the appointment.")
            self.top.deiconify()
        else:
            import DBManager
            db = DBManager.DBManager(database="petato_db")
            db.connect()
            try:
                db.execute_query("DELETE FROM my_appointments WHERE my_app_id = %s AND my_app_user = %s", (self.app_id, self.username))
                db.execute_query("UPDATE appointments SET app_type = 'FREE' WHERE app_id = %s", (self.app_id,))
                db.connection.commit()
            except Exception as e:
                MessageScreen().display(f"Error during rescheduling: {e}")
                db.close()
                return
            db.close()

            self.top.destroy()
            new_top = tk.Toplevel(self.root)
            MakeAppointmentScreen(new_top, self.root, self.username)
