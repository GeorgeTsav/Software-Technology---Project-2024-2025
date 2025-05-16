import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime

import DBManager
import PersonalDiaryTextScreen as pdts

class PersonalDiaryScreen:
    def __init__(self, top=None, root=None, username=None):
        self.top = top
        self.root = root
        self.username = username
        self.top.title("Petato")

        # Configure grid for scaling
        self.top.rowconfigure(1, weight=1)
        self.top.columnconfigure(0, weight=1)

        # Label above the calendar
        self.title_label = tk.Label(self.top, text="My Personal Diary", font=("Segoe UI", 14, "bold"))
        self.title_label.grid(row=0, column=0, pady=(15, 5), sticky="n")

        # Calendar widget (in a frame for scaling)
        cal_frame = tk.Frame(self.top)
        cal_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        cal_frame.rowconfigure(0, weight=1)
        cal_frame.columnconfigure(0, weight=1)

        self.calendar = Calendar(cal_frame, selectmode='day', date_pattern='yyyy-mm-dd')
        self.calendar.grid(row=0, column=0, sticky="nsew")

        # Highlight days with entries
        self.search_entries()
        
        btn_frame = tk.Frame(self.top)
        btn_frame.grid(row=2, column=0, pady=(0, 10))

        self.open_btn = tk.Button(btn_frame, text="Open Entry", command=self.open_text_screen)
        self.open_btn.pack(side=tk.LEFT, padx=(0, 10))
        self.open_btn.configure(activebackground="#0080ff")
        self.open_btn.configure(activeforeground="black")
        self.open_btn.configure(background="#d9d9d9")
        self.open_btn.configure(disabledforeground="#a3a3a3")
        self.open_btn.configure(font="-family {Segoe UI} -size 9")
        self.open_btn.configure(foreground="#000000")
        self.open_btn.configure(highlightbackground="#d9d9d9")
        self.open_btn.configure(highlightcolor="#000000")

        self.back_btn = tk.Button(btn_frame, text="Back", command=self.go_back)
        self.back_btn.pack(side=tk.LEFT)
        self.back_btn.configure(activebackground="#0080ff")
        self.back_btn.configure(activeforeground="black")
        self.back_btn.configure(background="#d9d9d9")
        self.back_btn.configure(disabledforeground="#a3a3a3")
        self.back_btn.configure(font="-family {Segoe UI} -size 9")
        self.back_btn.configure(foreground="#000000")
        self.back_btn.configure(highlightbackground="#d9d9d9")
        self.back_btn.configure(highlightcolor="#000000")

    def search_entries(self):
        db = DBManager.DBManager(database="petato_db")
        db.connect()
        db_cursor = db.execute_query("SELECT per_diary_date FROM personal_diary WHERE per_diary_user = %s", (self.username,))
        dates_with_entries = set()

        # Αναζήτηση ημερομηνιών με καταχωρήσεις
        if db_cursor:
            for row in db_cursor.fetchall():
                dates_with_entries.add(str(row[0]))
            db_cursor.close()
        db.close()
        
        # Μαρκάρισμα ημερομηνιών με καταχωρήσεις με χρώμα
        for date_str in dates_with_entries:
            try:
                self.calendar.calevent_create(datetime.strptime(date_str, "%Y-%m-%d"), 'Entry', 'entry')
            except Exception:
                pass
        self.calendar.tag_config('entry', background='lightgreen', foreground='black')

    def open_text_screen(self):
        date = self.calendar.get_date()
        pdts.PersonalDiaryTextScreen(tk.Toplevel(self.root), self.root, self.username, date)

    def go_back(self):
        pass

    #Σβήνει το προηγούμενο παράθυρο και εμφανίζει το νέο
    def display(self, previous_window=None):
        if previous_window is not None:
            previous_window.destroy()
        self.top.deiconify()
        
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    top = tk.Toplevel(root)
    username = "george_tsavos"
    window = PersonalDiaryScreen(top, root, username)
    root.mainloop()