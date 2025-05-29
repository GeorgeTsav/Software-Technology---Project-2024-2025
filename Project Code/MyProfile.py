import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

import DBManager
import MainMenuScreen
import MyMessagesScreen
import MyAnnouncementsScreen
import PersonalDiaryScreen
import MyAppointmentsScreen

_location = os.path.dirname(__file__)

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class MyProfile:
    def __init__(self, top=None, root=None, username=None):
        self.top = top
        self.username = username 
        self.root = root

        self.top.geometry("642x594+523+84")
        self.top.minsize(120, 1)
        self.top.maxsize(1540, 845)
        self.top.resizable(0, 0)
        self.top.title("Petato")
        self.top.configure(background="#d9d9d9")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="#000000")

        self.menubar = tk.Menu(self.top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        self.top.configure(menu=self.menubar)

        self.MyProfileframe = tk.Frame(self.top)
        self.MyProfileframe.place(relx=0.016, rely=0.017, relheight=0.965
                , relwidth=0.955)
        self.MyProfileframe.configure(relief='groove')
        self.MyProfileframe.configure(borderwidth="2")
        self.MyProfileframe.configure(relief="groove")
        self.MyProfileframe.configure(background="#c0c0c0")
        self.MyProfileframe.configure(highlightbackground="#d9d9d9")
        self.MyProfileframe.configure(highlightcolor="#000000")

        self.MyProfilePhoto = tk.Label(self.MyProfileframe)
        self.MyProfilePhoto.place(relx=0.392, rely=0.07, height=142, width=144)
        self.MyProfilePhoto.configure(activebackground="#d9d9d9")
        self.MyProfilePhoto.configure(activeforeground="black")
        self.MyProfilePhoto.configure(anchor='w')
        self.MyProfilePhoto.configure(background="#8080ff")
        self.MyProfilePhoto.configure(compound='left')
        self.MyProfilePhoto.configure(disabledforeground="#a3a3a3")
        self.MyProfilePhoto.configure(font="-family {Segoe UI} -size 9")
        self.MyProfilePhoto.configure(foreground="#000000")
        self.MyProfilePhoto.configure(highlightbackground="#d9d9d9")
        self.MyProfilePhoto.configure(highlightcolor="#000000")
        self.MyProfilePhoto.configure(text='''userphoto''')

        self.MyProfileusername = tk.Label(self.MyProfileframe)
        self.MyProfileusername.place(relx=0.375, rely=0.366, height=29, width=162)
        self.MyProfileusername.configure(activebackground="#d9d9d9")
        self.MyProfileusername.configure(activeforeground="black")
        self.MyProfileusername.configure(anchor='w')
        self.MyProfileusername.configure(background="#ffffff")
        self.MyProfileusername.configure(compound='left')
        self.MyProfileusername.configure(disabledforeground="#a3a3a3")
        self.MyProfileusername.configure(font="-family {Segoe UI} -size 9")
        self.MyProfileusername.configure(foreground="#000000")
        self.MyProfileusername.configure(highlightbackground="#d9d9d9")
        self.MyProfileusername.configure(highlightcolor="#000000")
        self.MyProfileusername.configure(text=self.username if self.username else "unknown")
        

        self.fra47_lab51 = tk.Label(self.MyProfileframe)
        self.fra47_lab51.place(relx=0.462, rely=0.471, height=28, width=31)
        self.fra47_lab51.configure(activebackground="#d9d9d9")
        self.fra47_lab51.configure(activeforeground="black")
        self.fra47_lab51.configure(anchor='w')
        self.fra47_lab51.configure(background="#d9d9d9")
        self.fra47_lab51.configure(compound='left')
        self.fra47_lab51.configure(disabledforeground="#a3a3a3")
        self.fra47_lab51.configure(font="-family {Yu Gothic UI Semibold} -size 12 -weight bold")
        self.fra47_lab51.configure(foreground="#000000")
        self.fra47_lab51.configure(highlightbackground="#d9d9d9")
        self.fra47_lab51.configure(highlightcolor="#000000")
        self.fra47_lab51.configure(text='''/5''')

        self.StarforMyScore = tk.Label(self.MyProfileframe)
        self.StarforMyScore.place(relx=0.538, rely=0.471, height=28, width=32)
        self.StarforMyScore.configure(activebackground="#d9d9d9")
        self.StarforMyScore.configure(activeforeground="black")
        self.StarforMyScore.configure(anchor='w')
        self.StarforMyScore.configure(background="#d9d9d9")
        self.StarforMyScore.configure(compound='left')
        self.StarforMyScore.configure(disabledforeground="#a3a3a3")
        self.StarforMyScore.configure(font="-family {Segoe UI} -size 9")
        self.StarforMyScore.configure(foreground="#000000")
        self.StarforMyScore.configure(highlightbackground="#d9d9d9")
        self.StarforMyScore.configure(highlightcolor="#000000")
        self.StarforMyScore.configure(text='''Label''')

        self.MyScoreLabel = tk.Label(self.MyProfileframe)
        self.MyScoreLabel.place(relx=0.393, rely=0.471, height=28, width=32)
        self.MyScoreLabel.configure(activebackground="#d9d9d9")
        self.MyScoreLabel.configure(activeforeground="black")
        self.MyScoreLabel.configure(anchor='w')
        self.MyScoreLabel.configure(background="#d9d9d9")
        self.MyScoreLabel.configure(compound='left')
        self.MyScoreLabel.configure(disabledforeground="#a3a3a3")
        self.MyScoreLabel.configure(font="-family {Segoe UI} -size 9")
        self.MyScoreLabel.configure(foreground="#000000")
        self.MyScoreLabel.configure(highlightbackground="#d9d9d9")
        self.MyScoreLabel.configure(highlightcolor="#000000")
        self.MyScoreLabel.configure(text='''Label''')

        self.MyReviews = tk.Label(self.MyProfileframe)
        self.MyReviews.place(relx=0.392, rely=0.570, height=20, width=146)
        self.MyReviews.configure(activebackground="#d9d9d9")
        self.MyReviews.configure(activeforeground="black")
        self.MyReviews.configure(background="#808080")
        self.MyReviews.configure(compound='left')
        self.MyReviews.configure(disabledforeground="#a3a3a3")
        self.MyReviews.configure(font="-family {Yu Gothic UI Semibold} -size 11 -weight bold -underline 1")
        self.MyReviews.configure(foreground="#000000")
        self.MyReviews.configure(highlightbackground="#d9d9d9")
        self.MyReviews.configure(highlightcolor="#000000")
        self.MyReviews.configure(text='''My Reviews''')

        self.Myreviewlist = tk.Listbox(self.MyProfileframe)
        self.Myreviewlist.place(relx=0.280, rely=0.610, relheight=0.246, relwidth=0.45)
        self.Myreviewlist.configure(background="white")
        self.Myreviewlist.configure(disabledforeground="#a3a3a3")
        self.Myreviewlist.configure(font="TkFixedFont")
        self.Myreviewlist.configure(foreground="#000000")
        self.Myreviewlist.configure(highlightbackground="#d9d9d9")
        self.Myreviewlist.configure(highlightcolor="#000000")
        self.Myreviewlist.configure(selectbackground="#d9d9d9")
        self.Myreviewlist.configure(selectforeground="black")
        
        self.load_Myreviews()
        
        self.backbutton = tk.Button(self.MyProfileframe)
        self.backbutton.place(relx=0.799, rely=0.07, height=26, width=57)
        self.backbutton.configure(activebackground="#d9d9d9")
        self.backbutton.configure(activeforeground="black")
        self.backbutton.configure(background="#0000ff")
        self.backbutton.configure(cursor="fleur")
        self.backbutton.configure(disabledforeground="#a3a3a3")
        self.backbutton.configure(foreground="#ffffff")
        self.backbutton.configure(highlightbackground="#d9d9d9")
        self.backbutton.configure(highlightcolor="#000000")
        self.backbutton.configure(text='''⟵ BACK''')
        self.backbutton.configure(command=self.go_back)
        
        self.MyMessagesbutton = tk.Button(self.MyProfileframe)
        self.MyMessagesbutton.place(relx=0.033, rely=0.07, height=26, width=97)
        self.MyMessagesbutton.configure(activebackground="#d9d9d9")
        self.MyMessagesbutton.configure(activeforeground="black")
        self.MyMessagesbutton.configure(background="#d9d9d9")
        self.MyMessagesbutton.configure(disabledforeground="#a3a3a3")
        self.MyMessagesbutton.configure(foreground="#000000")
        self.MyMessagesbutton.configure(highlightbackground="#d9d9d9")
        self.MyMessagesbutton.configure(highlightcolor="#000000")
        self.MyMessagesbutton.configure(text='''My Messages''')
        self.MyMessagesbutton.configure(command=self.openMyMessages)
        
        self.MyAppointmentsbutton = tk.Button(self.MyProfileframe)
        self.MyAppointmentsbutton.place(relx=0.67, rely=0.908, height=26, width=107)
        self.MyAppointmentsbutton.configure(activebackground="#d9d9d9")
        self.MyAppointmentsbutton.configure(activeforeground="black")
        self.MyAppointmentsbutton.configure(background="#0000ff")
        self.MyAppointmentsbutton.configure(disabledforeground="#a3a3a3")
        self.MyAppointmentsbutton.configure(foreground="#ffffff")
        self.MyAppointmentsbutton.configure(highlightbackground="#d9d9d9")
        self.MyAppointmentsbutton.configure(highlightcolor="#000000")
        self.MyAppointmentsbutton.configure(text='''My Appointments''')
        self.MyAppointmentsbutton.configure(command=self.openMyAppointments)

        self.PersonalDiaryButton = tk.Button(self.MyProfileframe)
        self.PersonalDiaryButton.place(relx=0.4, rely=0.908, height=26, width=130)
        self.PersonalDiaryButton.configure(activebackground="#d9d9d9")
        self.PersonalDiaryButton.configure(activeforeground="black")
        self.PersonalDiaryButton.configure(background="#0000ff")
        self.PersonalDiaryButton.configure(disabledforeground="#a3a3a3")
        self.PersonalDiaryButton.configure(foreground="#ffffff")
        self.PersonalDiaryButton.configure(highlightbackground="#d9d9d9")
        self.PersonalDiaryButton.configure(highlightcolor="#000000")
        self.PersonalDiaryButton.configure(text='''Personal Diary''')
        self.PersonalDiaryButton.configure(command=self.openPersonalDiary)

        self.MyAnnouncemetsbutton = tk.Button(self.MyProfileframe)
        self.MyAnnouncemetsbutton.place(relx=0.15, rely=0.908, height=26, width=117)
        self.MyAnnouncemetsbutton.configure(activebackground="#d9d9d9")
        self.MyAnnouncemetsbutton.configure(activeforeground="black")
        self.MyAnnouncemetsbutton.configure(background="#0000ff")
        self.MyAnnouncemetsbutton.configure(disabledforeground="#a3a3a3")
        self.MyAnnouncemetsbutton.configure(foreground="#ffffff")
        self.MyAnnouncemetsbutton.configure(highlightbackground="#d9d9d9")
        self.MyAnnouncemetsbutton.configure(highlightcolor="#000000")
        self.MyAnnouncemetsbutton.configure(text='''My Announcemets''')
        self.MyAnnouncemetsbutton.configure(command=self.openMyAnnouncements)
      
    # Κλείνει το παράθυρο του MyProfile
    def go_back(self):
        new_top = tk.Toplevel(self.root)
        new_top.protocol('WM_DELETE_WINDOW', self.root.destroy)
        MainMenuScreen.MainMenuScreen(new_top, self.root, self.username).display(self.top)
           
    #για την λιστα των αξιλογήσεων
    def load_Myreviews(self):
        db = DBManager.DBManager(host='localhost', user='root', password='', database='petato_db')
        db.connect()

        review_query = """
            SELECT rev_writer, rev_score, rev_text, rev_date 
            FROM review 
            WHERE rev_user = %s
            ORDER BY rev_date DESC
        """
        cursor = db.execute_query(review_query, (self.username,))
        if cursor is None:
            print("The review query could not be executed.")
            db.close()
            return

        self.Myreviewlist.delete(0, tk.END)
        for rev_writer, rev_score, rev_text, rev_date in cursor.fetchall():
            preview_text = rev_text if rev_text else ''
            display_text = f"{rev_writer} ({rev_score}/5): {preview_text}"
            self.Myreviewlist.insert(tk.END, display_text)
        cursor.close()

        # Υπολογισμός μέσου όρου βαθμολογίας
        avg_query = "SELECT ROUND(AVG(rev_score),1) FROM review WHERE rev_user = %s"
        cursor = db.execute_query(avg_query, (self.username,))
        if cursor:
            avg_score = cursor.fetchone()[0]
            if avg_score is not None:
                self.MyScoreLabel.configure(text=str(avg_score))
                self.StarforMyScore.configure(text="★")
            else:
                self.MyScoreLabel.configure(text="0")
                self.StarforMyScore.configure(text="☆")
            cursor.close()
        else:
            print("The average query could not be executed")
            self.MyScoreLabel.configure(text="0")
            self.StarforMyScore.configure(text="☆")

        db.close()

    def display(self, previous_window=None):
        if previous_window is not None:
            previous_window.destroy()
        self.top.deiconify()
       
    def openMyMessages(self):
        new_top = tk.Toplevel(self.root)
        MyMessagesScreen.MyMessagesScreen(new_top, self.username)

    def openMyAnnouncements(self):
        new_top = tk.Toplevel(self.root)
        new_top.protocol('WM_DELETE_WINDOW', self.root.destroy)
        MyAnnouncementsScreen.MyAnnouncementsScreen(new_top, self.root, self.username).display(self.top)

    def openPersonalDiary(self):
        new_top = tk.Toplevel(self.root)
        new_top.protocol('WM_DELETE_WINDOW', self.root.destroy)
        PersonalDiaryScreen.PersonalDiaryScreen(new_top, self.root, self.username).display(self.top)

    def openMyAppointments(self):
        new_top = tk.Toplevel(self.root)
        MyAppointmentsScreen.MyAppointmentsScreen(new_top, self.root, self.username)


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    window = MyProfile(top, root, username="george_tsavos")
    root.mainloop()




