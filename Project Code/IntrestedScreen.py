import sys
import tkinter as tk
from tkinter.constants import *
import tkinter.ttk as ttk
import os.path

import DBManager
import MessageScreen
import SendMessage
import OtherProfile

_location = os.path.dirname(__file__)
_debug = True

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 


class InterestedScreen:
    def __init__(self, top=None, root=None, username=None, ann_id=None):
        self.username = username
        self.ann_id = ann_id
        self.top = top
        self.root = root

        self.top.geometry("610x299+850+200")
        self.top.minsize(120, 1)
        self.top.maxsize(1540, 845)
        self.top.resizable(1,  1)
        self.top.title(f"Interested List for Announcemnt {self.ann_id}")
        self.top.configure(background="#ffffff")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="#000000")

        self.IntrestedFrame = tk.Frame(
            self.top, relief='groove', 
            borderwidth=2, 
            background="#d9d9d9", 
            highlightbackground="#d9d9d9", 
            highlightcolor="#000000"
        )
        self.IntrestedFrame.place(relx=0.02, rely=0.054, relheight=0.9, relwidth=0.957)

        self.InterestedList = tk.Canvas(
            self.IntrestedFrame, 
            background="#ffffff", 
            borderwidth=2, 
            highlightbackground="#d9d9d9",
            highlightcolor="#000000", 
            insertbackground="#000000", 
            relief="ridge", 
            selectbackground="#d9d9d9", 
            selectforeground="black"
        )
        self.InterestedList.place(relx=0.017, rely=0.037, relheight=0.933, relwidth=0.955)

        self.scrollbar = tk.Scrollbar(self.InterestedList, orient="vertical", command=self.InterestedList.yview)
        self.scrollbar.place(relx=0.97, rely=0.029, relheight=0.936, anchor='ne')
        self.InterestedList.configure(yscrollcommand=self.scrollbar.set)

        self.list_frame = tk.Frame(self.InterestedList, bg="#ffffff")
        self.InterestedList.create_window((0, 0), window=self.list_frame, anchor="nw")

        self.list_frame.bind(
            "<Configure>",
            lambda e: self.InterestedList.configure(scrollregion=self.InterestedList.bbox("all"))
        )

        self.searchInterested()
    
    class InterestedWidget(tk.Frame):
        def __init__(self, top, root, int_user, ann_id, logged_in_user=None, *args, **kwargs):
            super().__init__(top, *args, **kwargs)

            self.int_user = int_user
            self.ann_id = ann_id
            self.root = root
            self.top = top
            self.logged_in_user = logged_in_user

            self.configure(bg="#ffffff", relief="ridge", bd=1)
            tk.Label(self, text=self.int_user, font=("Segoe UI", 12, "bold"), bg="#ffffff").pack(side=tk.LEFT, padx=10)
            tk.Button(self, text="Profile", activebackground="#0080ff", command=self.openOtherProfile).pack(side=tk.LEFT, padx=10)
            tk.Button(self, text="Approve", background="#5FD363", activebackground="#0080ff", command=self.approveInterested).pack(side=tk.LEFT, padx=10)
            tk.Button(self, text="Ignore", background="#ff1d1d", activebackground="#0080ff", command=self.ignoreInterested).pack(side=tk.LEFT, padx=10)

        def approveInterested(self):
            SendMessage.SendMessage(
                message=f"You have been approved by the owner of the announcement {self.ann_id}.",
                receiver=self.int_user
            ).sendMsg()

            self.deleteAnn()

            self.destroy()

        def deleteAnn(self):
            db = DBManager.DBManager(database="petato_db")
            db.connect()

            db.execute_query(
                "DELETE FROM announcements WHERE ann_id = %s", 
                (self.ann_id,)
            )
            db.connection.commit()
            
            db.close()

        def ignoreInterested(self):
            db = DBManager.DBManager(database="petato_db")
            db.connect()

            db.execute_query(
                "DELETE FROM interested_users WHERE int_user = %s AND int_ann = %s", 
                (self.username, self.ann_id)
            )
            db.connection.commit()
            
            db.close()

            SendMessage.SendMessage(f"You have been ignored by the owner of the announcement {self.ann_id}.", self.username).sendMsg()

            self.destroy()
        
        def openOtherProfile(self):
            OtherProfile.OtherProfile(top=tk.Toplevel(self.root), username=self.int_user, logged_in_user=self.logged_in_user)

    def searchInterested(self):
        # Καθαρίζει το frame της λίστας από προηγούμενα widgets
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        # Παίρνει τις ανακοινώσεις του χρήστη από τη βάση δεδομένων
        db = DBManager.DBManager(database="petato_db")
        db.connect()
        db_cursor = db.execute_query("SELECT int_user FROM interested_users WHERE int_ann = %s", (self.ann_id,))
        results = db_cursor.fetchall()

        # Δημιουργεί ένα MyAnnouncementWidget για κάθε ανακοίνωση
        if results:
            for int_user in results:
                widget = self.InterestedWidget(self.list_frame, self.root, int_user[0], self.ann_id, self.username)
                widget.pack(fill=tk.X, pady=4, padx=4)
            
            db_cursor.close()
        else:
            MessageScreen.MessageScreen.display(self.top,"There are no interested users for this announcement yet!")
            db_cursor.close()


        db.close()

        # Ενημερώνει το frame της λίστας για να εμφανίσει τα νέα widgets
        self.list_frame.update_idletasks()


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    ann_id = 3
    window = InterestedScreen(top, root, username="george_tsavos", ann_id=ann_id)
    root.mainloop()