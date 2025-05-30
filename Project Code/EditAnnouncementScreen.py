import tkinter as tk
from tkinter.constants import *
import tkinter.ttk as ttk
from tkcalendar import DateEntry

import DBManager
import MessageScreen

class EditAnnouncementScreen:
    def __init__(self, top=None, ann_id=None):
        self.top = top
        self.ann_id = ann_id

        self.top.geometry("600x450+600+138")
        self.top.title("Edit Announcement")
        self.top.configure(background="#d9d9d9")

        self.announcement_type = tk.StringVar()
        self.pet_type = tk.StringVar()

        tk.Label(top, text="Edit Announcement", font=("Segoe UI", 20, "bold"),
                 bg="#d9d9d9", fg="black").pack(pady=10)

        self.Frame1 = tk.Frame(self.top, relief='raised', borderwidth=2, background="#ffffff")
        self.Frame1.place(relx=0.133, rely=0.178, relheight=0.711, relwidth=0.758)

        tk.Label(self.Frame1, text='Type of Announcement', background="#d9d9d9").place(relx=0.022, rely=0.063)
        self.TCombobox1 = ttk.Combobox(self.Frame1, textvariable=self.announcement_type)
        self.TCombobox1.place(relx=0.374, rely=0.063, relheight=0.078, relwidth=0.301)
        self.TCombobox1['values'] = ['ADOPTION', 'HOST']
        self.TCombobox1.bind("<<ComboboxSelected>>", self.on_type_change)

        tk.Label(self.Frame1, text='Title', background="#d9d9d9").place(relx=0.022, rely=0.172)
        self.Text1 = tk.Text(self.Frame1, wrap="word")
        self.Text1.place(relx=0.22, rely=0.172, relheight=0.078, relwidth=0.295)

        tk.Label(self.Frame1, text='Pet', background="#d9d9d9").place(relx=0.022, rely=0.281)
        self.TCombobox1_1 = ttk.Combobox(self.Frame1, textvariable=self.pet_type)
        self.TCombobox1_1.place(relx=0.149, rely=0.281, relheight=0.078, relwidth=0.22)
        self.TCombobox1_1['values'] = ['DOG', 'CAT']

        tk.Label(self.Frame1, text='Host Start Date', background="#d9d9d9").place(relx=0.022, rely=0.391)
        self.Entry1 = DateEntry(self.Frame1, date_pattern='dd/mm/yyyy', state='disabled')
        self.Entry1.place(relx=0.268, rely=0.391, height=25, relwidth=0.253)

        tk.Label(self.Frame1, text='Host End Date', background="#d9d9d9").place(relx=0.022, rely=0.5)
        self.Entry1_1 = DateEntry(self.Frame1, date_pattern='dd/mm/yyyy', state='disabled')
        self.Entry1_1.place(relx=0.268, rely=0.5, height=25, relwidth=0.253)

        tk.Label(self.Frame1, text='Adopt Description', background="#d9d9d9").place(relx=0.022, rely=0.656)
        self.Text2 = tk.Text(self.Frame1, wrap="word")
        self.Text2.place(relx=0.462, rely=0.656, relheight=0.294, relwidth=0.514)

        self.Button1 = tk.Button(self.Frame1, text='Save', background="#0080ff", command=self.update_announcement)
        self.Button1.place(relx=0.022, rely=0.906, height=26, width=60)

        self.Button2 = tk.Button(self.Frame1, text='Delete', background="#0080ff", command=self.delete_announcement)
        self.Button2.place(relx=0.16, rely=0.906, height=26, width=60)

        self.db = DBManager.DBManager(host='localhost', user='root', password='', database='petato_db')
        self.db.connect()
        self.load_announcement()

    def load_announcement(self):
        query = "SELECT ann_title, ann_type, ann_pet, adopt_description, host_start_date, host_end_date FROM announcements WHERE ann_id = %s"
        result = self.db.execute_query(query, (self.ann_id,)).fetchone()

        if result:
            ann_title, ann_type, ann_pet, adopt_description, host_start_date, host_end_date = result
            self.announcement_type.set(ann_type)
            self.TCombobox1.configure(state="disabled")
            self.pet_type.set(ann_pet)
            self.Text1.insert("1.0", ann_title)

            if ann_type == 'HOST':
                self.Entry1.config(state='normal')
                self.Entry1_1.config(state='normal')
                self.Entry1.set_date(host_start_date)
                self.Entry1_1.set_date(host_end_date)
                self.Text2.config(state='disabled')
            else:
                self.Text2.insert("1.0", adopt_description or "")
                
    def on_type_change(self, event=None):
        if self.announcement_type.get() == 'HOST':
            self.Entry1.config(state='normal')
            self.Entry1_1.config(state='normal')
            self.Text2.delete("1.0", tk.END)
            self.Text2.config(state='disabled')
        else:
            self.Entry1.config(state='disabled')
            self.Entry1_1.config(state='disabled')
            self.Text2.config(state='normal')

    def update_announcement(self):
        ann_type = self.announcement_type.get()
        ann_pet = self.pet_type.get()
        ann_title = self.Text1.get("1.0", tk.END).strip()
        host_start_date = self.Entry1.get_date().strftime('%Y-%m-%d') if ann_type == 'HOST' else None
        host_end_date = self.Entry1_1.get_date().strftime('%Y-%m-%d') if ann_type == 'HOST' else None
        adopt_description = self.Text2.get("1.0", "end-1c") if ann_type == 'ADOPTION' else None

        query = """
            UPDATE announcements SET
                ann_title = %s,
                ann_type = %s,
                ann_pet = %s,
                adopt_description = %s,
                host_start_date = %s,
                host_end_date = %s
            WHERE ann_id = %s
        """
        params = (ann_title, ann_type, ann_pet, adopt_description, host_start_date, host_end_date, self.ann_id)
        self.db.execute_query(query, params)
        self.db.connection.commit()
        MessageScreen.MessageScreen.display("The announcement has been updated","The announcement has been updated")
        self.top.destroy()

    def delete_announcement(self):
        query = "DELETE FROM announcements WHERE ann_id = %s"
        self.db.execute_query(query, (self.ann_id,))
        self.db.connection.commit()
        MessageScreen.MessageScreen().display("The announcement has been deleted")
        self.top.destroy()



if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    window = EditAnnouncementScreen(top, ann_id=16)
    root.mainloop()

