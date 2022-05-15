from tkinter import ttk, constants, StringVar
from services.mommo_service import mommo_service, MommoNameLengthError


class NewMommoView:
    def __init__(self, root, mommo_view):
        """luokan konstruktori, joka luo uuden uusi mömmö -näkymän

        Args:
            root (juuri): juurikomponentti.
            mommo_view (funktio): funktio, joka avaa mömmö-näkymän.
        """

        self._root = root
        self._mommo_view = mommo_view
        self._frame = None
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

    def _create_new_mommo(self):
        """luo uuden mömmön.
        """

        name = self._name_entry.get()

        try:
            mommo_service.create_mommo(name)
            self._mommo_view()
        except MommoNameLengthError:
            self._show_error(
                "Mömmön nimen on oltava vähintään neljän merkin pituinen")

    def _initialize_name_field(self):
        """alustaa nimikentän.
        """

        name_label = ttk.Label(master=self._frame, text='Anna mömmöllesi nimi', font=("Algerian",15))

        self._name_entry = ttk.Entry(master=self._frame, font=("Algerian",15))

        name_label.grid(row=2, column=0, pady=5)
        self._name_entry.grid(row=3, column=0)

    def _initialize(self):
        """alustaa näkymän.
        """

        self._frame = ttk.Frame(master=self._root, style="TFrame")
        new_mommo_label = ttk.Label(
            master=self._frame, text="Uusi mömmöystävä", style="TLabel", font=("Algerian", 20))
        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground='blue'
        )

        self._error_label.grid(row=5, column=0)

        self._initialize_name_field()

        accept_button = ttk.Button(
            master=self._frame,
            text="Hyväksy",
            command=self._create_new_mommo,
            style="Login.TButton"
        )

        accept_button.config(width=10)

        new_mommo_label.grid(row=0, column=0, padx=170, pady=20)
        accept_button.grid(row=4, column=0, pady=10)
