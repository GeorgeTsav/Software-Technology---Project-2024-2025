import sys
import tkinter as tk
from tkinter.constants import *
import tkinter.ttk as ttk
import os.path
from tkcalendar import DateEntry

import DBManager
import MessageScreen
import MainMenuScreen

debug = True
_location = os.path.dirname(__file__)

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black'
_tabfg2 = 'white'
_bgmode = 'light'
_tabbg1 = '#d9d9d9'
_tabbg2 = 'gray40'


class MakeAnnouncementScreen:
    def __init__(self, top=None, root=None, username=None):
        self.username = username
        self.root = root
        self.top = top

        self.top.geometry("600x450+468+138")
        self.top.minsize(120, 1)
        self.top.maxsize(1540, 845)
        self.top.resizable(1, 1)
        self.top.title("Petato")
        self.top.configure(background="#d9d9d9")

        self.title_label = tk.Label(top, text="Make Announcement", font=("Segoe UI", 20, "bold"), bg=_bgcolor, fg="black")
        self.title_label.pack(side="top", pady=10)

        self.announcement_type = tk.StringVar()
        self.pet_type = tk.StringVar()

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.133, rely=0.178, relheight=0.711, relwidth=0.758)
        self.Frame1.configure(relief='raised', borderwidth="2", background="#ffffff")

        # Τίτλος αγγελίας
        self.Label1_1 = tk.Label(self.Frame1, text='Title', background="#d9d9d9")
        self.Label1_1.place(relx=0.022, rely=0.172, height=25, width=80)
        self.Text1 = tk.Text(self.Frame1, wrap="word")
        self.Text1.place(relx=0.22, rely=0.172, relheight=0.078, relwidth=0.295)

        # Τύπος αγγελίας
        self.Label1 = tk.Label(self.Frame1, text='Type of Announcement', background="#d9d9d9")
        self.Label1.place(relx=0.022, rely=0.063, height=25, width=150)
        self.TCombobox1 = ttk.Combobox(self.Frame1, textvariable=self.announcement_type)
        self.TCombobox1.place(relx=0.374, rely=0.063, relheight=0.078, relwidth=0.301)
        self.TCombobox1['values'] = ['ADOPTION', 'HOST']
        self.TCombobox1.bind("<<ComboboxSelected>>", self.on_type_change)

        # Τύπος ζώου
        self.Label1_1_1 = tk.Label(self.Frame1, text='Pet', background="#d9d9d9")
        self.Label1_1_1.place(relx=0.022, rely=0.281, height=25, width=50)
        self.TCombobox1_1 = ttk.Combobox(self.Frame1, textvariable=self.pet_type)
        self.TCombobox1_1.place(relx=0.149, rely=0.281, relheight=0.078, relwidth=0.22)
        self.TCombobox1_1['values'] = ['DOG', 'CAT']

        # Ημερομηνίες hosting
        self.Label1_2 = tk.Label(self.Frame1, text='Host Start Date', background="#d9d9d9")
        self.Label1_2.place(relx=0.022, rely=0.391, height=25, width=100)
        self.Entry1 = DateEntry(self.Frame1, date_pattern='dd/mm/yyyy', state='disabled')
        self.Entry1.place(relx=0.268, rely=0.391, height=25, relwidth=0.253)

        self.Label1_2_1 = tk.Label(self.Frame1, text='Host End Date', background="#d9d9d9")
        self.Label1_2_1.place(relx=0.022, rely=0.5, height=25, width=100)
        self.Entry1_1 = DateEntry(self.Frame1, date_pattern='dd/mm/yyyy', state='disabled')
        self.Entry1_1.place(relx=0.268, rely=0.5, height=25, relwidth=0.253)

        # Περιγραφή υιοθεσίας
        self.Label1_3 = tk.Label(self.Frame1, text='Adopt Description', background="#d9d9d9")
        self.Label1_3.place(relx=0.022, rely=0.656, height=25, width=120)
        self.Text2 = tk.Text(self.Frame1, wrap="word")
        self.Text2.place(relx=0.462, rely=0.656, relheight=0.294, relwidth=0.514)

        # Κουμπί Make
        self.Button1 = tk.Button(self.Frame1, text='Make', background="#0080ff", command=self.upload_announcement)
        self.Button1.place(relx=0.022, rely=0.906, height=26, width=60)

        # Κουμπί Clear All
        self.Button2 = tk.Button(self.Frame1, text='Clear all', background="#0080ff", command=self.clear_fields)
        self.Button2.place(relx=0.16, rely=0.906, height=26, width=60)

        # DBManager instance, χωρίς να ανοίγει σύνδεση αμέσως
        self.db = DBManager.DBManager(database='petato_db')

        #Για όταν κλείνει το παράθυρο
        self.top.protocol('WM_DELETE_WINDOW', self.goBack)

    def on_type_change(self, event=None):
        if self.announcement_type.get() == 'HOST':
            self.Entry1.config(state='normal')
            self.Entry1_1.config(state='normal')
            self.Text2.delete("1.0", tk.END)
            self.Text2.config(state='disabled')
        else:
            self.Entry1.set_date('01/01/2025')
            self.Entry1_1.set_date('01/01/2025')
            self.Entry1.config(state='disabled')
            self.Entry1_1.config(state='disabled')
            self.Text2.config(state='normal')

    def upload_announcement(self):
        ann_user = self.username
        ann_type = self.announcement_type.get()
        ann_pet = self.pet_type.get()
        ann_title = self.Text1.get("1.0", tk.END).strip()
        host_start_date = self.Entry1.get_date().strftime('%Y-%m-%d') if ann_type == 'HOST' else None
        host_end_date = self.Entry1_1.get_date().strftime('%Y-%m-%d') if ann_type == 'HOST' else None
        adopt_description = self.Text2.get("1.0", "end-1c") if ann_type == 'ADOPTION' else None

        if not ann_title or not ann_type or not ann_pet:
            MessageScreen.MessageScreen().display("Please fill in all required fields!")
            return

        try:
            self.db.connect()
            query = """
                INSERT INTO announcements
                (ann_title, ann_type, ann_pet, adopt_description, host_start_date, host_end_date, ann_user)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query, (ann_title, ann_type, ann_pet, adopt_description, host_start_date, host_end_date, ann_user))
            self.db.connection.commit()
            cursor.close()
            MessageScreen.MessageScreen().display("Announcement uploaded successfully!")
            self.clear_fields()
        except Exception as e:
            MessageScreen.MessageScreen().display("Failed to upload announcement")
        finally:
            self.db.close()

    def clear_fields(self):
        self.announcement_type.set('')
        self.pet_type.set('')
        self.Text1.delete("1.0", tk.END)
        self.Entry1.set_date(None)
        self.Entry1_1.set_date(None)
        self.Text2.config(state='normal')
        self.Text2.delete("1.0", tk.END)

    def display(self, previous_window=None):
        if previous_window is not None:
            previous_window.destroy()
        self.top.deiconify()

    def goBack(self):
        new_window = tk.Toplevel(self.root)
        new_window.protocol('WM_DELETE_WINDOW', new_window.destroy)
        main_menu_screen = MainMenuScreen.MainMenuScreen(top=new_window, root=self.root)
        main_menu_screen.display(previous_window=self.top)


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    window = MakeAnnouncementScreen(top, root, username='george_tsavos')
    root.mainloop()
