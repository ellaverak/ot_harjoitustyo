from tkinter import ttk, constants, StringVar
from services.user_service import user_service, WrongPasswordError, UserNonexistingError


class LoginView:
    def __init__(self, root, main_view, mommo_view):
        """luokan konstruktori, joka luo uuden kirjautumisnäkymän.

        Args:
            root (juuri): juurikomponentti._
            main_view (funtio): funktio, joka avaa päänäkymän.
            mommo_view (funtio): funktio, joka avaa mömmö-näkymän.
        """
        self._root = root
        self._main_view = main_view
        self._mommo_view = mommo_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self.error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """näyttää kaikki näkymän komponentit.
        """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """tuokaa kaikki näkymän komponentit.
        """

        self._frame.destroy()

    def show_error(self, message):
        """näyttää error-viestin.

        Args:
            message (str): error-viesti.
        """

        self._error_variable.set(message)
        self._error_label.grid()

        self._frame.after(2000, self._hide_error)

    def _hide_error(self):
        """piilottaa error-viestin.
        """

        self._error_label.grid_remove()

    def _login_user(self):
        """kirjaa käyttäjän sisään.
        """

        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            user_service.login(username, password)
            self._mommo_view()
        except UserNonexistingError:
            self.show_error("Käyttäjätunnusta ei ole olemassa")
        except WrongPasswordError:
            self.show_error("Väärä salasana")

    def _initialize_username_field(self):
        """alustaa käyttäjänimikentän.
        """

        username_label = ttk.Label(
            master=self._frame, text='Anna käyttäjätunnus', style="Medium.TLabel")

        self._username_entry = ttk.Entry(
            master=self._frame, font=("Algerian", 15))

        username_label.grid(row=1, column=0, pady=5)
        self._username_entry.grid(row=2, column=0)

    def _initialize_password_field(self):
        """alustaa salasanakentän.
        """

        password_label = ttk.Label(
            master=self._frame, text='Anna salasana', style="Medium.TLabel")

        self._password_entry = ttk.Entry(
            master=self._frame, font=("Algerian", 15))
        password_label.grid(row=3, column=0, pady=5)
        self._password_entry.grid(row=4, column=0)

    def _initialize(self):
        """alustaa näkymän.
        """

        self._frame = ttk.Frame(master=self._root, style="TFrame")
        login_label = ttk.Label(
            master=self._frame, text="Kirjaudu sisään", style="Big.TLabel")
        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground='#cc0000',
            font=("Algerian", 15)
        )

        self._error_label.grid(row=7, column=0)

        self._initialize_username_field()
        self._initialize_password_field()

        main_button = ttk.Button(
            master=self._frame,
            text="Takaisin päävalikkoon",
            style="Back.TButton",
            command=self._main_view
        )

        accept_button = ttk.Button(
            master=self._frame,
            text="Hyväksy",
            style="Basic.TButton",
            command=self._login_user
        )

        accept_button.config(width=10)

        login_label.grid(row=0, column=0, padx=197, pady=20)
        main_button.grid(row=6, column=0, pady=20)
        accept_button.grid(row=5, column=0, pady=10)

        self._root.grid_columnconfigure(0, weight=2, minsize=400)
