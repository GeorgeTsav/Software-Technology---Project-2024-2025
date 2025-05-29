import tkinter as tk
from datetime import datetime
import DBManager
from ScreenSelection import ScrSelection

class MyAppointmentsScreen:
    def __init__(self, top=None, root=None, username="guest"):
        self.top = top
        self.root = root
        self.username = username

        self.top.title("MyAppointmentsScreen")
        self.top.geometry("700x500")
        self.top.configure(background="#d9d9d9")

        self.title_label = tk.Label(self.top, text="My Appointments", font=("Segoe UI", 14, "bold"), bg="#d9d9d9")
        self.title_label.pack(pady=15)

        self.results_frame = tk.Frame(self.top, background="#d9d9d9")
        self.results_frame.pack(pady=10, fill='both', expand=True)

        self.ReturnAppointments()

    def SearchAppointments(self):
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
        return results

    def ReturnAppointments(self):
        results = self.SearchAppointments()

        if results:
            for app_id, app_date, vet_name, vet_surname in results:
                app_datetime = datetime.strptime(str(app_date), "%Y-%m-%d %H:%M:%S")

                frame = tk.Frame(self.results_frame, bg="#f0f0f0", pady=5)
                frame.pack(fill='x', padx=10, pady=5)

                label = tk.Label(
                    frame,
                    text=f"{app_datetime.strftime('%Y-%m-%d %H:%M')} - Dr. {vet_name} {vet_surname}",
                    font=("Segoe UI", 10),
                    bg="#f0f0f0"
                )
                label.pack(side=tk.LEFT, padx=5)

                edit_btn = tk.Button(
                    frame,
                    text="Select",
                    command=lambda aid=app_id, dt=app_datetime: self.create_selection_screen(aid, dt)
                )
                edit_btn.pack(side=tk.RIGHT, padx=10)
        else:
            tk.Label(self.results_frame, text="There are no appointments.", bg="#d9d9d9").pack()

    def create_selection_screen(self, app_id, app_datetime):
        self.top.withdraw()
        new_window = tk.Toplevel(self.root)
        ScrSelection(new_window, self.root, self.username, app_id, app_datetime, previous_window=self.top)

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
