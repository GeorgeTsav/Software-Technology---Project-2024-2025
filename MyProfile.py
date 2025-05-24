import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import DBManager
import MainMenuScreen
import OtherProfile
import MessageScreen

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class MyProfile:
    def __init__(self, top=None, username=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("642x594+523+84")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Petato")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.username = username 

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

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
        self.MyReviews.place(relx=0.392, rely=0.611, height=28, width=146)
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
        self.Myreviewlist.place(relx=0.392, rely=0.698, relheight=0.246
                , relwidth=0.23)
        self.Myreviewlist.configure(background="white")
        self.Myreviewlist.configure(disabledforeground="#a3a3a3")
        self.Myreviewlist.configure(font="TkFixedFont")
        self.Myreviewlist.configure(foreground="#000000")
        self.Myreviewlist.configure(highlightbackground="#d9d9d9")
        self.Myreviewlist.configure(highlightcolor="#000000")
        self.Myreviewlist.configure(selectbackground="#d9d9d9")
        self.Myreviewlist.configure(selectforeground="black")
        
        
    def load_Myreviews(self):
        db = DBManager(host='localhost', user='root', password='', database='petato_db')
        db.connect()

        query = """
            SELECT rev_writer, rev_score, rev_text, rev_date 
            FROM review 
            WHERE rev_user = %s
            ORDER BY rev_date DESC
        """

        cursor = db.execute_query(query, (self.username,))

        if cursor is None:
            print("Δεν μπόρεσε να εκτελεστεί το query.")
            db.close()
            return

        self.Myreviewlist.delete(0, tk.END)
        for rev_writer, rev_score, rev_text, rev_date in cursor.fetchall():
            preview_text = rev_text if rev_text else ''
            display_text = f"{rev_writer} ({rev_score}/5): {preview_text}"
            self.reviewlist.insert(tk.END, display_text)
        cursor.close()
        db.close()    



if __name__ == '__main__':
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = MyProfile(_top1)
    root.mainloop()




