from tkinter import ttk, constants, StringVar
from services.user_service import user_service, PasswordLengthError, UsernameLengthError, UsernameExistsError


class RegisterView:
    def __init__(self, root, main_view, new_mommo_view):
        """luokan konstruktori, joka luo uuden rekisteröinti-näkymän.

        Args:
            root (juuri): juurikomponentti_
            main_view (funktio): funktio, joka avaa päänäkymän.
            new_mommo_view (funktio): funktio, joka avaa uusi mömmö-näkymän.
        """

        self.root = root
        self.main_view = main_view
        self.new_mommo_view = new_mommo_view
        self.frame = None
        self.username_entry = None
        self.password_entry = None
        self.error_variable = None
        self.error_label = None

        self.initialize()

    def pack(self):
        """näyttää kaikki näkymän komponentit.
        """

        self.frame.pack(fill=constants.X)

    def destroy(self):
        """tuhoaa kaikki näkymän komponentit.
        """

        self.frame.destroy()

    def show_error(self, message):
        """näyttää error-viestin.

        Args:
            message (str): error-viesti.
        """

        self.error_variable.set(message)
        self.error_label.grid()

    def hide_error(self):
        """piilottaa error-viestin.
        """

        self.error_label.grid_remove()

    def register_user(self):
        """rekisteröi uuden käyttäjän.
        """

        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            user_service.create_user(username, password, 0)
            self.new_mommo_view()
        except UsernameExistsError:
            self.show_error(f"Käyttäjätunnus on jo käytössä")
        except PasswordLengthError:
            self.show_error(
                f"Salasanan on oltava vähintään neljän merkin pituinen")
        except UsernameLengthError:
            self.show_error(
                f"Käyttäjätunnuksen on oltava vähintään neljän merkin pituinen")

    def initialize_username_field(self):
        """alustaa käyttäjänimikentän.
        """

        username_label = ttk.Label(
            master=self.frame, text='Anna uusi käyttäjätunnus')

        self.username_entry = ttk.Entry(master=self.frame)

        username_label.grid(row=1, column=0)
        self.username_entry.grid(row=2, column=0)

    def initialize_password_field(self):
        """alustaa salasanakentän.
        """

        password_label = ttk.Label(
            master=self.frame, text='Anna uusi salasana')

        self.password_entry = ttk.Entry(master=self.frame)

        password_label.grid(row=3, column=0)
        self.password_entry.grid(row=4, column=0)

    def initialize(self):
        """alustaa näkymän.
        """

        self.frame = ttk.Frame(master=self.root)
        register_label = ttk.Label(master=self.frame, text="Luo käyttäjä")
        self.error_variable = StringVar(self.frame)

        self.error_label = ttk.Label(
            master=self.frame,
            textvariable=self.error_variable,
            foreground='blue'
        )

        self.error_label.grid(row=0, column=0)

        self.initialize_username_field()
        self.initialize_password_field()

        main_button = ttk.Button(
            master=self.frame,
            text="Takaisin päävalikkoon",
            command=self.main_view
        )

        accept_button = ttk.Button(
            master=self.frame,
            text="Hyväksy",
            command=self.register_user
        )

        register_label.grid(row=0, column=0)
        main_button.grid(row=6, column=0)
        accept_button.grid(row=5, column=0)

        self.hide_error()
