import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from PIL import Image, ImageTk
import os.path

_location = os.path.dirname(__file__)
_debug = True

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class MainMenuScreen:
    def __init__(self, top=None, root=None, username=None):
        self.username = username
        self.root = root

        top.geometry("693x474+429+128")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Petato")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top

        self.MenuBarFrame = tk.Frame(self.top)
        self.MenuBarFrame.place(relx=0.014, rely=0.021, relheight=0.186, relwidth=0.973)
        self.MenuBarFrame.configure(relief='groove')
        self.MenuBarFrame.configure(borderwidth="2")
        self.MenuBarFrame.configure(relief="groove")
        self.MenuBarFrame.configure(background="#d9d9d9")
        self.MenuBarFrame.configure(highlightbackground="#d9d9d9")
        self.MenuBarFrame.configure(highlightcolor="#000000")

        self.MakeApointmenetButton = tk.Button(self.MenuBarFrame)
        self.MakeApointmenetButton.place(relx=0.527, rely=0.295, height=26
                , width=137)
        self.MakeApointmenetButton.configure(activebackground="#0080ff")
        self.MakeApointmenetButton.configure(activeforeground="black")
        self.MakeApointmenetButton.configure(background="#d9d9d9")
        self.MakeApointmenetButton.configure(disabledforeground="#a3a3a3")
        self.MakeApointmenetButton.configure(font="-family {Segoe UI} -size 9")
        self.MakeApointmenetButton.configure(foreground="#000000")
        self.MakeApointmenetButton.configure(highlightbackground="#d9d9d9")
        self.MakeApointmenetButton.configure(highlightcolor="#000000")
        self.MakeApointmenetButton.configure(text='''Make an Apointment''')

        self.AnnouncementsButton = tk.Button(self.MenuBarFrame)
        self.AnnouncementsButton.place(relx=0.271, rely=0.295, height=26
                , width=97)
        self.AnnouncementsButton.configure(activebackground="#0080ff")
        self.AnnouncementsButton.configure(activeforeground="black")
        self.AnnouncementsButton.configure(background="#d9d9d9")
        self.AnnouncementsButton.configure(disabledforeground="#a3a3a3")
        self.AnnouncementsButton.configure(font="-family {Segoe UI} -size 9")
        self.AnnouncementsButton.configure(foreground="#000000")
        self.AnnouncementsButton.configure(highlightbackground="#d9d9d9")
        self.AnnouncementsButton.configure(highlightcolor="#000000")
        self.AnnouncementsButton.configure(text='''Announcements''')

        self.eshopButton = tk.Button(self.MenuBarFrame)
        self.eshopButton.place(relx=0.843, rely=0.295, height=26, width=47)
        self.eshopButton.configure(activebackground="#0080ff")
        self.eshopButton.configure(activeforeground="black")
        self.eshopButton.configure(background="#ffff00")
        self.eshopButton.configure(disabledforeground="#a3a3a3")
        self.eshopButton.configure(font="-family {Segoe UI} -size 9")
        self.eshopButton.configure(foreground="black")
        self.eshopButton.configure(highlightbackground="#d9d9d9")
        self.eshopButton.configure(highlightcolor="#000000")
        self.eshopButton.configure(text='''e-shop''')

        self.MyProfileButton = tk.Button(self.MenuBarFrame)
        self.MyProfileButton.place(relx=0.075, rely=0.295, height=26, width=65)
        self.MyProfileButton.configure(activebackground="#0080ff")
        self.MyProfileButton.configure(activeforeground="black")
        self.MyProfileButton.configure(background="#d9d9d9")
        self.MyProfileButton.configure(disabledforeground="#a3a3a3")
        self.MyProfileButton.configure(font="-family {Segoe UI} -size 9")
        self.MyProfileButton.configure(foreground="#000000")
        self.MyProfileButton.configure(highlightbackground="#d9d9d9")
        self.MyProfileButton.configure(highlightcolor="#000000")
        self.MyProfileButton.configure(text='''My Profile''')

        self.AppLogoFrame = tk.Frame(self.top)
        self.AppLogoFrame.place(relx=0.014, rely=0.232, relheight=0.728
                , relwidth=0.973)
        self.AppLogoFrame.configure(relief='groove')
        self.AppLogoFrame.configure(relief="groove")
        self.AppLogoFrame.configure(background="#ffffff")
        self.AppLogoFrame.configure(highlightbackground="#ffffff")
        self.AppLogoFrame.configure(highlightcolor="#000000")

        self.AppLogo = tk.Label(self.AppLogoFrame)
        self.AppLogo.configure(activebackground="#ffffff")
        self.AppLogo.configure(activeforeground="#ffffff")
        self.AppLogo.configure(anchor='center')
        self.AppLogo.configure(background="#ffffff")
        self.AppLogo.configure(compound='left')
        self.AppLogo.configure(disabledforeground="#ffffff")
        self.AppLogo.configure(foreground="#ffffff")
        self.AppLogo.configure(highlightbackground="#ffffff")
        self.AppLogo.configure(highlightcolor="#ffffff")
        photo_location = os.path.join(_location,"./images/ProjectLogo.png")
        global _img0
        img = Image.open(photo_location)
        img = img.resize((500, 500), Image.LANCZOS)
        _img0 = ImageTk.PhotoImage(img)
        self.AppLogo.configure(image=_img0)
        self.AppLogo.configure(justify='center')
        self.AppLogo.pack(expand=True, anchor='center')

    #Σβήνει το προηγούμενο παράθυρο και εμφανίζει το νέο
    def display(self, previous_window=None):
        if previous_window is not None:
            previous_window.destroy()
        self.top.deiconify()

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    window = MainMenuScreen(top, root)
    root.mainloop()




