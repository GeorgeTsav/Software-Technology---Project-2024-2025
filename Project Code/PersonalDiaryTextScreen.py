import tkinter as tk

import DBManager
import MessageScreen

class PersonalDiaryTextScreen:
    def __init__(self, top=None, root=None, username=None, date=None):
        self.top = top
        self.root = root
        self.username = username
        self.date = date
        self.top.title(f"Diary Entry for {date}")

        self.text_area = tk.Text(top, width=50, height=15)
        self.text_area.pack(padx=10, pady=10)

        # Load entry from DB
        entry = self.search_entries(username, date)
        if entry:
            self.text_area.insert(tk.END, entry)

        self.save_btn = tk.Button(self.top, text="Save Entry", command=self.save_entry)
        self.save_btn.pack(pady=(0, 10))
        self.save_btn.configure(activebackground="#0080ff")
        self.save_btn.configure(activeforeground="black")
        self.save_btn.configure(background="#d9d9d9")
        self.save_btn.configure(disabledforeground="#a3a3a3")
        self.save_btn.configure(font="-family {Segoe UI} -size 9")
        self.save_btn.configure(foreground="#000000")
        self.save_btn.configure(highlightbackground="#d9d9d9")
        self.save_btn.configure(highlightcolor="#000000")

    def search_entries(self, username, date):
        db = DBManager.DBManager(database="petato_db")
        db.connect()
        cursor = db.execute_query("SELECT per_diary_text FROM personal_diary WHERE per_diary_user = %s AND per_diary_date = %s", (username, date))
        result = cursor.fetchone() if cursor else None
        cursor.close() if cursor else None
        db.close()
        return result[0] if result else ""

    def save_entry(self):
        text = self.text_area.get("1.0", tk.END).strip()
        if self.checkText(text):
            self.updateDiary(self.username, self.date, text)
            MessageScreen.MessageScreen.display("Success", "Entry saved successfully.")
        else:
            MessageScreen.MessageScreen.display("Error", "Text over 150 characters.")

    def checkText(self, text):
        return bool(len(text) <= 150)

    def updateDiary(self, username, date, entry):
        db = DBManager.DBManager(database="petato_db")
        db.connect()
        db.execute_query(
            "REPLACE INTO personal_diary (per_diary_user, per_diary_date, per_diary_text) VALUES (%s, %s, %s)",
            (username, date, entry)
        )
        db.connection.commit()
        db.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  #Κρύβει το κύριο παράθυρο
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    top = tk.Toplevel(root)
    username = "george_tsavos"
    date = "2023-10-01"
    window = PersonalDiaryTextScreen(top, root, username, date)
    root.mainloop()