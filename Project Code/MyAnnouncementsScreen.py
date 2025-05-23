import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

import DBManager
import MessageScreen
import IntrestedScreen

_location = os.path.dirname(__file__)
_debug = True

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class MyAnnouncementWidget(tk.Frame):
    def __init__(self, master, ann_title, ann_id, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.ann_id = ann_id
        self.ann_title = ann_title

        self.configure(bg="#ffffff", relief="ridge", bd=1)
        tk.Label(self, text=ann_title, font=("Segoe UI", 12, "bold"), bg="#ffffff").pack(side=tk.LEFT, padx=10)
        tk.Button(self, text="Details", activebackground="#0080ff", command=self.showDetails).pack(side=tk.LEFT, padx=10)
        tk.Button(self, text="Interested", activebackground="#0080ff", command=self.openInterested).pack(side=tk.LEFT, padx=10)

    def openInterested(self):
        pass

    def showDetails(self):
        pass


class MyAnnouncementsScreen:
    def __init__(self, top=None, root=None, username=None):
        self.username = username
        self.root = root
        self.top = top

        self.top.geometry("600x450+468+138")
        self.top.minsize(120, 1)
        self.top.maxsize(1540, 845)
        self.top.resizable(1,  1)
        self.top.title("Petato")
        self.top.configure(background="#ffffff")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="#000000")

        self.MyAnnouncementsFrame = tk.Frame(
            self.top,
            relief='groove',
            borderwidth=2,
            background="#d9d9d9",
            highlightbackground="#d9d9d9",
            highlightcolor="#000000"
        )
        self.MyAnnouncementsFrame.place(relx=0.033, rely=0.178, relheight=0.767, relwidth=0.942)

        self.MyAnnouncementsList = tk.Canvas(
            self.MyAnnouncementsFrame,
            background="#ffffff",
            borderwidth=2,
            highlightbackground="#d9d9d9",
            highlightcolor="#000000",
            insertbackground="#000000",
            relief="ridge",
            selectbackground="#d9d9d9",
            selectforeground="black"
        )
        self.MyAnnouncementsList.place(relx=0.018, rely=0.029, relheight=0.936, relwidth=0.961)

        self.scrollbar = tk.Scrollbar(self.MyAnnouncementsList, orient="vertical", command=self.MyAnnouncementsList.yview)
        self.scrollbar.place(relx=0.97, rely=0.029, relheight=0.936, anchor='ne')
        self.MyAnnouncementsList.configure(yscrollcommand=self.scrollbar.set)

        self.list_frame = tk.Frame(self.MyAnnouncementsList, bg="#ffffff")
        self.MyAnnouncementsList.create_window((0, 0), window=self.list_frame, anchor="nw")

        self.list_frame.bind(
            "<Configure>",
            lambda e: self.MyAnnouncementsList.configure(scrollregion=self.MyAnnouncementsList.bbox("all"))
        )

        self.MyAnnouncementsLabel = tk.Label(
            self.top,
            activebackground="#d9d9d9",
            activeforeground="black",
            anchor='w',
            background="#ffffff",
            compound='left',
            disabledforeground="#a3a3a3",
            font="-family {Segoe UI} -size 22 -weight bold",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="#000000",
            text='''My Announcements'''
        )
        self.MyAnnouncementsLabel.place(relx=0.283, rely=0.044, height=41, width=284)

        self.searchAnnouncements()

    #Σβήνει το προηγούμενο παράθυρο και εμφανίζει το νέο
    def display(self, previous_window=None):
        if previous_window is not None:
            previous_window.destroy()
        self.top.deiconify()

    def searchAnnouncements(self):
        # Καθαρίζει το frame της λίστας από προηγούμενα widgets
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        # Παίρνει τις ανακοινώσεις του χρήστη από τη βάση δεδομένων
        db = DBManager.DBManager(database="petato_db")
        db.connect()
        db_cursor = db.execute_query("SELECT ann_id, ann_title  FROM announcements WHERE ann_user = %s", (self.username,))
        results = db_cursor.fetchall()

        # Δημιουργεί ένα MyAnnouncementWidget για κάθε ανακοίνωση
        if results:
            for ann in results:
                widget = MyAnnouncementWidget(self.list_frame, ann[1], ann[0])
                widget.pack(fill=tk.X, pady=4, padx=4)
            
            db_cursor.close()
        else:
            MessageScreen.MessageScreen.display(self.top,"You have no announcements yet!")
            db_cursor.close()
         

        db.close()

        # Ενημερώνει το frame της λίστας για να εμφανίσει τα νέα widgets
        self.list_frame.update_idletasks()

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    username = "george_tsavos"
    window = MyAnnouncementsScreen(top, root, username)
    root.mainloop()

