from tkinter import ttk, constants
from services.user_service import user_service


class LoginView:
    def __init__(self, root, main, mommo):
        self.root = root
        self.main = main
        self.mommo = mommo
        self.frame = None
        self.username_entry = None
        self.password_entry = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        login_label = ttk.Label(master=self.frame, text="Kirjaudu sisään")

        self.initialize_username_field()
        self.initialize_password_field()

        main_button = ttk.Button(
            master=self.frame,
            text="Takaisin päävalikkoon",
            command=self.main
        )

        accept_button = ttk.Button(
            master=self.frame,
            text="Hyväksy",
            command=self.login_user
        )

        login_label.grid(row=0, column=0)
        main_button.grid(row=6, column=0)
        accept_button.grid(row=5, column=0)

    def initialize_username_field(self):
        username_label = ttk.Label(
            master=self.frame, text='Anna käyttäjätunnus')

        self.username_entry = ttk.Entry(master=self.frame)

        username_label.grid(row=1, column=0)
        self.username_entry.grid(row=2, column=0)

    def initialize_password_field(self):
        password_label = ttk.Label(master=self.frame, text='Anna salasana')

        self.password_entry = ttk.Entry(master=self.frame)

        password_label.grid(row=3, column=0)
        self.password_entry.grid(row=4, column=0)

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if len(username) == 0 or len(password) == 0:
            # error
            print("length error")
            return

        try:
            result = user_service.login(username, password)
            self.mommo()
        except:
            # error
            print("login error")
            return
