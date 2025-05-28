import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox
from datetime import datetime
import DBManager
from MessageScreen import MessageScreen

class MakeAppointmentScreen:
    def __init__(self, top=None, root=None, username="guest"):
        self.top = top
        self.root = root
        self.username = username

        self.top.title("Petato")
        self.top.geometry("600x450+468+138")
        self.top.resizable(1, 1)
        self.top.configure(background="#d9d9d9")

        # Title
        self.title_label = tk.Label(self.top, text="Make an Appointment", font=("Segoe UI", 14, "bold"))
        self.title_label.pack(pady=15)

        # Calendar
        self.cal_frame = tk.Frame(self.top, background="#d9d9d9")
        self.cal_frame.pack(padx=10, pady=10, fill='both', expand=True)

        self.calendar = Calendar(self.cal_frame, selectmode='day', date_pattern='yyyy-mm-dd')
        self.calendar.pack(expand=True, fill='both')
        self.mark_dates_with_entries()

        # Buttons
        self.btn_frame = tk.Frame(self.top, background="#d9d9d9")
        self.btn_frame.pack(pady=10)

        self.select_date_btn = tk.Button(self.btn_frame, text="Select Date", command=self.select_date)
        self.select_date_btn.pack(side=tk.LEFT, padx=10)

        self.back_btn = tk.Button(self.btn_frame, text="Back", command=self.go_back)
        self.back_btn.pack(side=tk.LEFT, padx=10)
        self.back_btn.pack_forget()

        # Results (appointments)
        self.results_frame = tk.Frame(self.top, background="#d9d9d9")
        self.results_frame.pack(pady=10)

    def mark_dates_with_entries(self):
        db = DBManager.DBManager(database="petato_db")
        db.connect()
        query = "SELECT DISTINCT DATE(app_date) FROM appointments WHERE app_type = 'FREE'"
        cursor = db.execute_query(query)
        dates_with_entries = [row[0].strftime("%Y-%m-%d") for row in cursor.fetchall()] if cursor else []
        db.close()

        for date_str in dates_with_entries:
            try:
                self.calendar.calevent_create(datetime.strptime(date_str, "%Y-%m-%d"), 'Entry', 'entry')
            except Exception:
                pass
        self.calendar.tag_config('entry', background='lightgreen', foreground='black')

    def select_date(self):
        selected_date = self.calendar.get_date()

        # UI adjustments
        self.cal_frame.pack_forget()
        self.select_date_btn.pack_forget()
        self.back_btn.pack(side=tk.LEFT, padx=10)

        for widget in self.results_frame.winfo_children():
            widget.destroy()

        # Query DB
        db = DBManager.DBManager(database="petato_db")
        db.connect()
        query = """
        SELECT app_id, TIME(app_date), vet.name, vet.last_name
        FROM appointments
        JOIN vet ON appointments.app_vet = vet.vet_id
        WHERE DATE(app_date) = %s AND app_type = 'FREE'
        ORDER BY TIME(app_date)
        """
        cursor = db.execute_query(query, (selected_date,))
        results = cursor.fetchall() if cursor else []
        db.close()

        if results:
            for app_id, time, name, surname in results:
                btn = tk.Button(
                    self.results_frame,
                    text=f"{time} - Dr. {name} {surname}",
                    font=("Segoe UI", 10),
                    width=40,
                    command=lambda a=app_id, t=time: self.go_to_confirm_popup(a, t)
                )
                btn.pack(pady=2)
        else:
            MessageScreen().display("There are no available appointments for this date.")
            self.go_back()

    def go_back(self):
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        self.cal_frame.pack(padx=10, pady=10, fill='both', expand=True)
        self.select_date_btn.pack(side=tk.LEFT, padx=10)
        self.back_btn.pack_forget()

    def go_to_confirm_popup(self, app_id, time):
        confirm = messagebox.askyesno("Confirm Appointment", f"Do you want to book this appointment at {time};")
        if confirm:
            db = DBManager.DBManager(database="petato_db")
            db.connect()
            try:
                # Update appointment status
                update_query = "UPDATE appointments SET app_type = 'RESERVED' WHERE app_id = %s"
                db.execute_query(update_query, (app_id,))

                # Insert into my_appointments
                insert_query = """
                INSERT INTO my_appointments (my_app_user, my_app_id, my_app_date)
                VALUES (%s, %s, NOW())
                """
                db.execute_query(insert_query, (self.username, app_id))

                db.connection.commit()
                messagebox.showinfo("Success", "Appointment successfully reserved!")
                self.go_back()
            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong:\n{e}")
            finally:
                db.close()

    def display(self, previous_window=None):
        if previous_window is not None:
            previous_window.destroy()
        self.top.deiconify()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    app = MakeAppointmentScreen(top, root, username="george_tsavos")
    root.mainloop()
