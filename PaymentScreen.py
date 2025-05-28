import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import DBManager
import eshopScreen

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class PaymentScreen:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Petato")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#c0c0c0")

        self.top = top

        self.paymentframe = tk.Frame(self.top)
        self.paymentframe.place(relx=0.033, rely=0.044, relheight=0.9
                , relwidth=0.942)
        self.paymentframe.configure(relief='groove')
        self.paymentframe.configure(borderwidth="2")
        self.paymentframe.configure(relief="groove")
        self.paymentframe.configure(background="#d9d9d9")
        self.paymentframe.configure(highlightbackground="#d9d9d9")
        self.paymentframe.configure(highlightcolor="#000000")

        self.creditcardnumber = tk.Label(self.paymentframe)
        self.creditcardnumber.place(relx=0.035, rely=0.049, height=21, width=124)

        self.creditcardnumber.configure(activebackground="#d9d9d9")
        self.creditcardnumber.configure(activeforeground="black")
        self.creditcardnumber.configure(anchor='w')
        self.creditcardnumber.configure(background="#ffffff")
        self.creditcardnumber.configure(compound='left')
        self.creditcardnumber.configure(disabledforeground="#a3a3a3")
        self.creditcardnumber.configure(foreground="#000000")
        self.creditcardnumber.configure(highlightbackground="#d9d9d9")
        self.creditcardnumber.configure(highlightcolor="#000000")
        self.creditcardnumber.configure(text='''Credit Card Number:''')

        self.namelabel = tk.Label(self.paymentframe)
        self.namelabel.place(relx=0.035, rely=0.222, height=21, width=64)
        self.namelabel.configure(activebackground="#d9d9d9")
        self.namelabel.configure(activeforeground="black")
        self.namelabel.configure(anchor='w')
        self.namelabel.configure(background="#ffffff")
        self.namelabel.configure(compound='left')
        self.namelabel.configure(disabledforeground="#a3a3a3")
        self.namelabel.configure(foreground="#000000")
        self.namelabel.configure(highlightbackground="#d9d9d9")
        self.namelabel.configure(highlightcolor="#000000")
        self.namelabel.configure(text='''Name:''')

        self.cardentry = tk.Entry(self.paymentframe)
        self.cardentry.place(relx=0.035, rely=0.123, height=20, relwidth=0.45)
        self.cardentry.configure(background="white")
        self.cardentry.configure(disabledforeground="#a3a3a3")
        self.cardentry.configure(font="TkFixedFont")
        self.cardentry.configure(foreground="#000000")
        self.cardentry.configure(highlightbackground="#d9d9d9")
        self.cardentry.configure(highlightcolor="#000000")
        self.cardentry.configure(insertbackground="#000000")
        self.cardentry.configure(selectbackground="#d9d9d9")
        self.cardentry.configure(selectforeground="black")

        self.expirationdate = tk.Label(self.paymentframe)
        self.expirationdate.place(relx=0.035, rely=0.395, height=21, width=124)
        self.expirationdate.configure(activebackground="#d9d9d9")
        self.expirationdate.configure(activeforeground="black")
        self.expirationdate.configure(anchor='w')
        self.expirationdate.configure(background="#ffffff")
        self.expirationdate.configure(compound='left')
        self.expirationdate.configure(disabledforeground="#a3a3a3")
        self.expirationdate.configure(foreground="#000000")
        self.expirationdate.configure(highlightbackground="#d9d9d9")
        self.expirationdate.configure(highlightcolor="#000000")
        self.expirationdate.configure(text='''Expiration Date:''')

        self.dayentry = tk.Entry(self.paymentframe)
        self.dayentry.place(relx=0.035, rely=0.469, height=20, relwidth=0.078)
        self.dayentry.configure(background="white")
        self.dayentry.configure(disabledforeground="#a3a3a3")
        self.dayentry.configure(font="TkFixedFont")
        self.dayentry.configure(foreground="#000000")
        self.dayentry.configure(highlightbackground="#d9d9d9")
        self.dayentry.configure(highlightcolor="#000000")
        self.dayentry.configure(insertbackground="#000000")
        self.dayentry.configure(selectbackground="#d9d9d9")
        self.dayentry.configure(selectforeground="black")

        self.monthentry = tk.Entry(self.paymentframe)
        self.monthentry.place(relx=0.142, rely=0.469, height=20, relwidth=0.078)
        self.monthentry.configure(background="white")
        self.monthentry.configure(disabledforeground="#a3a3a3")
        self.monthentry.configure(font="TkFixedFont")
        self.monthentry.configure(foreground="#000000")
        self.monthentry.configure(highlightbackground="#d9d9d9")
        self.monthentry.configure(highlightcolor="#000000")
        self.monthentry.configure(insertbackground="#000000")
        self.monthentry.configure(selectbackground="#d9d9d9")
        self.monthentry.configure(selectforeground="black")

        self.CVVlabel = tk.Label(self.paymentframe)
        self.CVVlabel.place(relx=0.035, rely=0.568, height=21, width=44)
        self.CVVlabel.configure(activebackground="#d9d9d9")
        self.CVVlabel.configure(activeforeground="black")
        self.CVVlabel.configure(anchor='w')
        self.CVVlabel.configure(background="#ffffff")
        self.CVVlabel.configure(compound='left')
        self.CVVlabel.configure(disabledforeground="#a3a3a3")
        self.CVVlabel.configure(foreground="#000000")
        self.CVVlabel.configure(highlightbackground="#d9d9d9")
        self.CVVlabel.configure(highlightcolor="#000000")
        self.CVVlabel.configure(text='''CVV:''')

        self.nameentry = tk.Entry(self.paymentframe)
        self.nameentry.place(relx=0.035, rely=0.296, height=20, relwidth=0.414)
        self.nameentry.configure(background="white")
        self.nameentry.configure(disabledforeground="#a3a3a3")
        self.nameentry.configure(font="TkFixedFont")
        self.nameentry.configure(foreground="#000000")
        self.nameentry.configure(highlightbackground="#d9d9d9")
        self.nameentry.configure(highlightcolor="#000000")
        self.nameentry.configure(insertbackground="#000000")
        self.nameentry.configure(selectbackground="#d9d9d9")
        self.nameentry.configure(selectforeground="black")

        self.CVVentry = tk.Entry(self.paymentframe)
        self.CVVentry.place(relx=0.035, rely=0.642, height=20, relwidth=0.113)
        self.CVVentry.configure(background="white")
        self.CVVentry.configure(disabledforeground="#a3a3a3")
        self.CVVentry.configure(font="TkFixedFont")
        self.CVVentry.configure(foreground="#000000")
        self.CVVentry.configure(highlightbackground="#d9d9d9")
        self.CVVentry.configure(highlightcolor="#000000")
        self.CVVentry.configure(insertbackground="#000000")
        self.CVVentry.configure(selectbackground="#d9d9d9")
        self.CVVentry.configure(selectforeground="black")

        self.paybutton = tk.Button(self.paymentframe)
        self.paybutton.place(relx=0.053, rely=0.815, height=26, width=107)
        self.paybutton.configure(activebackground="#d9d9d9")
        self.paybutton.configure(activeforeground="black")
        self.paybutton.configure(background="#0000ff")
        self.paybutton.configure(disabledforeground="#a3a3a3")
        self.paybutton.configure(foreground="#ffffff")
        self.paybutton.configure(highlightbackground="#d9d9d9")
        self.paybutton.configure(highlightcolor="#000000")
        self.paybutton.configure(text='''Payment''')

        self.countrylabel = tk.Label(self.paymentframe)
        self.countrylabel.place(relx=0.619, rely=0.049, height=21, width=64)
        self.countrylabel.configure(activebackground="#d9d9d9")
        self.countrylabel.configure(activeforeground="black")
        self.countrylabel.configure(anchor='w')
        self.countrylabel.configure(background="#ffffff")
        self.countrylabel.configure(compound='left')
        self.countrylabel.configure(disabledforeground="#a3a3a3")
        self.countrylabel.configure(foreground="#000000")
        self.countrylabel.configure(highlightbackground="#d9d9d9")
        self.countrylabel.configure(highlightcolor="#000000")
        self.countrylabel.configure(text='''Country:''')

        self.countryentry = tk.Entry(self.paymentframe)
        self.countryentry.place(relx=0.619, rely=0.123, height=20
                , relwidth=0.202)
        self.countryentry.configure(background="white")
        self.countryentry.configure(disabledforeground="#a3a3a3")
        self.countryentry.configure(font="TkFixedFont")
        self.countryentry.configure(foreground="#000000")
        self.countryentry.configure(highlightbackground="#d9d9d9")
        self.countryentry.configure(highlightcolor="#000000")
        self.countryentry.configure(insertbackground="#000000")
        self.countryentry.configure(selectbackground="#d9d9d9")
        self.countryentry.configure(selectforeground="black")

        self.adrressentry = tk.Entry(self.paymentframe)
        self.adrressentry.place(relx=0.619, rely=0.296, height=20
                , relwidth=0.255)
        self.adrressentry.configure(background="white")
        self.adrressentry.configure(disabledforeground="#a3a3a3")
        self.adrressentry.configure(font="TkFixedFont")
        self.adrressentry.configure(foreground="#000000")
        self.adrressentry.configure(highlightbackground="#d9d9d9")
        self.adrressentry.configure(highlightcolor="#000000")
        self.adrressentry.configure(insertbackground="#000000")
        self.adrressentry.configure(selectbackground="#d9d9d9")
        self.adrressentry.configure(selectforeground="black")

        self.emaillabel = tk.Label(self.paymentframe)
        self.emaillabel.place(relx=0.619, rely=0.395, height=21, width=44)
        self.emaillabel.configure(activebackground="#d9d9d9")
        self.emaillabel.configure(activeforeground="black")
        self.emaillabel.configure(anchor='w')
        self.emaillabel.configure(background="#ffffff")
        self.emaillabel.configure(compound='left')
        self.emaillabel.configure(disabledforeground="#a3a3a3")
        self.emaillabel.configure(foreground="#000000")
        self.emaillabel.configure(highlightbackground="#d9d9d9")
        self.emaillabel.configure(highlightcolor="#000000")
        self.emaillabel.configure(text='''email:''')

        self.addresslabel = tk.Label(self.paymentframe)
        self.addresslabel.place(relx=0.619, rely=0.222, height=21, width=84)
        self.addresslabel.configure(activebackground="#d9d9d9")
        self.addresslabel.configure(activeforeground="black")
        self.addresslabel.configure(anchor='w')
        self.addresslabel.configure(background="#ffffff")
        self.addresslabel.configure(compound='left')
        self.addresslabel.configure(disabledforeground="#a3a3a3")
        self.addresslabel.configure(foreground="#000000")
        self.addresslabel.configure(highlightbackground="#d9d9d9")
        self.addresslabel.configure(highlightcolor="#000000")
        self.addresslabel.configure(text='''Address,City:''')

        self.emailentry = tk.Entry(self.paymentframe)
        self.emailentry.place(relx=0.619, rely=0.494, height=20, relwidth=0.219)
        self.emailentry.configure(background="white")
        self.emailentry.configure(disabledforeground="#a3a3a3")
        self.emailentry.configure(font="TkFixedFont")
        self.emailentry.configure(foreground="#000000")
        self.emailentry.configure(highlightbackground="#d9d9d9")
        self.emailentry.configure(highlightcolor="#000000")
        self.emailentry.configure(insertbackground="#000000")
        self.emailentry.configure(selectbackground="#d9d9d9")
        self.emailentry.configure(selectforeground="black")

        self.backbutton = tk.Button(self.paymentframe)
        self.backbutton.place(relx=0.619, rely=0.815, height=26, width=87)
        self.backbutton.configure(activebackground="#d9d9d9")
        self.backbutton.configure(activeforeground="black")
        self.backbutton.configure(background="#0000ff")
        self.backbutton.configure(disabledforeground="#a3a3a3")
        self.backbutton.configure(foreground="#ffffff")
        self.backbutton.configure(highlightbackground="#d9d9d9")
        self.backbutton.configure(highlightcolor="#000000")
        self.backbutton.configure(text='''⟵ BACK''')


if __name__ == '__main__':
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)

    global _top1, _w1
    _top1 = root
    _w1 = PaymentScreen(_top1)
    root.mainloop()




