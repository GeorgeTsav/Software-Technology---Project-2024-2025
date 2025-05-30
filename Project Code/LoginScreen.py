import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from PIL import Image, ImageTk

import DBManager
import MainMenuScreen
import MessageScreen

_location = os.path.dirname(__file__)
_debug = True

class LoginScreen:
    def __init__(self, top=None, root=None):
        top.geometry("600x450+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Petato")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.root = root

        # Configure grid for top window
        self.top.grid_rowconfigure(0, weight=1)
        self.top.grid_columnconfigure(0, weight=1)
        self.top.grid_columnconfigure(1, weight=1)

        # AppLogoFrame (right)
        self.AppLogoFrame = tk.Frame(self.top, relief='groove', borderwidth=2, background="#d9d9d9",
                                     highlightbackground="#d9d9d9", highlightcolor="#000000")
        self.AppLogoFrame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.AppLogoFrame.grid_rowconfigure(0, weight=0)
        self.AppLogoFrame.grid_rowconfigure(1, weight=1)
        self.AppLogoFrame.grid_columnconfigure(0, weight=1)

        self.AppName = tk.Label(self.AppLogoFrame, text="Petato", font="-family {Rage Italic} -size 36 -weight bold -slant italic",
                                background="#d9d9d9", foreground="#000000", justify='center', anchor='center')
        self.AppName.grid(row=0, column=0, sticky="ew", pady=(10, 0))

        self.AppLogo = tk.Label(self.AppLogoFrame, background="#d9d9d9")
        self.AppLogo.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        photo_location = os.path.join(_location,"./images/ProjectLogo.png")
        global _img0
        img = Image.open(photo_location)
        img = img.resize((350, 350), Image.LANCZOS)
        _img0 = ImageTk.PhotoImage(img)
        self.AppLogo.configure(image=_img0, justify='center')

        # CredentialsFrame (left)
        self.CredentialsFrame = tk.Frame(self.top, relief='groove', borderwidth=2, background="#ffffff",
                                         highlightbackground="#d9d9d9", highlightcolor="#000000")
        self.CredentialsFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        for i in range(8):
            self.CredentialsFrame.grid_rowconfigure(i, weight=1)
        self.CredentialsFrame.grid_columnconfigure(0, weight=1)

        self.WelcomeLabel = tk.Label(self.CredentialsFrame, text="Welcome Back!", font="-family {Segoe UI} -size 20 -weight bold",
                                     background="#ffffff", foreground="#000000", anchor='center')
        self.WelcomeLabel.grid(row=0, column=0, sticky="ew", pady=(10, 10), padx=(5, 5))

        self.CredentialsLabel = tk.Label(self.CredentialsFrame, text="Please enter your credentials below.",
                                         background="#ffffff", foreground="#000000", anchor='center')
        self.CredentialsLabel.grid(row=1, column=0, sticky="ew", pady=(5, 0))

        self.UsernameLabel = tk.Label(self.CredentialsFrame, text="Username", background="#ffffff", foreground="#000000", anchor='w')
        self.UsernameLabel.grid(row=2, column=0, sticky="ew", padx=20, pady=(10, 0))

        self.UsernameEntry = tk.Entry(self.CredentialsFrame, background="white", foreground="#000000")
        self.UsernameEntry.grid(row=3, column=0, sticky="ew", padx=20, pady=(0, 10))

        self.PasswordLabel = tk.Label(self.CredentialsFrame, text="Password", background="#ffffff", foreground="#000000", anchor='w')
        self.PasswordLabel.grid(row=4, column=0, sticky="ew", padx=20, pady=(0, 0))

        self.PasswordEntry = tk.Entry(self.CredentialsFrame, background="white", foreground="#000000", show="*")
        self.PasswordEntry.grid(row=5, column=0, sticky="ew", padx=20, pady=(0, 10))

        self.LoginButton = tk.Button(self.CredentialsFrame, text="Log-in", background="#d9d9d9", foreground="#000000",
                                     activebackground="#0080ff", activeforeground="black", command=self.login)
        self.LoginButton.grid(row=6, column=0, pady=(10, 10))

    def login(self):
        username = self.UsernameEntry.get().strip()
        password = self.PasswordEntry.get().strip()
        
        if not username or not password:
            MessageScreen.MessageScreen.display("Missing Credentials", "Please enter both username and password.")
            return

        db = DBManager.DBManager(database='petato_db')
        db.connect()
        db_cursor = db.execute_query("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))

        if db_cursor.fetchone() is not None:
            db_cursor.close()
            db.close()
            new_top = tk.Toplevel(self.root)
            new_top.protocol('WM_DELETE_WINDOW', self.root.destroy)
            MainMenuScreen.MainMenuScreen(new_top, self.root, username).display(self.top)
        else:
            db_cursor.close()
            db.close()
            MessageScreen.MessageScreen.display("Login Failed", "Invalid username or password.")
      


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    window = LoginScreen(top, root)
    root.mainloop()

