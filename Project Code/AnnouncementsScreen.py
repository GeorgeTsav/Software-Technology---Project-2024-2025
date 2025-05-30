import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkcalendar import DateEntry
import os.path

import DBManager
import MessageScreen
import MessageTextScreen
import OtherProfile
import MainMenuScreen

_location = os.path.dirname(__file__)
_debug = True

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black'
_tabfg2 = 'white'
_bgmode = 'light'
_tabbg1 = '#d9d9d9'
_tabbg2 = 'gray40'

class AnnouncementsScreen:
    def __init__(self, top=None, root=None, username=None):
        self.username = username
        self.root = root

        top.geometry("900x600+341+136")
        top.minsize(600, 400)
        top.maxsize(1600, 900)
        top.title("Petato")
        top.configure(background=_bgcolor)

        self.title_label = tk.Label(top, text="Announcements", font=("Segoe UI", 20, "bold"), bg=_bgcolor, fg="black")
        self.title_label.pack(side="top", pady=10)

        self.back_button = tk.Button(
            top, text="⟵ BACK", bg="#0000ff", fg="white", font=("Segoe UI", 10, "bold"),
            command=self.go_back)
        self.back_button.pack(side="top", anchor="w", padx=20, pady=(0, 5))

        self.top = top
        self.che50 = tk.IntVar()
        self.che51 = tk.IntVar()
        self.che52 = tk.IntVar()
        self.che53 = tk.IntVar()

        self.main_frame = tk.Frame(self.top, bg=_bgcolor)
        self.main_frame.pack(fill="both", expand=True)
        self.main_frame.columnconfigure(0, weight=0)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        left_canvas = tk.Canvas(self.main_frame, bg=_bgcolor, highlightthickness=0)
        left_scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=left_canvas.yview)
        left_scrollbar.grid(row=0, column=0, sticky="nse")

        left_canvas.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=10)
        left_canvas.configure(yscrollcommand=left_scrollbar.set)

        self.left_panel = tk.Frame(left_canvas, bg=_bgcolor)
        left_canvas.create_window((0, 0), window=self.left_panel, anchor="nw")

        def update_scrollregion(event):
            left_canvas.configure(scrollregion=left_canvas.bbox("all"))

        self.left_panel.bind("<Configure>", update_scrollregion)

        def _on_mousewheel(event):
            left_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        left_canvas.bind_all("<MouseWheel>", _on_mousewheel)

        self.ResultFrame = tk.Frame(self.main_frame, bg=_bgcolor, bd=2, relief="groove")
        self.ResultFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.selectlabel = tk.Label(self.left_panel, text="SELECT", bg="#0000ff", fg="white",
                                    font="-family {Segoe UI} -size 9 -weight bold")
        self.selectlabel.pack(pady=(10, 5), anchor="w", padx=10)

        self.dog = tk.Checkbutton(self.left_panel, text="DOG", variable=self.che50, bg=_bgcolor, anchor="w")
        self.dog.pack(anchor="w", padx=10)
        self.cat = tk.Checkbutton(self.left_panel, text="CAT", variable=self.che51, bg=_bgcolor, anchor="w")
        self.cat.pack(anchor="w", padx=10)
        self.adoption = tk.Checkbutton(self.left_panel, text="ADOPTION", variable=self.che52, bg=_bgcolor, anchor="w")
        self.adoption.pack(anchor="w", padx=10)
        self.hospitality = tk.Checkbutton(self.left_panel, text="HOSPITALITY", variable=self.che53, bg=_bgcolor, anchor="w")
        self.hospitality.pack(anchor="w", padx=10)

        tk.Label(self.left_panel, text="Start Date:", bg=_bgcolor).pack(anchor="w", padx=10, pady=(10, 0))
        self.start_date = DateEntry(self.left_panel, date_pattern='yyyy-mm-dd')
        self.start_date.pack(anchor="w", padx=10)

        tk.Label(self.left_panel, text="End Date:", bg=_bgcolor).pack(anchor="w", padx=10, pady=(10, 0))
        self.end_date = DateEntry(self.left_panel, date_pattern='yyyy-mm-dd')
        self.end_date.pack(anchor="w", padx=10)

        self.SearchButton = tk.Button(self.left_panel, text="SEARCH", bg="#0000ff", fg="white",
                                      font="-family {Segoe UI} -size 9", command=self.search_announcements)
        self.SearchButton.pack(pady=(10, 20), padx=10, fill="x")

    def display(self, previous_window=None):
        if previous_window is not None:
            previous_window.destroy()
        self.top.deiconify()

    def go_back(self):
        new_window = tk.Toplevel(self.root)
        new_window.protocol('WM_DELETE_WINDOW', new_window.destroy)
        main_menu_screen = MainMenuScreen.MainMenuScreen(top=new_window, root=self.root, username=self.username)
        main_menu_screen.display(previous_window=self.top)

    def update_interestedusers(self, ann_id):
        db = DBManager.DBManager(database='petato_db')
        db.connect()
        try:
            query = "INSERT INTO interested_users (int_ann, int_user) VALUES (%s, %s)"
            cursor = db.connection.cursor()
            cursor.execute(query, (ann_id, self.username))
            db.connection.commit()
        except Exception as e:
            print("Error inserting interest:", e)
        finally:
            cursor.close()
            db.close()

    def retrieveinformation(self, parent, ann_user, ann_id):
        
        message_button = tk.Button(
            parent, text="Message", bg="#2846a7", fg="white", font=("Segoe UI", 9),
            command=lambda ann_user=ann_user: MessageTextScreen.MessageTextScreen(self.top, self.username, ann_user)
        )
        message_button.grid(row=0, column=3, sticky='e', padx=(5, 10))

        username_label = tk.Label(
            parent,
            text=f"Username: {ann_user}",
            font=("Segoe UI", 9, "underline"),
            fg="blue",
            bg="#ffffff",
            cursor="hand2"
        )
        username_label.grid(row=0, column=1, sticky="w", padx=(20, 0))

        def open_profile(event, user=ann_user):
            OtherProfile.OtherProfile(tk.Toplevel(self.root), user, self.username)

        username_label.bind("<Button-1>", open_profile)

    def retrievedetails(self, parent, ann_type, adopt_description, host_start_date, host_end_date):
        
        description = adopt_description if ann_type == 'ADOPTION' else f"Host start date: {host_start_date}  Host end date: {host_end_date}"

        desc_label = tk.Label(parent, text=description, wraplength=520, justify='left', bg="#ffffff",
                              font=("Segoe UI", 9))
        desc_label.grid(row=1, column=0, columnspan=4, sticky='w', pady=(8, 0))
        desc_label.grid_remove()

        toggle_button = tk.Button(
            parent, text="More...", font=("Segoe UI", 9, "italic"),
            bg="#ffffff", bd=0, fg="blue", cursor="hand2"
        )
        toggle_button.grid(row=2, column=0, columnspan=4, sticky="w", pady=(5, 0), padx=(20, 0))

        def toggle_description():
            if desc_label.winfo_viewable():
                desc_label.grid_remove()
                toggle_button.config(text="More...")
            else:
                desc_label.grid()
                toggle_button.config(text="Less...")

        toggle_button.config(command=toggle_description)

    def search_announcements(self):
        pet_filters = []
        type_filters = []
        from_date = self.start_date.get_date().strftime('%Y-%m-%d')
        to_date = self.end_date.get_date().strftime('%Y-%m-%d')

        if self.che50.get() == 1:
            pet_filters.append('DOG')
        if self.che51.get() == 1:
            pet_filters.append('CAT')
        if self.che52.get() == 1:
            type_filters.append('ADOPTION')
        if self.che53.get() == 1:
            type_filters.append('HOST')

        db = DBManager.DBManager(database='petato_db')
        db.connect()

        query = "SELECT ann_id, ann_title, ann_date, ann_type, adopt_description, host_start_date, host_end_date, ann_user FROM announcements WHERE 1=1"
        params = []
        if pet_filters:
            placeholders = ",".join(["%s"] * len(pet_filters))
            query += f" AND ann_pet IN ({placeholders})"
            params.extend(pet_filters)
        if type_filters:
            placeholders = ",".join(["%s"] * len(type_filters))
            query += f" AND ann_type IN ({placeholders})"
            params.extend(type_filters)
        if from_date and to_date:
            query += " AND ann_date BETWEEN %s AND %s"
            params.extend([from_date, to_date])

        db_cursor = db.execute_query(query, tuple(params))
        results = db_cursor.fetchall()

        for widget in self.ResultFrame.winfo_children():
            widget.destroy()

        if results:
            canvas = tk.Canvas(self.ResultFrame, background="#f0f0f0")
            scrollbar = ttk.Scrollbar(self.ResultFrame, orient="vertical", command=canvas.yview)
            scroll_frame = tk.Frame(canvas, background="#f0f0f0")
            scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
            canvas.create_window((0, 0), window=scroll_frame, anchor='nw')
            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            for idx, (ann_id, title, date, ann_type, adopt_description, host_start_date, host_end_date, ann_user) in enumerate(results):
                container = tk.Frame(scroll_frame, bg="#ffffff", bd=1, relief="solid", padx=10, pady=10)
                container.grid(row=idx, column=0, sticky='ew', pady=5, padx=5)
                container.grid_columnconfigure(0, weight=1)

                title_label = tk.Label(container, text=title, font=("Segoe UI", 10, "bold"), anchor='w', bg="#ffffff")
                title_label.grid(row=0, column=0, sticky='w', padx=(20, 0))

                date_label = tk.Label(container, text=str(date), font=("Segoe UI", 9), anchor='e', bg="#ffffff")
                date_label.grid(row=1, column=0, sticky='e', padx=(10, 10))

                star_button = tk.Button(container, text="★", font=("Segoe UI", 14), fg="gold", bg="#ffffff", bd=0,
                                        activebackground="#ffffff",
                                        command=lambda ann_id=ann_id: self.update_interestedusers(ann_id))
                star_button.grid(row=0, column=2, sticky='e', padx=(0, 10))

                if ann_user:
                    self.retrieveinformation(container, ann_user, ann_id)

                self.retrievedetails(container, ann_type, adopt_description, host_start_date, host_end_date)

            db_cursor.close()
            db.close()
        else:
            db_cursor.close()
            db.close()
            MessageScreen.MessageScreen().display("There are no announcements")


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    top = tk.Toplevel(root)
    window = AnnouncementsScreen(top, root, username="giwrgos2")
    root.mainloop()
