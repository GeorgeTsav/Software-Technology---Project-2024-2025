import sys
import tkinter as tk
from tkinter.constants import *
import tkinter.ttk as ttk
import os.path
import sqlite3
import mysql.connector
from MessageScreen import MessageScreen
import datetime

_location = os.path.dirname(__file__)


_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

_style_code_ran = 0
def _style_code():
        global _style_code_ran
        if _style_code_ran: return		
        try: MakeAnnouncmentScreen.root.tk.call('source',
                                os.path.join(_location, 'themes', 'default.tcl'))
        except: pass
        style = ttk.Style()
        style.theme_use('default')
        style.configure('.', font = "TkDefaultFont")
        if sys.platform == "win32":
           style.theme_use('winnative')	
        _style_code_ran = 1

class MakeAnnouncmentScreen:
        def __init__(self, top=None, ann_user="unknown"):
                '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''

                top.geometry("200x48+100+100")
                top.minsize(120, 1)
                top.maxsize(1540, 845)
                top.resizable(1,  1)
                top.title("MakeAnnouncmentScreen")
                top.configure(background="#d9d9d9")
                top.configure(highlightbackground="#d9d9d9")
                top.configure(highlightcolor="#000000")

                self.top = top
                self.combobox = tk.StringVar()
                
                self.species_var = tk.StringVar()
                self.announcement_type_var = tk.StringVar()
                self.gender_var = tk.StringVar()
                self.region_var = tk.StringVar()
                self.vaccinated_var = tk.StringVar()

                self.ann_user = ann_user  # Πάρε το username από το instance

                self.MakeAnnouncmentScreen = tk.Frame(self.top)
                self.MakeAnnouncmentScreen.place(relx=0.058, rely=0.091, relheight=0.75, relwidth=0.848)
                self.MakeAnnouncmentScreen.configure(relief='raised')
                self.MakeAnnouncmentScreen.configure(borderwidth="2")
                self.MakeAnnouncmentScreen.configure(relief="raised")
                self.MakeAnnouncmentScreen.configure(background="#ffffff")
                self.MakeAnnouncmentScreen.configure(highlightbackground="#d9d9d9")
                self.MakeAnnouncmentScreen.configure(highlightcolor="#000000")

                _style_code()
                self.TCombobox2 = ttk.Combobox(self.MakeAnnouncmentScreen)
                self.TCombobox2.place(relx=0.204, rely=0.091, relheight=0.058, relwidth=0.162)
                self.value_list = ['DOG','CAT',]
                self.TCombobox2.configure(values=self.value_list)
                self.TCombobox2.configure(font="-family {Segoe UI} -size 9")
                self.TCombobox2.configure(textvariable=self.species_var)

                self.Label1_1_1 = tk.Label(self.MakeAnnouncmentScreen)
                self.Label1_1_1.place(relx=0.067, rely=0.209, height=23, width=81)
                self.Label1_1_1.configure(activebackground="#d9d9d9")
                self.Label1_1_1.configure(activeforeground="black")
                self.Label1_1_1.configure(anchor='w')
                self.Label1_1_1.configure(background="#d9d9d9")
                self.Label1_1_1.configure(disabledforeground="#a3a3a3")
                self.Label1_1_1.configure(font="-family {Segoe UI} -size 9")
                self.Label1_1_1.configure(foreground="#000000")
                self.Label1_1_1.configure(highlightbackground="#d9d9d9")
                self.Label1_1_1.configure(highlightcolor="#000000")
                self.Label1_1_1.configure(relief="groove")
                self.Label1_1_1.configure(text='''Title''')

                self.Text1 = tk.Text(self.MakeAnnouncmentScreen)
                self.Text1.place(relx=0.181, rely=0.215, relheight=0.058, relwidth=0.182)

                self.Text1.configure(background="white")
                self.Text1.configure(font="TkTextFont")
                self.Text1.configure(foreground="black")
                self.Text1.configure(highlightbackground="#d9d9d9")
                self.Text1.configure(highlightcolor="#000000")
                self.Text1.configure(insertbackground="#000000")
                self.Text1.configure(selectbackground="#d9d9d9")
                self.Text1.configure(selectforeground="black")
                self.Text1.configure(setgrid="1")
                self.Text1.configure(wrap="word")

                self.TCombobox1 = ttk.Combobox(self.MakeAnnouncmentScreen)
                self.TCombobox1.place(relx=0.678, rely=0.094, relheight=0.058
                                , relwidth=0.233)
                self.value_list = ['ADOPTION','HOST',]
                self.TCombobox1.configure(values=self.value_list)
                self.TCombobox1.configure(font="-family {Segoe UI} -size 9")
                self.TCombobox1.configure(textvariable=self.announcement_type_var)

                self.Text1_1 = tk.Text(self.MakeAnnouncmentScreen)
                self.Text1_1.place(relx=0.169, rely=0.333, relheight=0.058
                                , relwidth=0.182)
                self.Text1_1.configure(background="white")
                self.Text1_1.configure(font="TkTextFont")
                self.Text1_1.configure(foreground="black")
                self.Text1_1.configure(highlightbackground="#d9d9d9")
                self.Text1_1.configure(highlightcolor="#000000")
                self.Text1_1.configure(insertbackground="#000000")
                self.Text1_1.configure(selectbackground="#d9d9d9")
                self.Text1_1.configure(selectforeground="black")
                self.Text1_1.configure(setgrid="1")
                self.Text1_1.configure(wrap="word")

                self.Label1_1_1_1 = tk.Label(self.MakeAnnouncmentScreen)
                self.Label1_1_1_1.place(relx=0.067, rely=0.333, height=23, width=69)
                self.Label1_1_1_1.configure(activebackground="#d9d9d9")
                self.Label1_1_1_1.configure(activeforeground="black")
                self.Label1_1_1_1.configure(anchor='w')
                self.Label1_1_1_1.configure(background="#d9d9d9")
                self.Label1_1_1_1.configure(disabledforeground="#a3a3a3")
                self.Label1_1_1_1.configure(font="-family {Segoe UI} -size 9")
                self.Label1_1_1_1.configure(foreground="#000000")
                self.Label1_1_1_1.configure(highlightbackground="#d9d9d9")
                self.Label1_1_1_1.configure(highlightcolor="#000000")
                self.Label1_1_1_1.configure(relief="groove")
                self.Label1_1_1_1.configure(text='''AGE''')

                self.Text1_1_1 = tk.Text(self.MakeAnnouncmentScreen)
                self.Text1_1_1.place(relx=0.584, rely=0.333, relheight=0.058
                                , relwidth=0.169)
                self.Text1_1_1.configure(background="white")
                self.Text1_1_1.configure(font="TkTextFont")
                self.Text1_1_1.configure(foreground="black")
                self.Text1_1_1.configure(highlightbackground="#d9d9d9")
                self.Text1_1_1.configure(highlightcolor="#000000")
                self.Text1_1_1.configure(insertbackground="#000000")
                self.Text1_1_1.configure(selectbackground="#d9d9d9")
                self.Text1_1_1.configure(selectforeground="black")
                self.Text1_1_1.configure(setgrid="1")
                self.Text1_1_1.configure(wrap="word")

                self.Label1_2 = tk.Label(self.MakeAnnouncmentScreen)
                self.Label1_2.place(relx=0.444, rely=0.209, height=23, width=92)
                self.Label1_2.configure(activebackground="#d9d9d9")
                self.Label1_2.configure(activeforeground="black")
                self.Label1_2.configure(anchor='w')
                self.Label1_2.configure(background="#d9d9d9")
                self.Label1_2.configure(disabledforeground="#a3a3a3")
                self.Label1_2.configure(font="-family {Segoe UI} -size 9")
                self.Label1_2.configure(foreground="#000000")
                self.Label1_2.configure(highlightbackground="#d9d9d9")
                self.Label1_2.configure(highlightcolor="#000000")
                self.Label1_2.configure(relief="groove")
                self.Label1_2.configure(text='''Gender''')

                self.Text1_1_1_1 = tk.Text(self.MakeAnnouncmentScreen)
                self.Text1_1_1_1.place(relx=0.169, rely=0.452, relheight=0.058
                                , relwidth=0.158)
                self.Text1_1_1_1.configure(background="white")
                self.Text1_1_1_1.configure(font="TkTextFont")
                self.Text1_1_1_1.configure(foreground="black")
                self.Text1_1_1_1.configure(highlightbackground="#d9d9d9")
                self.Text1_1_1_1.configure(highlightcolor="#000000")
                self.Text1_1_1_1.configure(insertbackground="#000000")
                self.Text1_1_1_1.configure(selectbackground="#d9d9d9")
                self.Text1_1_1_1.configure(selectforeground="black")
                self.Text1_1_1_1.configure(setgrid="1")
                self.Text1_1_1_1.configure(wrap="word")

                self.Label1_1_2 = tk.Label(self.MakeAnnouncmentScreen)
                self.Label1_1_2.place(relx=0.446, rely=0.333, height=23, width=99)
                self.Label1_1_2.configure(activebackground="#d9d9d9")
                self.Label1_1_2.configure(activeforeground="black")
                self.Label1_1_2.configure(anchor='w')
                self.Label1_1_2.configure(background="#d9d9d9")
                self.Label1_1_2.configure(disabledforeground="#a3a3a3")
                self.Label1_1_2.configure(font="-family {Segoe UI} -size 9")
                self.Label1_1_2.configure(foreground="#000000")
                self.Label1_1_2.configure(highlightbackground="#d9d9d9")
                self.Label1_1_2.configure(highlightcolor="#000000")
                self.Label1_1_2.configure(relief="groove")
                self.Label1_1_2.configure(text='''NAME (IF EXISTS)''')

                self.TCombobox3 = ttk.Combobox(self.MakeAnnouncmentScreen)
                self.TCombobox3.place(relx=0.575, rely=0.209, relheight=0.058
                                , relwidth=0.165)
                self.value_list = ['MALE','FEMALE',]
                self.TCombobox3.configure(values=self.value_list)
                self.TCombobox3.configure(font="-family {Segoe UI} -size 9")
                self.TCombobox3.configure(textvariable=self.gender_var)

                self.Label1_1 = tk.Label(self.MakeAnnouncmentScreen)
                self.Label1_1.place(relx=0.444, rely=0.091, height=23, width=165)
                self.Label1_1.configure(activebackground="#d9d9d9")
                self.Label1_1.configure(activeforeground="black")
                self.Label1_1.configure(anchor='w')
                self.Label1_1.configure(background="#d9d9d9")
                self.Label1_1.configure(disabledforeground="#a3a3a3")
                self.Label1_1.configure(font="-family {Segoe UI} -size 9")
                self.Label1_1.configure(foreground="#000000")
                self.Label1_1.configure(highlightbackground="#d9d9d9")
                self.Label1_1.configure(highlightcolor="#000000")
                self.Label1_1.configure(relief="groove")
                self.Label1_1.configure(text='''TYPE OF ANNOUNCMENT''')

                self.Label1 = tk.Label(self.MakeAnnouncmentScreen)
                self.Label1.place(relx=0.067, rely=0.091, height=23, width=91)
                self.Label1.configure(activebackground="#d9d9d9")
                self.Label1.configure(activeforeground="black")
                self.Label1.configure(anchor='w')
                self.Label1.configure(background="#d9d9d9")
                self.Label1.configure(disabledforeground="#a3a3a3")
                self.Label1.configure(font="-family {Segoe UI} -size 9")
                self.Label1.configure(foreground="#000000")
                self.Label1.configure(highlightbackground="#d9d9d9")
                self.Label1.configure(highlightcolor="#000000")
                self.Label1.configure(relief="groove")
                self.Label1.configure(text='''SPECIES''')

                self.Button1_1 = tk.Button(self.MakeAnnouncmentScreen)
                self.Button1_1.place(relx=0.458, rely=0.882, height=23, width=60)
                self.Button1_1.configure(activebackground="#d9d9d9")
                self.Button1_1.configure(activeforeground="black")
                self.Button1_1.configure(background="#0080ff")
                self.Button1_1.configure(disabledforeground="#a3a3a3")
                self.Button1_1.configure(font="-family {Segoe UI} -size 9")
                self.Button1_1.configure(foreground="#000000")
                self.Button1_1.configure(highlightbackground="#d9d9d9")
                self.Button1_1.configure(highlightcolor="#000000")
                self.Button1_1.configure(text='''CLEAR ALL''')
                self.Button1_1.configure(command=self.clear_all_fields)

                self.Button1_1_1 = tk.Button(self.MakeAnnouncmentScreen)
                self.Button1_1_1.place(relx=0.554, rely=0.882, height=23, width=60)
                self.Button1_1_1.configure(activebackground="#d9d9d9")
                self.Button1_1_1.configure(activeforeground="black")
                self.Button1_1_1.configure(background="#0080ff")
                self.Button1_1_1.configure(disabledforeground="#a3a3a3")
                self.Button1_1_1.configure(font="-family {Segoe UI} -size 9")
                self.Button1_1_1.configure(foreground="#000000")
                self.Button1_1_1.configure(highlightbackground="#d9d9d9")
                self.Button1_1_1.configure(highlightcolor="#000000")
                self.Button1_1_1.configure(text='''BACK''')
                self.Button1_1_1.configure(command=self.go_back)

                self.Button1 = tk.Button(self.MakeAnnouncmentScreen)
                self.Button1.place(relx=0.361, rely=0.882, height=23, width=60)
                self.Button1.configure(activebackground="#d9d9d9")
                self.Button1.configure(activeforeground="black")
                self.Button1.configure(background="#0080ff")
                self.Button1.configure(disabledforeground="#a3a3a3")
                self.Button1.configure(font="-family {Segoe UI} -size 9")
                self.Button1.configure(foreground="#000000")
                self.Button1.configure(highlightbackground="#d9d9d9")
                self.Button1.configure(highlightcolor="#000000")
                self.Button1.configure(text='''UPLOAD''')
                self.Button1.configure(command=self.upload_to_db)

                self.TCombobox3_2 = ttk.Combobox(self.MakeAnnouncmentScreen)
                self.TCombobox3_2.place(relx=0.547, rely=0.573, relheight=0.058
                                , relwidth=0.111)
                self.value_list = ['YES','NO',]
                self.TCombobox3_2.configure(values=self.value_list)
                self.TCombobox3_2.configure(font="-family {Segoe UI} -size 9")
                self.TCombobox3_2.configure(textvariable=self.vaccinated_var)

                self.Label1_2_1_1 = tk.Label(self.MakeAnnouncmentScreen)
                self.Label1_2_1_1.place(relx=0.446, rely=0.57, height=23, width=69)
                self.Label1_2_1_1.configure(activebackground="#d9d9d9")
                self.Label1_2_1_1.configure(activeforeground="black")
                self.Label1_2_1_1.configure(anchor='w')
                self.Label1_2_1_1.configure(background="#d9d9d9")
                self.Label1_2_1_1.configure(disabledforeground="#a3a3a3")
                self.Label1_2_1_1.configure(font="-family {Segoe UI} -size 9")
                self.Label1_2_1_1.configure(foreground="#000000")
                self.Label1_2_1_1.configure(highlightbackground="#d9d9d9")
                self.Label1_2_1_1.configure(highlightcolor="#000000")
                self.Label1_2_1_1.configure(relief="groove")
                self.Label1_2_1_1.configure(text='''VACCINATED''')

                self.TCombobox3_1 = ttk.Combobox(self.MakeAnnouncmentScreen)
                self.TCombobox3_1.place(relx=0.547, rely=0.452, relheight=0.058
                                , relwidth=0.166)
                self.value_list = ['ATHENS,GREECE','PATRA,GREECE','TRIKALA,GREECE','THESALLONIKH,GREECE',]
                self.TCombobox3_1.configure(values=self.value_list)
                self.TCombobox3_1.configure(font="-family {Segoe UI} -size 9")
                self.TCombobox3_1.configure(textvariable=self.region_var)

                self.Label1_1_1_1_1_1 = tk.Label(self.MakeAnnouncmentScreen)
                self.Label1_1_1_1_1_1.place(relx=0.444, rely=0.452, height=23, width=69)
                self.Label1_1_1_1_1_1.configure(activebackground="#d9d9d9")
                self.Label1_1_1_1_1_1.configure(activeforeground="black")
                self.Label1_1_1_1_1_1.configure(anchor='w')
                self.Label1_1_1_1_1_1.configure(background="#d9d9d9")
                self.Label1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
                self.Label1_1_1_1_1_1.configure(font="-family {Segoe UI} -size 9")
                self.Label1_1_1_1_1_1.configure(foreground="#000000")
                self.Label1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
                self.Label1_1_1_1_1_1.configure(highlightcolor="#000000")
                self.Label1_1_1_1_1_1.configure(relief="groove")
                self.Label1_1_1_1_1_1.configure(text='''REGION''')

                self.Text1_1_1_1_1 = tk.Text(self.MakeAnnouncmentScreen)
                self.Text1_1_1_1_1.place(relx=0.169, rely=0.57, relheight=0.058
                                , relwidth=0.147)
                self.Text1_1_1_1_1.configure(background="white")
                self.Text1_1_1_1_1.configure(font="TkTextFont")
                self.Text1_1_1_1_1.configure(foreground="black")
                self.Text1_1_1_1_1.configure(highlightbackground="#d9d9d9")
                self.Text1_1_1_1_1.configure(highlightcolor="#000000")
                self.Text1_1_1_1_1.configure(insertbackground="#000000")
                self.Text1_1_1_1_1.configure(selectbackground="#d9d9d9")
                self.Text1_1_1_1_1.configure(selectforeground="black")
                self.Text1_1_1_1_1.configure(setgrid="1")
                self.Text1_1_1_1_1.configure(wrap="word")

                self.Label1_1_1_1_1 = tk.Label(self.MakeAnnouncmentScreen)
                self.Label1_1_1_1_1.place(relx=0.067, rely=0.452, height=23, width=68)
                self.Label1_1_1_1_1.configure(activebackground="#d9d9d9")
                self.Label1_1_1_1_1.configure(activeforeground="black")
                self.Label1_1_1_1_1.configure(anchor='w')
                self.Label1_1_1_1_1.configure(background="#d9d9d9")
                self.Label1_1_1_1_1.configure(disabledforeground="#a3a3a3")
                self.Label1_1_1_1_1.configure(font="-family {Segoe UI} -size 9")
                self.Label1_1_1_1_1.configure(foreground="#000000")
                self.Label1_1_1_1_1.configure(highlightbackground="#d9d9d9")
                self.Label1_1_1_1_1.configure(highlightcolor="#000000")
                self.Label1_1_1_1_1.configure(relief="groove")
                self.Label1_1_1_1_1.configure(text='''BREED''')

                self.Label1_2_1 = tk.Label(self.MakeAnnouncmentScreen)
                self.Label1_2_1.place(relx=0.067, rely=0.573, height=23, width=69)
                self.Label1_2_1.configure(activebackground="#d9d9d9")
                self.Label1_2_1.configure(activeforeground="black")
                self.Label1_2_1.configure(anchor='w')
                self.Label1_2_1.configure(background="#d9d9d9")
                self.Label1_2_1.configure(disabledforeground="#a3a3a3")
                self.Label1_2_1.configure(font="-family {Segoe UI} -size 9")
                self.Label1_2_1.configure(foreground="#000000")
                self.Label1_2_1.configure(highlightbackground="#d9d9d9")
                self.Label1_2_1.configure(highlightcolor="#000000")
                self.Label1_2_1.configure(relief="groove")
                self.Label1_2_1.configure(text='''CONTACT''')

                self.Text1_1_1_1_1_1 = tk.Text(self.MakeAnnouncmentScreen)
                self.Text1_1_1_1_1_1.place(relx=0.288, rely=0.691, relheight=0.058
                                , relwidth=0.148)
                self.Text1_1_1_1_1_1.configure(background="white")
                self.Text1_1_1_1_1_1.configure(font="TkTextFont")
                self.Text1_1_1_1_1_1.configure(foreground="black")
                self.Text1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
                self.Text1_1_1_1_1_1.configure(highlightcolor="#000000")
                self.Text1_1_1_1_1_1.configure(insertbackground="#000000")
                self.Text1_1_1_1_1_1.configure(selectbackground="#d9d9d9")
                self.Text1_1_1_1_1_1.configure(selectforeground="black")
                self.Text1_1_1_1_1_1.configure(setgrid="1")
                self.Text1_1_1_1_1_1.configure(wrap="word")

                # Host Start Date Label
                self.Label_host_start = tk.Label(self.MakeAnnouncmentScreen)
                self.Label_host_start.place(relx=0.067, rely=0.691, height=23, width=120)
                self.Label_host_start.configure(activebackground="#d9d9d9")
                self.Label_host_start.configure(activeforeground="black")
                self.Label_host_start.configure(anchor='w')
                self.Label_host_start.configure(background="#d9d9d9")
                self.Label_host_start.configure(disabledforeground="#a3a3a3")
                self.Label_host_start.configure(font="-family {Segoe UI} -size 9")
                self.Label_host_start.configure(foreground="#000000")
                self.Label_host_start.configure(highlightbackground="#d9d9d9")
                self.Label_host_start.configure(highlightcolor="#000000")
                self.Label_host_start.configure(relief="groove")
                self.Label_host_start.configure(text='''Host Start Date (YYYY-MM-DD)''')

                self.Text_host_start = tk.Text(self.MakeAnnouncmentScreen)
                self.Text_host_start.place(relx=0.288, rely=0.691, relheight=0.058, relwidth=0.148)
                self.Text_host_start.configure(background="white")
                self.Text_host_start.configure(font="TkTextFont")
                self.Text_host_start.configure(foreground="black")
                self.Text_host_start.configure(highlightbackground="#d9d9d9")
                self.Text_host_start.configure(highlightcolor="#000000")
                self.Text_host_start.configure(insertbackground="#000000")
                self.Text_host_start.configure(selectbackground="#d9d9d9")
                self.Text_host_start.configure(selectforeground="black")
                self.Text_host_start.configure(setgrid="1")
                self.Text_host_start.configure(wrap="word")

                # Host End Date Label
                self.Label_host_end = tk.Label(self.MakeAnnouncmentScreen)
                self.Label_host_end.place(relx=0.067, rely=0.76, height=23, width=120)
                self.Label_host_end.configure(activebackground="#d9d9d9")
                self.Label_host_end.configure(activeforeground="black")
                self.Label_host_end.configure(anchor='w')
                self.Label_host_end.configure(background="#d9d9d9")
                self.Label_host_end.configure(disabledforeground="#a3a3a3")
                self.Label_host_end.configure(font="-family {Segoe UI} -size 9")
                self.Label_host_end.configure(foreground="#000000")
                self.Label_host_end.configure(highlightbackground="#d9d9d9")
                self.Label_host_end.configure(highlightcolor="#000000")
                self.Label_host_end.configure(relief="groove")
                self.Label_host_end.configure(text='''Host End Date (YYYY-MM-DD)''')

                self.Text_host_end = tk.Text(self.MakeAnnouncmentScreen)
                self.Text_host_end.place(relx=0.288, rely=0.76, relheight=0.058, relwidth=0.148)
                self.Text_host_end.configure(background="white")
                self.Text_host_end.configure(font="TkTextFont")
                self.Text_host_end.configure(foreground="black")
                self.Text_host_end.configure(highlightbackground="#d9d9d9")
                self.Text_host_end.configure(highlightcolor="#000000")
                self.Text_host_end.configure(insertbackground="#000000")
                self.Text_host_end.configure(selectbackground="#d9d9d9")
                self.Text_host_end.configure(selectforeground="black")
                self.Text_host_end.configure(setgrid="1")
                self.Text_host_end.configure(wrap="word")

                # After creating self.TCombobox1 (announcement type combobox)
                self.TCombobox1.bind("<<ComboboxSelected>>", self.on_type_change)
                self.on_type_change()  # Set initial state

        def clear_all_fields(self):
            # Clear all StringVars (comboboxes)
            self.species_var.set("")
            self.announcement_type_var.set("")
            self.gender_var.set("")
            self.region_var.set("")
            self.vaccinated_var.set("")
            # Clear all Text widgets
            self.Text1.delete("1.0", tk.END)
            self.Text1_1.delete("1.0", tk.END)
            self.Text1_1_1.delete("1.0", tk.END)
            self.Text1_1_1_1.delete("1.0", tk.END)
            self.Text1_1_1_1_1.delete("1.0", tk.END)
            self.Text1_1_1_1_1_1.delete("1.0", tk.END)

        def go_back(self):
            self.top.destroy()

        def on_type_change(self, event=None):
            ann_type = self.announcement_type_var.get().strip()
            if ann_type == "HOST":
                self.Text_host_start.config(state="normal")
                self.Text_host_end.config(state="normal")
            else:
                self.Text_host_start.delete("1.0", tk.END)
                self.Text_host_end.delete("1.0", tk.END)
                self.Text_host_start.config(state="disabled")
                self.Text_host_end.config(state="disabled")

        def upload_to_db(self):
            # Collect data from widgets
            ann_title = self.Text1.get("1.0", "end").strip()
            ann_type = self.announcement_type_var.get().strip()
            ann_species = self.species_var.get().strip()
            ann_gender = self.gender_var.get().strip()
            ann_region = self.region_var.get().strip()
            ann_vaccin = self.vaccinated_var.get().strip()
            ann_age = self.Text1_1.get("1.0", "end").strip()
            ann_conntact = self.Text1_1_1_1_1.get("1.0", "end").strip()
            adopt_description = self.Text1_1_1_1.get("1.0", "end").strip()
            ann_user = self.ann_user.strip()
            host_start_date = self.Text_host_start.get("1.0", "end").strip()
            host_end_date = self.Text_host_end.get("1.0", "end").strip()

            # Check if any required field is empty (host_start_date and host_end_date are optional)
            if not all([ann_title, ann_type, ann_species, ann_gender, ann_region, ann_vaccin, ann_age, ann_conntact, ann_user]):
                msg_screen = MessageScreen()
                msg_screen.display("invalid action please fill up all the fields")
                return

            # Validate age: must be an integer from 1 to 10
            try:
                age_int = int(ann_age)
                if not (1 <= age_int <= 10):
                    raise ValueError
            except ValueError:
                msg_screen = MessageScreen()
                msg_screen.display("invalid age: must be an integer from 1 to 10")
                return

            # Validate contact field: must be 10 digits, no spaces, only numbers
            if not (ann_conntact.isdigit() and len(ann_conntact) == 10):
                msg_screen = MessageScreen()
                msg_screen.display("invalid contact info")
                return

            # Validate host_start_date and host_end_date (optional, only if filled)
            import datetime
            for date_val, label in [(host_start_date, "Host Start Date"), (host_end_date, "Host End Date")]:
                if date_val:
                    try:
                        datetime.datetime.strptime(date_val, "%Y-%m-%d")
                    except ValueError:
                        msg_screen = MessageScreen()
                        msg_screen.display(f"{label} must be in YYYY-MM-DD format")
                        return

            # Connect to the database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="petato_db"
            )
            cursor = conn.cursor()

            # Insert data (adapted for your table)
            cursor.execute("""
                INSERT INTO announcements 
                (ann_title, ann_type, ann_species, ann_gender, ann_region, ann_vaccin, ann_age, ann_conntact, adopt_description, host_start_date, host_end_date, ann_user)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                ann_title, ann_type, ann_species, ann_gender, ann_region, ann_vaccin,
                age_int, ann_conntact, adopt_description or None,
                host_start_date or None, host_end_date or None, ann_user
            ))

            conn.commit()
            conn.close()

            self.clear_all_fields()
            tk.messagebox.showinfo("Success", "Announcement uploaded!")

def start_up():
        MakeAnnouncmentScreen.MakeAnnouncmentScreen.main()

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    window = MakeAnnouncmentScreen(top)
    root.mainloop()