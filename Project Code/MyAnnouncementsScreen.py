import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

import DBManager
import MessageScreen
import IntrestedScreen
import EditScreen  

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
    def __init__(self, master, ann_title, ann_id, parent, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.ann_id = ann_id
        self.ann_title = ann_title
        self.parent = parent

        self.configure(bg="#ffffff", relief="ridge", bd=1)
        tk.Label(self, text=ann_title, font=("Segoe UI", 12, "bold"), bg="#ffffff").pack(side=tk.LEFT, padx=10)

        tk.Button(
            self,
            text="Details",
            bg="#0080ff",
            fg="white",
            font=("Segoe UI", 9, "bold"),
            command=self.showDetails
        ).pack(side=tk.RIGHT, padx=10)

        tk.Button(
            self,
            text="Interested",
            activebackground="#0080ff",
            command=self.openInterested
        ).pack(side=tk.RIGHT, padx=10)

    def openInterested(self):
        IntrestedScreen.InterestedScreen(tk.Toplevel(), self.ann_id)

    def showDetails(self):
        new_window = tk.Toplevel(self)
        EditScreen.EditScreen(top=new_window, root=self.parent.root, username=self.parent.username, ann_id=self.ann_id)

class MyAnnouncementsScreen:
    def __init__(self, top=None, root=None, username=None):
        self.username = username
        self.root = root
        self.top = top

        self.top.geometry("600x450+468+138")
        self.top.minsize(120, 1)
        self.top.maxsize(1540, 845)
        self.top.resizable(1, 1)
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
        self.MyAnnouncementsFrame.place(relx=0.033, rely=0.178, relheight=0.7, relwidth=0.942)

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

        self.BackButton = tk.Button(
            self.top,
            text="Back",
            activebackground="#0080ff",
            command=self.goBack
        )
        self.BackButton.place(relx=0.5, rely=0.93, anchor=tk.CENTER, height=30, width=80)

        self.searchAnnouncements()

    def goBack(self):
        self.top.destroy()
        if self.root:
            self.root.deiconify()

    def display(self, previous_window=None):
        if previous_window is not None:
            previous_window.destroy()
        self.top.deiconify()

    def searchAnnouncements(self):
    
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        db = DBManager.DBManager(database="petato_db")
        try:
            db.connect()
            cursor = db.execute_query(
                "SELECT ann_id, ann_title FROM announcements WHERE ann_user = %s",
                (self.username,)
            )
            results = cursor.fetchall()

            if results:
                for ann in results:
                    widget = MyAnnouncementWidget(self.list_frame, ann[1], ann[0], self)
                    widget.pack(fill=tk.X, pady=4, padx=4)
            else:
                MessageScreen.MessageScreen.display(self.top, "You have no announcements yet!")

            cursor.close()
        except Exception as e:
            MessageScreen.MessageScreen.display(self.top, "Error loading announcements: {e}")
        finally:
            db.close()

        

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    username = "george_tsavos"
    window = MyAnnouncementsScreen(top, root, username)
    root.mainloop()
