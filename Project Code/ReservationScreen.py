import tkinter as tk
from tkinter import messagebox
from ConfirmationScreen import ConfirmScreen

class ReservScreen:
    def __init__(self, top, root, selected_date, username="guest", previous_window=None):
        self.top = top
        self.root = root
        self.username = username
        self.selected_date = selected_date
        self.previous_window = previous_window

        self.top.title("ReservationScreen")
        self.top.geometry("600x450")
        self.top.configure(background="#d9d9d9")

        self.title_label = tk.Label(self.top, text="Select an Appointment", font=("Segoe UI", 14, "bold"), bg="#d9d9d9")
        self.title_label.pack(pady=15)

        self.appointments_frame = tk.Frame(self.top, background="#d9d9d9")
        self.appointments_frame.pack(fill='both', expand=True, padx=20, pady=10)

        self.back_btn = tk.Button(self.top, text="Back", command=self.go_back)
        self.back_btn.pack(pady=10)

        self.ReturnAppointmentHours(selected_date)

    def SearchAppointmentHours(self, date):
        import DBManager
        db = DBManager.DBManager(database="petato_db")
        db.connect()
        query = """
        SELECT app_id, TIME(app_date), vet.name, vet.last_name
        FROM appointments
        JOIN vet ON appointments.app_vet = vet.vet_id
        WHERE DATE(app_date) = %s AND app_type = 'FREE'
        ORDER BY TIME(app_date)
        """
        cursor = db.execute_query(query, (date,))
        results = cursor.fetchall() if cursor else []
        db.close()
        return results

    def ReturnAppointmentHours(self, date):
        results = self.SearchAppointmentHours(date)

        if results:
            for app_id, time, name, surname in results:
                btn = tk.Button(
                    self.appointments_frame,
                    text=f"{time} - Dr. {name} {surname}",
                    font=("Segoe UI", 10),
                    width=40,
                    command=lambda a=app_id, t=time, vet=f"Dr. {name} {surname}": self.CheckAvailability(a, t, vet)
                )
                btn.pack(pady=4)
        else:
            messagebox.showinfo("Info", "There are no available appointments for this date.")
            self.go_back()

    def CheckAvailability(self, app_id, time, vet):
        self.top.withdraw()
        new_window = tk.Toplevel(self.root)
        ConfirmScreen(new_window, self.root, self.username, app_id, time, vet, previous_window=self.top)

    def go_back(self):
        self.top.destroy()
        if self.previous_window:
            self.previous_window.deiconify()