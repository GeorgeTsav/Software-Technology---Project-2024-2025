import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import ReviewScreen
from DBManager import DBManager
import MainMenuScreen

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class OtherProfile:
    def __init__(self, top=None, root=None, username=None, logged_in_user=None):
        self.top = top
        self.root = root
        self.username = username
        self.logged_in_user = logged_in_user

        self.top.geometry("642x594+523+84")
        self.top.minsize(120, 1)
        self.top.maxsize(1540, 845)
        self.top.resizable(0,  0)
        self.top.title("Petato")
        self.top.configure(background="#d9d9d9")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="#000000")

        self.menubar = tk.Menu(self.top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        self.top.configure(menu=self.menubar)


        self.reviewscreenframe = tk.Frame(self.top)
        self.reviewscreenframe.place(relx=0.016, rely=0.0, relheight=0.965
                , relwidth=0.956)
        self.reviewscreenframe.configure(relief='groove')
        self.reviewscreenframe.configure(borderwidth="2")
        self.reviewscreenframe.configure(relief="groove")
        self.reviewscreenframe.configure(background="#c0c0c0")
        self.reviewscreenframe.configure(highlightbackground="#d9d9d9")
        self.reviewscreenframe.configure(highlightcolor="#000000")

        self.StarforScore = tk.Label(self.reviewscreenframe)
        self.StarforScore.place(relx=0.537, rely=0.471, height=28, width=32)
        self.StarforScore.configure(activebackground="#d9d9d9")
        self.StarforScore.configure(activeforeground="black")
        self.StarforScore.configure(anchor='w')
        self.StarforScore.configure(background="#d9d9d9")
        self.StarforScore.configure(compound='left')
        self.StarforScore.configure(disabledforeground="#a3a3a3")
        self.StarforScore.configure(foreground="#000000")
        self.StarforScore.configure(highlightbackground="#d9d9d9")
        self.StarforScore.configure(highlightcolor="#000000")
        self.StarforScore.configure(text='''Label''')

        self.Label1 = tk.Label(self.reviewscreenframe)
        self.Label1.place(relx=0.463, rely=0.471, height=28, width=31)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Yu Gothic UI Semibold} -size 12 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(text='''/5''')

        self.UserPhoto = tk.Label(self.reviewscreenframe)
        self.UserPhoto.place(relx=0.393, rely=0.07, height=142, width=144)
        self.UserPhoto.configure(activebackground="#d9d9d9")
        self.UserPhoto.configure(activeforeground="black")
        self.UserPhoto.configure(anchor='w')
        self.UserPhoto.configure(background="#8080ff")
        self.UserPhoto.configure(compound='left')
        self.UserPhoto.configure(disabledforeground="#a3a3a3")
        self.UserPhoto.configure(font="-family {Segoe UI} -size 9")
        self.UserPhoto.configure(foreground="#000000")
        self.UserPhoto.configure(highlightbackground="#d9d9d9")
        self.UserPhoto.configure(highlightcolor="#000000")
        self.UserPhoto.configure(text='''userphoto''')

        #for username drom DB
        self.username_label = tk.Label(self.top, text=username)
        self.username_label.place(relx=0.375, rely=0.366, height=29, width=162)
        self.username_label.configure(activebackground="#d9d9d9")
        self.username_label.configure(activeforeground="black")
        self.username_label.configure(anchor='w')
        self.username_label.configure(background="#ffffff")
        self.username_label.configure(compound='left')
        self.username_label.configure(disabledforeground="#a3a3a3")
        self.username_label.configure(font="-family {Segoe UI} -size 9")
        self.username_label.configure(foreground="#000000")
        self.username_label.configure(highlightbackground="#d9d9d9")
        self.username_label.configure(highlightcolor="#000000")
        self.username_label.configure(text=self.username)

        self.Label2 = tk.Label(self.reviewscreenframe)
        self.Label2.place(relx=0.383, rely=0.611, height=28, width=146)
        self.Label2.configure(activebackground="#d9d9d9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Yu Gothic UI Semibold} -size 11 -weight bold -underline 1")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="#000000")
        self.Label2.configure(text='''My Reviews''')

        self.reviewlist = tk.Listbox(self.reviewscreenframe)
        self.reviewlist.place(relx=0.393, rely=0.698, relheight=0.246
                , relwidth=0.45)
        self.reviewlist.configure(background="white")
        self.reviewlist.configure(disabledforeground="#a3a3a3")
        self.reviewlist.configure(font="TkFixedFont")
        self.reviewlist.configure(foreground="#000000")
        self.reviewlist.configure(highlightbackground="#d9d9d9")
        self.reviewlist.configure(highlightcolor="#000000")
        self.reviewlist.configure(selectbackground="#d9d9d9")
        self.reviewlist.configure(selectforeground="black")

        self.ScoreLabel = tk.Label(self.reviewscreenframe)
        self.ScoreLabel.place(relx=0.393, rely=0.471, height=28, width=32)
        self.ScoreLabel.configure(activebackground="#d9d9d9")
        self.ScoreLabel.configure(activeforeground="black")
        self.ScoreLabel.configure(anchor='w')
        self.ScoreLabel.configure(background="#d9d9d9")
        self.ScoreLabel.configure(compound='left')
        self.ScoreLabel.configure(cursor="fleur")
        self.ScoreLabel.configure(disabledforeground="#a3a3a3")
        self.ScoreLabel.configure(foreground="#000000")
        self.ScoreLabel.configure(highlightbackground="#d9d9d9")
        self.ScoreLabel.configure(highlightcolor="#000000")
        self.ScoreLabel.configure(text='''Label''')
        
    
        self.WriteReviewButton = ttk.Button(self.reviewscreenframe)
        self.WriteReviewButton.place(relx=0.07, rely=0.785, height=26  , width=125)
        self.WriteReviewButton.configure(takefocus="")
        self.WriteReviewButton.configure(text='''WriteReview''')
        self.WriteReviewButton.configure(compound='left')
        self.WriteReviewButton.configure(command=self.open_review_screen)
        
        self.backbutton = tk.Button(self.reviewscreenframe)
        self.backbutton.place(relx=0.07, rely=0.85, height=26, width=125)
        self.backbutton.configure(activebackground="#d9d9d9")
        self.backbutton.configure(activeforeground="black")
        self.backbutton.configure(background="#d9d9d9")
        self.backbutton.configure(cursor="fleur")
        self.backbutton.configure(disabledforeground="#a3a3a3")
        self.backbutton.configure(foreground="#000000")
        self.backbutton.configure(highlightbackground="#d9d9d9")
        self.backbutton.configure(highlightcolor="#000000")
        self.backbutton.configure(text='''Back''')
        self.backbutton.configure(command=self.go_back)
        
        self.load_reviews()
        
    def display(self, previous_window=None):
        if previous_window is not None:
            previous_window.destroy()
        self.top.deiconify()
    
    
     # Κλείνει το παράθυρο του MyProfile
   
    def go_back(self):
      if self.root is not None:
        new_top = tk.Toplevel(self.root)
        new_top.protocol('WM_DELETE_WINDOW', self.root.destroy)
        MainMenuScreen.MainMenuScreen(new_top, self.root, self.logged_in_user).display(self.top)
      elif self.top is not None:
         self.top.destroy()

    #for pop up review screen
    def open_review_screen(self):
        popup = tk.Toplevel(self.top)
        ReviewScreen.ReviewScreen(popup, username=self.username, logged_in_user=self.logged_in_user)

        def on_close():
            popup.destroy()
            self.load_reviews()

        popup.protocol("WM_DELETE_WINDOW", on_close)

          
         #for review list 
    
    def load_reviews(self):
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

      self.reviewlist.delete(0, tk.END)
      for rev_writer, rev_score, rev_text, rev_date in cursor.fetchall():
          preview_text = rev_text if rev_text else ''
          display_text = f"{rev_writer} ({rev_score}/5): {preview_text}"
          self.reviewlist.insert(tk.END, display_text)
      cursor.close()

      # for average score
      avg_query = "SELECT ROUND(AVG(rev_score),1) FROM review WHERE rev_user = %s"
      cursor = db.execute_query(avg_query, (self.username,))
      if cursor:
        avg_score = cursor.fetchone()[0]
        if avg_score:
            self.ScoreLabel.configure(text=str(avg_score))
            self.StarforScore.configure(text="★")
        else:
            self.ScoreLabel.configure(text="0")
            self.StarforScore.configure(text="☆")
        cursor.close()
      else:
        print("Δεν μπόρεσε να εκτελεστεί το query μέσου όρου.")
        self.ScoreLabel.configure(text="0")
        self.StarforScore.configure(text="☆")

      db.close()


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    window = OtherProfile(top, root, username="george_tsavos", logged_in_user="giwrgos2")
    root.mainloop()




