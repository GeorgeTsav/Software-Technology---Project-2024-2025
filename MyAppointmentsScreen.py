import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import DBManager
from MakeAppointment import MakeAppointmentScreen
from MessageScreen import MessageScreen  

class MyAppointmentsScreen:
    def __init__(self, top=None, root=None, username="guest"):
        self.top = top
        self.root = root
        self.username = username

        self.top.title("My Appointments")
        self.top.geometry("700x500")
        self.top.configure(background="#d9d9d9")

        self.title_label = tk.Label(self.top, text="My Appointments", font=("Segoe UI", 14, "bold"), bg="#d9d9d9")
        self.title_label.pack(pady=15)

        self.results_frame = tk.Frame(self.top, background="#d9d9d9")
        self.results_frame.pack(pady=10, fill='both', expand=True)

        self.load_appointments()

    def load_appointments(self):
        db = DBManager.DBManager(database="petato_db")
        db.connect()
        query = """
            SELECT a.app_id, a.app_date, v.name, v.last_name
            FROM appointments a
            JOIN my_appointments m ON m.my_app_id = a.app_id
            JOIN vet v ON a.app_vet = v.vet_id
            WHERE m.my_app_user = %s
            ORDER BY a.app_date
        """
        cursor = db.execute_query(query, (self.username,))
        results = cursor.fetchall() if cursor else []
        db.close()

        if results:
            for app_id, app_date, vet_name, vet_surname in results:
                app_datetime = datetime.strptime(str(app_date), "%Y-%m-%d %H:%M:%S")
                days_left = (app_datetime - datetime.now()).days

                frame = tk.Frame(self.results_frame, bg="#f0f0f0", pady=5)
                frame.pack(fill='x', padx=10, pady=5)

                label = tk.Label(
                    frame,
                    text=f"{app_datetime.strftime('%Y-%m-%d %H:%M')} - Dr. {vet_name} {vet_surname}",
                    font=("Segoe UI", 10),
                    bg="#f0f0f0"
                )
                label.pack(side=tk.LEFT, padx=5)

                if days_left == 0 :
                    cancel_btn = tk.Button(
                        frame,
                        text="Cancel",
                        command=lambda: MessageScreen().display("Δεν μπορείτε να αλλάξετε αυτό το ραντεβού λιγότερο από 2 ημέρες πριν.")
                    )
                    resched_btn = tk.Button(
                        frame,
                        text="Reschedule",
                        command=lambda: MessageScreen().display("Δεν μπορείτε να αλλάξετε αυτό το ραντεβού λιγότερο από 2 ημέρες πριν.")
                    )
                else:
                    cancel_btn = tk.Button(
                        frame,
                        text="Cancel",
                        command=lambda aid=app_id: self.cancel_appointment(aid)
                    )
                    resched_btn = tk.Button(
                        frame,
                        text="Reschedule",
                        command=lambda aid=app_id: self.reschedule_appointment(aid)
                    )

                resched_btn.pack(side=tk.RIGHT, padx=5)
                cancel_btn.pack(side=tk.RIGHT, padx=5)
        else:
            tk.Label(self.results_frame, text="Δεν υπάρχουν ραντεβού.", bg="#d9d9d9").pack()

    def cancel_appointment(self, app_id):
        confirm = messagebox.askyesno("Cancel Appointment", "Are you sure you want to cancel this appointment?")
        if not confirm:
            return

        db = DBManager.DBManager(database="petato_db")
        db.connect()
        try:
            db.execute_query("DELETE FROM my_appointments WHERE my_app_id = %s AND my_app_user = %s", (app_id, self.username))
            db.execute_query("UPDATE appointments SET app_type = 'FREE' WHERE app_id = %s", (app_id,))
            db.connection.commit()
            messagebox.showinfo("Success", "Appointment cancelled.")
            self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Could not cancel appointment:\n{e}")
        finally:
            db.close()

    def reschedule_appointment(self, app_id):
        confirm = messagebox.askyesno("Reschedule Appointment", "Do you want to reschedule this appointment?")
        if not confirm:
            return

        db = DBManager.DBManager(database="petato_db")
        db.connect()
        try:
            db.execute_query("DELETE FROM my_appointments WHERE my_app_id = %s AND my_app_user = %s", (app_id, self.username))
            db.execute_query("UPDATE appointments SET app_type = 'FREE' WHERE app_id = %s", (app_id,))
            db.connection.commit()
        except Exception as e:
            messagebox.showerror("Error", f"Error during rescheduling:\n{e}")
            db.close()
            return
        db.close()

        self.top.destroy()
        new_top = tk.Toplevel(self.root)
        new_top.protocol("WM_DELETE_WINDOW", self.root.destroy)
        MakeAppointmentScreen(new_top, self.root, self.username)

    def refresh(self):
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        self.load_appointments()

    def display(self, previous_window=None):
        if previous_window:
            previous_window.destroy()
        self.top.deiconify()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    top = tk.Toplevel(root)
    app = MyAppointmentsScreen(top, root, username="george_tsavos")
    root.mainloop()
