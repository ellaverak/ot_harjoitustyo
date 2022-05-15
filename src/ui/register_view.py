from tkinter import Checkbutton, ttk, constants, StringVar, IntVar
from services.user_service import user_service, PasswordLengthError, UsernameLengthError, UsernameExistsError


class RegisterView:
    def __init__(self, root, main_view, new_mommo_view):
        """luokan konstruktori, joka luo uuden rekisteröinti-näkymän.

        Args:
            root (juuri): juurikomponentti_
            main_view (funktio): funktio, joka avaa päänäkymän.
            new_mommo_view (funktio): funktio, joka avaa uusi mömmö-näkymän.
        """

        self._root = root
        self._main_view = main_view
        self._new_mommo_view = new_mommo_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._checkvar = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """näyttää kaikki näkymän komponentit.
        """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """tuhoaa kaikki näkymän komponentit.
        """

        self._frame.destroy()

    def _show_error(self, message):
        """näyttää error-viestin.

        Args:
            message (str): error-viesti.
        """

        self._error_variable.set(message)
        self._error_label.grid()

        self._frame.after(3000, self._hide_error)

    def _hide_error(self):
        """piilottaa error-viestin.
        """

        self._error_label.grid_remove()

    def _register_user(self):
        """rekisteröi uuden käyttäjän.
        """

        username = self._username_entry.get()
        password = self._password_entry.get()
        role = self._checkvar.get()

        try:
            user_service.create_user(username, password, role)
            self._new_mommo_view()
        except UsernameExistsError:
            self._show_error("Käyttäjätunnus on jo käytössä")
        except PasswordLengthError:
            self._show_error(
                "Salasanan on oltava vähintään neljän merkin pituinen")
        except UsernameLengthError:
            self._show_error(
                "Käyttäjätunnuksen on oltava vähintään neljän merkin pituinen")

    def _initialize_username_field(self):
        """alustaa käyttäjänimikentän.
        """

        username_label = ttk.Label(
            master=self._frame, text='Anna uusi käyttäjätunnus', style="TLabel", font=("Algerian", 15))

        self._username_entry = ttk.Entry(master=self._frame, font=("Algerian",15))

        username_label.grid(row=1, column=0,pady=5)
        self._username_entry.grid(row=2, column=0)

    def _initialize_password_field(self):
        """alustaa salasanakentän.
        """

        password_label = ttk.Label(
            master=self._frame, text='Anna uusi salasana', style="TLabel", font=("Algerian", 15))

        self._password_entry = ttk.Entry(master=self._frame, font=("Algerian",15))

        password_label.grid(row=3, column=0, pady=5)
        self._password_entry.grid(row=4, column=0)

    def _initialize_admin_checkbox(self):
        """alustaa ylläpitäjävalinnan.
        """

        role_label = ttk.Label(master=self._frame, text="Rooli", style="TLabel", font=("Algerian",15))

        self._checkvar = IntVar()

        admin_checkbox = ttk.Checkbutton(
            master=self._frame,
            text="Ylläpitäjä",
            variable=self._checkvar,
            onvalue=1,
            offvalue=0,
            style="TCheckbutton"
        )

        role_label.grid(row=5, column=0, pady=5)
        admin_checkbox.grid(row=6, column=0, pady=5)

    def _initialize(self):
        """alustaa näkymän.
        """

        self._frame = ttk.Frame(master=self._root, style="TFrame")
        register_label = ttk.Label(master=self._frame, text="Luo käyttäjä", style="TLabel", font=("Algerian", 20))
        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground='#cc0000',
            font=("Algerian", 15)
        )

        self._error_label.grid(row=9, column=0)

        self._initialize_username_field()
        self._initialize_password_field()
        self._initialize_admin_checkbox()

        main_button = ttk.Button(
            master=self._frame,
            text="Takaisin päävalikkoon",
            command=self._main_view,
            style="Back.TButton"
        )

        accept_button = ttk.Button(
            master=self._frame,
            text="Hyväksy",
            command=self._register_user,
            style="Register.TButton"
        )

        accept_button.config(width=10)

        register_label.grid(row=0, column=0, padx=220, pady=20)
        main_button.grid(row=8, column=0, pady=20)
        accept_button.grid(row=7, column=0, pady=10)

        self._hide_error()