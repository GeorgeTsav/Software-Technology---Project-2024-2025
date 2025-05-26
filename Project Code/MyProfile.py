import tkinter as tk

import DBManager
import MyMessagesScreen  

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'

class MyProfile:
    def __init__(self, top=None, root=None, username=None):
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
        self.root = root

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.MyProfileframe = tk.Frame(self.top)
        self.MyProfileframe.place(relx=0.016, rely=0.017, relheight=0.965, relwidth=0.955)
        self.MyProfileframe.configure(relief='groove', borderwidth="2", background="#c0c0c0",
                                      highlightbackground="#d9d9d9", highlightcolor="#000000")

        self.MyProfilePhoto = tk.Label(self.MyProfileframe)
        self.MyProfilePhoto.place(relx=0.392, rely=0.07, height=142, width=144)
        self.MyProfilePhoto.configure(background="#8080ff", font="-family {Segoe UI} -size 9",
                                      foreground="#000000", text='userphoto')

        self.MyProfileusername = tk.Label(self.MyProfileframe)
        self.MyProfileusername.place(relx=0.375, rely=0.366, height=29, width=162)
        self.MyProfileusername.configure(background="#ffffff", font="-family {Segoe UI} -size 9",
                                         foreground="#000000", text=self.username if self.username else "unknown")

        self.fra47_lab51 = tk.Label(self.MyProfileframe)
        self.fra47_lab51.place(relx=0.462, rely=0.471, height=28, width=31)
        self.fra47_lab51.configure(background="#d9d9d9", font="-family {Yu Gothic UI Semibold} -size 12 -weight bold",
                                   foreground="#000000", text='/5')

        self.StarforMyScore = tk.Label(self.MyProfileframe)
        self.StarforMyScore.place(relx=0.538, rely=0.471, height=28, width=32)
        self.StarforMyScore.configure(background="#d9d9d9", font="-family {Segoe UI} -size 9",
                                      foreground="#000000", text='Label')

        self.MyScoreLabel = tk.Label(self.MyProfileframe)
        self.MyScoreLabel.place(relx=0.393, rely=0.471, height=28, width=32)
        self.MyScoreLabel.configure(background="#d9d9d9", font="-family {Segoe UI} -size 9",
                                    foreground="#000000", text='Label')

        self.MyReviews = tk.Label(self.MyProfileframe)
        self.MyReviews.place(relx=0.392, rely=0.611, height=28, width=146)
        self.MyReviews.configure(background="#808080",
                                 font="-family {Yu Gothic UI Semibold} -size 11 -weight bold -underline 1",
                                 foreground="#000000", text='My Reviews')
        self.MyReviews.configure(cursor="hand2")
        self.MyReviews.bind("<Button-1>", lambda e: self.load_Myreviews())

        self.Myreviewlist = tk.Listbox(self.MyProfileframe)
        self.Myreviewlist.place(relx=0.392, rely=0.698, relheight=0.246, relwidth=0.23)
        self.Myreviewlist.configure(background="white", font="TkFixedFont", foreground="#000000",
                                    highlightbackground="#d9d9d9", highlightcolor="#000000",
                                    selectbackground="#d9d9d9", selectforeground="black")

        
        self.MyMessages = tk.Label(self.MyProfileframe)
        self.MyMessages.place(relx=0.1, rely=0.611, height=28, width=146)
        self.MyMessages.configure(background="#808080",
                                  font="-family {Yu Gothic UI Semibold} -size 11 -weight bold -underline 1",
                                  foreground="#000000", text='My Messages')
        self.MyMessages.configure(cursor="hand2")
        self.MyMessages.bind("<Button-1>", lambda e: MyMessagesScreen.MyMessagesScreen(self.top, self.username))

    def load_Myreviews(self):
        db = DBManager.DBManager(host='localhost', user='root', password='', database='petato_db')
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
            self.Myreviewlist.insert(tk.END, display_text)
        cursor.close()
        
        db.close()

    def display(self, previous_window=None):
        if previous_window is not None:
            previous_window.destroy()
        self.top.deiconify()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    top = tk.Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', root.destroy)
    username = "george_tsavos"
    window = MyProfile(top, root, username)
    root.mainloop()
