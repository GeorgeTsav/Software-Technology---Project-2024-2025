import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

import DBManager
import MessageScreen

_location = os.path.dirname(__file__)

_debug = True

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black'
_tabfg2 = 'white'
_bgmode = 'light'
_tabbg1 = '#d9d9d9'
_tabbg2 = 'gray40'


class ReviewScreen:
    def __init__(self, top=None, username=None, logged_in_user=None):
        self.top = top
        self.username = username 
        self.logged_in_user = logged_in_user 

        self.top.geometry("680x464+485+82")
        self.top.minsize(120, 1)
        self.top.maxsize(1540, 845)
        self.top.resizable(1,  1)
        self.top.title("Petato")
        self.top.configure(background="#c0c0c0")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="#0000ff")

        self.menubar = tk.Menu(self.top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        self.top.configure(menu=self.menubar)

        self.reviewscreenframe = tk.Frame(self.top)
        self.reviewscreenframe.place(relx=0.018, rely=0.022, relheight=0.966
                , relwidth=0.957)
        self.reviewscreenframe.configure(relief='groove')
        self.reviewscreenframe.configure(borderwidth="2")
        self.reviewscreenframe.configure(relief="groove")
        self.reviewscreenframe.configure(background="#c0c0c0")
        self.reviewscreenframe.configure(highlightbackground="#d9d9d9")
        self.reviewscreenframe.configure(highlightcolor="#000000")


        #count for the stars submitted
        self.selected_stars = 0

        self.insertstar1 = ttk.Button(self.reviewscreenframe)
        self.insertstar1.place(relx=0.553, rely=0.324, height=26, width=25)
        self.insertstar1.configure(text='''Tbutton''')
        self.insertstar1.configure(text='☆')
        self.insertstar1.configure(compound='left')
        self.insertstar1.configure(command=lambda: self.set_stars(1))

        self.insertstar2 = ttk.Button(self.reviewscreenframe)
        self.insertstar2.place(relx=0.63, rely=0.324, height=26, width=25)
        self.insertstar2.configure(text='''Tbutton''')
        self.insertstar2.configure(text='☆')
        self.insertstar2.configure(compound='left')
        self.insertstar2.configure(command=lambda: self.set_stars(2))

        self.insertstar3 = ttk.Button(self.reviewscreenframe)
        self.insertstar3.place(relx=0.722, rely=0.324, height=26, width=25)
        self.insertstar3.configure(text='''Tbutton''')
        self.insertstar3.configure(text='☆')
        self.insertstar3.configure(compound='left')
        self.insertstar3.configure(command=lambda: self.set_stars(3))

        self.insertstar4 = ttk.Button(self.reviewscreenframe)
        self.insertstar4.place(relx=0.799, rely=0.324, height=26, width=25)
        self.insertstar4.configure(text='''Tbutton''')
        self.insertstar4.configure(text='☆')
        self.insertstar4.configure(compound='left')
        self.insertstar4.configure(command=lambda: self.set_stars(4))

        self.insertstar5 = ttk.Button(self.reviewscreenframe)
        self.insertstar5.place(relx=0.891, rely=0.324, height=26, width=25)
        self.insertstar5.configure(text='''Tbutton''')
        self.insertstar5.configure(text='☆')
        self.insertstar5.configure(compound='left')
        self.insertstar5.configure(command=lambda: self.set_stars(5))

        self.reviews = tk.Label(self.reviewscreenframe)
        self.reviews.place(relx=0.43, rely=0.107, height=29, width=91)
        self.reviews.configure(activebackground="#d9d9d9")
        self.reviews.configure(activeforeground="black")
        self.reviews.configure(background="#d9d9d9")
        self.reviews.configure(compound='left')
        self.reviews.configure(disabledforeground="#a3a3a3")
        self.reviews.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.reviews.configure(foreground="#000000")
        self.reviews.configure(highlightbackground="#d9d9d9")
        self.reviews.configure(highlightcolor="#000000")
        self.reviews.configure(text='''Reviews''')

        self.Reviewtext = tk.Text(self.reviewscreenframe)
        self.Reviewtext.place(relx=0.108, rely=0.248, relheight=0.397
                , relwidth=0.359)
        self.Reviewtext.configure(background="white")
        self.Reviewtext.configure(font="TkTextFont")
        self.Reviewtext.configure(foreground="black")
        self.Reviewtext.configure(highlightbackground="#d9d9d9")
        self.Reviewtext.configure(highlightcolor="#000000")
        self.Reviewtext.configure(insertbackground="#000000")
        self.Reviewtext.configure(selectbackground="#d9d9d9")
        self.Reviewtext.configure(selectforeground="black")
        self.Reviewtext.configure(wrap="word")

        self.addreviewbutton = tk.Button(self.reviewscreenframe)
        self.addreviewbutton.place(relx=0.645, rely=0.493, height=36, width=87)
        self.addreviewbutton.configure(activebackground="#d9d9d9")
        self.addreviewbutton.configure(activeforeground="black")
        self.addreviewbutton.configure(background="#0080c0")
        self.addreviewbutton.configure(disabledforeground="#a3a3a3")
        self.addreviewbutton.configure(font="-family {Segoe UI} -size 9")
        self.addreviewbutton.configure(foreground="#ffffff")
        self.addreviewbutton.configure(highlightbackground="#d9d9d9")
        self.addreviewbutton.configure(highlightcolor="#000000")
        self.addreviewbutton.configure(text='''Add Review''')
        self.addreviewbutton.configure(command=self.add_review)

    def set_stars(self, stars):
        self.selected_stars = stars

        # list of star buttons
        star_buttons = [
            self.insertstar1,
            self.insertstar2,
            self.insertstar3,
            self.insertstar4,
            self.insertstar5
        ]

        # make rating visible
        for i in range(5):
            if i < stars:
                star_buttons[i].configure(text='★')  # empty stars showing the stars submitted
            else:
                star_buttons[i].configure(text='☆')  # full star showing the remaining stars

   # check if the user has submitted stars and review doen not surpass 100 words. then add to DB
    def add_review(self):
        review_text = self.Reviewtext.get("1.0", tk.END).strip()

        if len(review_text.split()) > 100:
            MessageScreen.MessageScreen().display("The review cannot exceed 100 words.")
            return

        if self.selected_stars == 0:
            MessageScreen.MessageScreen().display("Please select stars before adding the review.")
            return

        rev_writer = self.logged_in_user  # username of the user making the review
        rev_user = self.username # username of the user accepting the review

        db = DBManager.DBManager(host='localhost', user='root', password='', database='petato_db')
        db.connect()
        success = db.add_review(review_text, str(self.selected_stars), rev_writer, rev_user)
        db.close()

        # if everything done correctly reset text and stars
        if success:
            MessageScreen.MessageScreen().display("The review was added successfully!")
            self.Reviewtext.delete("1.0", tk.END)
            self.set_stars(0)
        else:
            MessageScreen.MessageScreen().display("An error occurred while saving the review.")



if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    window = ReviewScreen(top, username="george_tsavos", logged_in_user="sof")
    root.mainloop()




