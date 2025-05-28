import sys
import tkinter as tk
from tkinter.constants import *
import tkinter.ttk as ttk
import os.path
import re
import DBManager

debug = True
_location = os.path.dirname(__file__)

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black'
_tabfg2 = 'white'
_bgmode = 'light'
_tabbg1 = '#d9d9d9'
_tabbg2 = 'gray40'

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
        return
    try:
        MakeAnnouncementScreen.root.tk.call(
            'source',
            os.path.join(_location, 'themes', 'default.tcl')
        )
    except:
        pass
    style = ttk.Style()
    style.theme_use('default')
    style.configure('.', font="TkDefaultFont")
    if sys.platform == "win32":
        style.theme_use('winnative')
    _style_code_ran = 1

class MakeAnnouncementScreen:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1, 1)
        top.title("Petato")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.combobox = tk.StringVar()
        self.announcement_type = tk.StringVar()
        self.pet_type = tk.StringVar()

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.133, rely=0.178, relheight=0.711, relwidth=0.758)
        self.Frame1.configure(relief='raised')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="raised")
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#000000")

        self.Label1_2_1 = tk.Label(self.Frame1)
        self.Label1_2_1.place(relx=0.022, rely=0.5, height=25, width=100)
        self.Label1_2_1.configure(activebackground="#d9d9d9")
        self.Label1_2_1.configure(activeforeground="black")
        self.Label1_2_1.configure(anchor='w')
        self.Label1_2_1.configure(background="#d9d9d9")
        self.Label1_2_1.configure(compound='left')
        self.Label1_2_1.configure(disabledforeground="#a3a3a3")
        self.Label1_2_1.configure(font="-family {Segoe UI} -size 9")
        self.Label1_2_1.configure(foreground="#000000")
        self.Label1_2_1.configure(highlightbackground="#d9d9d9")
        self.Label1_2_1.configure(highlightcolor="#000000")
        self.Label1_2_1.configure(relief="groove")
        self.Label1_2_1.configure(text='Host_end_date')

        self.Label1_2 = tk.Label(self.Frame1)
        self.Label1_2.place(relx=0.022, rely=0.391, height=25, width=100)
        self.Label1_2.configure(activebackground="#d9d9d9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(anchor='w')
        self.Label1_2.configure(background="#d9d9d9")
        self.Label1_2.configure(compound='left')
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font="-family {Segoe UI} -size 9")
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="#000000")
        self.Label1_2.configure(relief="groove")
        self.Label1_2.configure(text='Host_start_date')

        _style_code()
        self.TCombobox1_1 = ttk.Combobox(self.Frame1)
        self.TCombobox1_1.place(relx=0.149, rely=0.281, relheight=0.078, relwidth=0.22)
        self.value_list = ['DOG', 'CAT']
        self.TCombobox1_1.configure(values=self.value_list)
        self.TCombobox1_1.configure(font="-family {Segoe UI} -size 9")
        self.TCombobox1_1.configure(textvariable=self.combobox)

        self.Label1_1_1 = tk.Label(self.Frame1)
        self.Label1_1_1.place(relx=0.022, rely=0.281, height=25, width=50)
        self.Label1_1_1.configure(activebackground="#d9d9d9")
        self.Label1_1_1.configure(activeforeground="black")
        self.Label1_1_1.configure(anchor='w')
        self.Label1_1_1.configure(background="#d9d9d9")
        self.Label1_1_1.configure(compound='left')
        self.Label1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1.configure(font="-family {Segoe UI} -size 9")
        self.Label1_1_1.configure(foreground="#000000")
        self.Label1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1.configure(highlightcolor="#000000")
        self.Label1_1_1.configure(relief="groove")
        self.Label1_1_1.configure(text='Pet')

        self.Text1 = tk.Text(self.Frame1)
        self.Text1.place(relx=0.22, rely=0.172, relheight=0.078, relwidth=0.295)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="#000000")
        self.Text1.configure(insertbackground="#000000")
        self.Text1.configure(selectbackground="#d9d9d9")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")

        self.Label1_1 = tk.Label(self.Frame1)
        self.Label1_1.place(relx=0.022, rely=0.172, height=25, width=80)
        self.Label1_1.configure(activebackground="#d9d9d9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(compound='left')
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Segoe UI} -size 9")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="#000000")
        self.Label1_1.configure(relief="groove")
        self.Label1_1.configure(text='Title')

        # Τύπος αγγελίας
        self.TCombobox1 = ttk.Combobox(self.Frame1, textvariable=self.announcement_type)
        self.TCombobox1.place(relx=0.374, rely=0.063, relheight=0.078, relwidth=0.301)
        self.TCombobox1['values'] = ['ADOPTION', 'HOST']
        self.TCombobox1.configure(font="-family {Segoe UI} -size 9")
        self.TCombobox1.bind("<<ComboboxSelected>>", self.on_type_change)

        # Τύπος ζώου
        self.TCombobox1_1 = ttk.Combobox(self.Frame1, textvariable=self.pet_type)
        self.TCombobox1_1.place(relx=0.149, rely=0.281, relheight=0.078, relwidth=0.22)
        self.TCombobox1_1['values'] = ['DOG', 'CAT']
        self.TCombobox1_1.configure(font="-family {Segoe UI} -size 9")

        # Host_start_date
        vcmd = (self.Frame1.register(self.validate_date), '%P')
        self.Entry1 = tk.Entry(self.Frame1, validate='focusout', validatecommand=vcmd)
        self.Entry1.place(relx=0.268, rely=0.391, height=25, relwidth=0.253)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 10")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="#000000")
        self.Entry1.configure(insertbackground="#000000")
        self.Entry1.configure(selectbackground="#d9d9d9")
        self.Entry1.configure(selectforeground="black")

        # Host_end_date
        self.Entry1_1 = tk.Entry(self.Frame1, validate='focusout', validatecommand=vcmd)
        self.Entry1_1.place(relx=0.268, rely=0.5, height=25, relwidth=0.253)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="-family {Courier New} -size 10")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="#000000")
        self.Entry1_1.configure(insertbackground="#000000")
        self.Entry1_1.configure(selectbackground="#d9d9d9")
        self.Entry1_1.configure(selectforeground="black")

        # Αρχικά απενεργοποιημένα
        self.Entry1.config(state='disabled')
        self.Entry1_1.config(state='disabled')

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.022, rely=0.063, height=25, width=150)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 9")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(relief="groove")
        self.Label1.configure(text='Type of Announcement')

        self.Label1_3 = tk.Label(self.Frame1)
        self.Label1_3.place(relx=0.022, rely=0.656, height=25, width=120)
        self.Label1_3.configure(activebackground="#d9d9d9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(anchor='w')
        self.Label1_3.configure(background="#d9d9d9")
        self.Label1_3.configure(compound='left')
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(font="-family {Segoe UI} -size 9")
        self.Label1_3.configure(foreground="#000000")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="#000000")
        self.Label1_3.configure(relief="groove")
        self.Label1_3.configure(text='Description')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.022, rely=0.906, height=26, width=47)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#0080ff")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 9")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='Upload')
        self.Button1.configure(command=self.upload_announcement)

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.154, rely=0.906, height=26, width=47)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#0080ff")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 9")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="#000000")
        self.Button2.configure(text='Delete')
        self.Button2.configure(command=self.clear_fields)

        self.Text2 = tk.Text(self.Frame1)
        self.Text2.place(relx=0.462, rely=0.656, relheight=0.294, relwidth=0.514)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="#000000")
        self.Text2.configure(insertbackground="#000000")
        self.Text2.configure(relief="groove")
        self.Text2.configure(selectbackground="#d9d9d9")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(wrap="word")

        self.db = DBManager.DBManager(host='localhost', user='root', password='', database='petato_db')
        self.db.connect()

    def on_type_change(self, event=None):
        if self.announcement_type.get() == 'HOST':
            self.Entry1.config(state='normal')
            self.Entry1_1.config(state='normal')
        else:
            self.Entry1.delete(0, tk.END)
            self.Entry1_1.delete(0, tk.END)
            self.Entry1.config(state='disabled')
            self.Entry1_1.config(state='disabled')

    def validate_date(self, value):
        # Επιτρέπει κενό ή ΗΗ/ΜΜ/ΕΕΕΕ
        if not value:
            return True
        return bool(re.match(r'^\d{2}/\d{2}/\d{4}$', value))

    def upload_announcement(self):
        ann_type = self.announcement_type.get()
        ann_pet = self.pet_type.get()
        ann_title = self.Text1.get("1.0", tk.END).strip()
        host_start_date = self.Entry1.get() if ann_type == 'HOST' else None
        host_end_date = self.Entry1_1.get() if ann_type == 'HOST' else None
        adopt_description = self.Text2.get("1.0", tk.END).strip()
        ann_user = 'spiros'  

        query = """
            INSERT INTO announcements
            (ann_title, ann_type, ann_pet, adopt_description, host_start_date, host_end_date, ann_user)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (ann_title, ann_type, ann_pet, adopt_description, host_start_date, host_end_date, ann_user)
        self.db.execute_query(query, params)
        self.db.connection.commit()  # Για να αποθηκευτούν οι αλλαγές

    def clear_fields(self):
        self.announcement_type.set('')
        self.pet_type.set('')
        self.Text1.delete("1.0", tk.END)
        self.Entry1.delete(0, tk.END)
        self.Entry1_1.delete(0, tk.END)
        self.Text2.delete("1.0", tk.END)

def start_up():
    MakeAnnouncementScreen.main()

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    window = MakeAnnouncementScreen(top)
    root.mainloop()
