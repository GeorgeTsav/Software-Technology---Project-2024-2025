import sys
import tkinter as tk
from tkinter.constants import *
import tkinter.ttk as ttk
import os.path

import MainMenuScreen
import AnnouncementsScreen
import MakeAnnouncementScreen

_location = os.path.dirname(__file__)
_debug = True

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class Make_Search_Announcemnts_Screen:
    def __init__(self, top=None, root=None, username=None):
        self.top = top
        self.root = root
        self.username = username
        
        self.top.geometry("600x450+468+138")
        self.top.minsize(120, 1)
        self.top.maxsize(1540, 845)
        self.top.resizable(0, 0)
        self.top.title("Petato")
        self.top.configure(background="#d9d9d9")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="#000000")

        self.menubar = tk.Menu(self.top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        self.top.configure(menu = self.menubar)

        self.Make_Search_Frame = tk.Frame(self.top)
        self.Make_Search_Frame.place(relx=0.033, rely=0.044, relheight=0.9, relwidth=0.942)
        self.Make_Search_Frame.configure(relief='groove')
        self.Make_Search_Frame.configure(borderwidth="2")
        self.Make_Search_Frame.configure(relief="groove")
        self.Make_Search_Frame.configure(background="#ffffff")
        self.Make_Search_Frame.configure(highlightbackground="#d9d9d9")
        self.Make_Search_Frame.configure(highlightcolor="#000000")

        self.Make_Search_Label = tk.Label(self.Make_Search_Frame)
        self.Make_Search_Label.place(relx=0.23, rely=0.123, height=51, width=334)

        self.Make_Search_Label.configure(activebackground="#ffffff")
        self.Make_Search_Label.configure(activeforeground="black")
        self.Make_Search_Label.configure(anchor='w')
        self.Make_Search_Label.configure(background="#ffffff")
        self.Make_Search_Label.configure(compound='left')
        self.Make_Search_Label.configure(disabledforeground="#a3a3a3")
        self.Make_Search_Label.configure(font="-family {Segoe UI} -size 28 -weight bold -underline 1")
        self.Make_Search_Label.configure(foreground="#000000")
        self.Make_Search_Label.configure(highlightbackground="#d9d9d9")
        self.Make_Search_Label.configure(highlightcolor="#000000")
        self.Make_Search_Label.configure(text='''Choose an Option:''')

        self.Make_Ann_Button = tk.Button(self.Make_Search_Frame)
        self.Make_Ann_Button.place(relx=0.319, rely=0.321, height=46, width=227)
        self.Make_Ann_Button.configure(activebackground="#0080ff")
        self.Make_Ann_Button.configure(activeforeground="black")
        self.Make_Ann_Button.configure(background="#ffffff")
        self.Make_Ann_Button.configure(borderwidth="4")
        self.Make_Ann_Button.configure(disabledforeground="#a3a3a3")
        self.Make_Ann_Button.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Make_Ann_Button.configure(foreground="#000000")
        self.Make_Ann_Button.configure(highlightbackground="#d9d9d9")
        self.Make_Ann_Button.configure(highlightcolor="#000000")
        self.Make_Ann_Button.configure(text='''Make an Announcemnt''')
        self.Make_Ann_Button.configure(command=self.openMakeAnnouncemntScreen)

        self.Search_Ann_Button = tk.Button(self.Make_Search_Frame)
        self.Search_Ann_Button.place(relx=0.372, rely=0.494, height=46, width=177)
        self.Search_Ann_Button.configure(activebackground="#0080ff")
        self.Search_Ann_Button.configure(activeforeground="black")
        self.Search_Ann_Button.configure(background="#d9d9d9")
        self.Search_Ann_Button.configure(disabledforeground="#a3a3a3")
        self.Search_Ann_Button.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Search_Ann_Button.configure(foreground="#000000")
        self.Search_Ann_Button.configure(highlightbackground="#d9d9d9")
        self.Search_Ann_Button.configure(highlightcolor="#000000")
        self.Search_Ann_Button.configure(text='''Announcemnts''')
        self.Search_Ann_Button.configure(command=self.openAnnouncementsScreen)

        self.BackButton = tk.Button(self.Make_Search_Frame)
        self.BackButton.place(relx=0.442, rely=0.667, height=36, width=97)
        self.BackButton.configure(activebackground="#0080ff")
        self.BackButton.configure(activeforeground="black")
        self.BackButton.configure(background="#d9d9d9")
        self.BackButton.configure(disabledforeground="#a3a3a3")
        self.BackButton.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.BackButton.configure(foreground="#000000")
        self.BackButton.configure(highlightbackground="#d9d9d9")
        self.BackButton.configure(highlightcolor="#000000")
        self.BackButton.configure(text='''Back''')
        self.BackButton.configure(command=self.go_back)

    def display(self, previous_window=None):
        if previous_window is not None:
            previous_window.destroy()
        self.top.deiconify()

    def openAnnouncementsScreen(self):
        new_top = tk.Toplevel(self.root)
        new_top.protocol('WM_DELETE_WINDOW', self.root.destroy)
        AnnouncementsScreen.AnnouncementsScreen(new_top, self.root, self.username).display(self.top)

    def openMakeAnnouncemntScreen(self):
        new_top = tk.Toplevel(self.root)
        new_top.protocol('WM_DELETE_WINDOW', self.root.destroy)
        MakeAnnouncementScreen.MakeAnnouncementScreen(new_top, self.root, self.username).display(self.top)

    def go_back(self):
        new_top = tk.Toplevel(self.root)
        new_top.protocol('WM_DELETE_WINDOW', self.root.destroy)
        MainMenuScreen.MainMenuScreen(new_top, self.root, self.username).display(self.top)



if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    window = Make_Search_Announcemnts_Screen(top, root, username="george_tsavos")
    root.mainloop()
