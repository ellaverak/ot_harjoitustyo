from tkinter import ttk, constants
from services.user_service import user_service

class RegisterView:
    def __init__(self, root, start):
        self._root = root
        self.start = start
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_user(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            #error
            return

        try:
            user_service.create_user(username, password, 0)
            self.start()
        except:
            #error
            pass

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text='Anna uusi käyttäjätunnus')

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(row=1, column=0)
        self._username_entry.grid(row=2, column=0)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text='Anna uusi salasana')

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(row=3, column=0)
        self._password_entry.grid(row=4, column=0)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        register_label = ttk.Label(master=self._frame, text="Luo käyttäjä")

        self._initialize_username_field()
        self._initialize_password_field()

        main_button = ttk.Button(
            master=self._frame,
            text="Takaisin päävalikkoon",
            command=self.start
        )

        accept_button = ttk.Button(
            master=self._frame,
            text="Hyväksy",
            command=self._create_user
        )

        register_label.grid(row=0, column=0)
        main_button.grid(row=6, column=0)
        accept_button.grid(row=5, column=0)
