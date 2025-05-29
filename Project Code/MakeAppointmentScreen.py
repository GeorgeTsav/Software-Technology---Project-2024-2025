import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime

import DBManager
from ReservationScreen import ReservationScreen
import MainMenuScreen

class MakeAppointmentScreen:
    def __init__(self, top=None, root=None, username="guest"):
        self.top = top
        self.root = root
        self.username = username

        self.top.title("Petato")
        self.top.geometry("600x450+468+138")
        self.top.resizable(1, 1)
        self.top.configure(background="#d9d9d9")

        self.title_label = tk.Label(self.top, text="Make an Appointment", font=("Segoe UI", 14, "bold"))
        self.title_label.pack(pady=15)

        self.cal_frame = tk.Frame(self.top, background="#d9d9d9")
        self.cal_frame.pack(padx=10, pady=10, fill='both', expand=True)

        self.calendar = Calendar(self.cal_frame, selectmode='day', date_pattern='yyyy-mm-dd')
        self.calendar.pack(expand=True, fill='both')
        self.ReturnAppointmentDates()

        self.btn_frame = tk.Frame(self.top, background="#d9d9d9")
        self.btn_frame.pack(pady=10)

        self.select_date_btn = tk.Button(self.btn_frame, text="Select Date", command=self.SelectDate)
        self.select_date_btn.pack(side=tk.LEFT, padx=10)

        self.back_btn = tk.Button(self.btn_frame, text="Back", command=self.goBack)
        self.back_btn.pack(side=tk.LEFT, padx=10)

    def SearchAppointmentDates(self):
        db = DBManager.DBManager(database="petato_db")
        db.connect()
        query = "SELECT DISTINCT DATE(app_date) FROM appointments WHERE app_type = 'FREE'"
        cursor = db.execute_query(query)
        dates = [row[0].strftime("%Y-%m-%d") for row in cursor.fetchall()] if cursor else []
        db.close()
        return dates

    def ReturnAppointmentDates(self):
        dates_with_entries = self.SearchAppointmentDates()
        for date_str in dates_with_entries:
            try:
                self.calendar.calevent_create(datetime.strptime(date_str, "%Y-%m-%d"), 'Entry', 'entry')
            except Exception:
                pass
        self.calendar.tag_config('entry', background='lightgreen', foreground='black')

    def SelectDate(self):
        selected_date = self.calendar.get_date()
        self.top.withdraw()
        new_window = tk.Toplevel(self.root)
        ReservationScreen(new_window, self.root, selected_date, self.username, previous_window=self.top)

    def display(self, previous_window=None):
        if previous_window is not None:
            previous_window.destroy()
        self.top.deiconify()

    def goBack(self):
        new_top = tk.Toplevel(self.root)
        new_top.protocol('WM_DELETE_WINDOW', self.root.destroy)
        MainMenuScreen.MainMenuScreen(new_top, self.root, self.username).display(self.top)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    app = MakeAppointmentScreen(top, root, username="george_tsavos")
    root.mainloop()
