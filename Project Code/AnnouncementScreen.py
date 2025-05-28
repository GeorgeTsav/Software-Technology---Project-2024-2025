import sys
import tkinter as tk
from tkinter.constants import *
from MakeAnnouncementScreen import MakeAnnouncementScreen

import tkinter.ttk as ttk
import os.path

_location = os.path.dirname(__file__)


_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class AnnouncementScreen:
    def __init__(self, top=None, ann_user="unknown"):

        top.geometry("600x450+440+233")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Petato")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.ann_user = ann_user

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=-0.017, rely=0.0, relheight=0.989, relwidth=1.008)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#000000")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.397, rely=0.427, height=21, width=104)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 9")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(text='''Select an option''')

        self.Button1_1_1 = tk.Button(self.Frame1)
        self.Button1_1_1.place(relx=0.248, rely=0.022, height=26, width=157)
        self.Button1_1_1.configure(activebackground="#d9d9d9")
        self.Button1_1_1.configure(activeforeground="black")
        self.Button1_1_1.configure(background="#0080ff")
        self.Button1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1_1.configure(font="-family {Segoe UI} -size 9")
        self.Button1_1_1.configure(foreground="#000000")
        self.Button1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1_1.configure(highlightcolor="#000000")
        self.Button1_1_1.configure(text='''Announcements''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.347, rely=0.517, height=26, width=157)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 9")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='''Make an Announcement''')
        self.Button1.configure(command=self.open_make_announcement_screen)

        self.Button1_2 = tk.Button(self.Frame1)
        self.Button1_2.place(relx=0.512, rely=0.022, height=26, width=157)
        self.Button1_2.configure(activebackground="#d9d9d9")
        self.Button1_2.configure(activeforeground="black")
        self.Button1_2.configure(background="#ffffff")
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(font="-family {Segoe UI} -size 9")
        self.Button1_2.configure(foreground="#000000")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="#000000")
        self.Button1_2.configure(text='''Make an Appointment''')

        self.Button1_1 = tk.Button(self.Frame1)
        self.Button1_1.place(relx=0.347, rely=0.607, height=26, width=157)
        self.Button1_1.configure(activebackground="#d9d9d9")
        self.Button1_1.configure(activeforeground="black")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family {Segoe UI} -size 9")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="#000000")
        self.Button1_1.configure(text='''Announcements''')

        self.Button1_1_2 = tk.Button(self.Frame1)
        self.Button1_1_2.place(relx=0.033, rely=0.022, height=26, width=127)
        self.Button1_1_2.configure(activebackground="#d9d9d9")
        self.Button1_1_2.configure(activeforeground="black")
        self.Button1_1_2.configure(background="#ffffff")
        self.Button1_1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_1_2.configure(font="-family {Segoe UI} -size 9")
        self.Button1_1_2.configure(foreground="#000000")
        self.Button1_1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_1_2.configure(highlightcolor="#000000")
        self.Button1_1_2.configure(text='''My Profile''')

        self.Button1_1_2_1 = tk.Button(self.Frame1)
        self.Button1_1_2_1.place(relx=0.777, rely=0.022, height=26, width=117)
        self.Button1_1_2_1.configure(activebackground="#d9d9d9")
        self.Button1_1_2_1.configure(activeforeground="black")
        self.Button1_1_2_1.configure(background="#ffff00")
        self.Button1_1_2_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1_2_1.configure(font="-family {Segoe UI} -size 9")
        self.Button1_1_2_1.configure(foreground="#000000")
        self.Button1_1_2_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1_2_1.configure(highlightcolor="#000000")
        self.Button1_1_2_1.configure(text='''e-shop''')

    def open_make_announcement_screen(self):
        try:
            from MakeAnnouncementScreen import MakeAnnouncmentScreen
        except ImportError:
            import tkinter.messagebox as msg
            msg.showerror("Error", "MakeAnnouncementScreen module not found.")
            return
        top = tk.Toplevel(self.top)
        MakeAnnouncementScreen(top, ann_user=self.ann_user)

def start_up():
    AnnouncementScreen.AnnouncmentScreen.main()

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    window = AnnouncementScreen(top)
    root.mainloop()