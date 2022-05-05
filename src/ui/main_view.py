from tkinter import ttk, constants


class MainView:
    def __init__(self, root, login_view, register_view):
        """luokan konstruktori, joka luo uuden päänäkymän.

        Args:
            root (juuri): juurikomponentti.
            login_view (funktio): funktio, joka avaa kirjautumisnäkymän.
            register_view (funktio): funktio, joka avaa rekisteröinti-näkymän.
        """

        self._root = root
        self._login_view = login_view
        self._register_view = register_view
        self._frame = None

        self._initialize()

    def pack(self):
        """näyttää kaikki näkymän komponentit.
        """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """tuhoaa kaikki näkymän komponentit.
        """

        self._frame.destroy()

    def _initialize(self):
        """alustaa näkymän.
        """

        self._frame = ttk.Frame(master=self._root)
        main_title = ttk.Label(master=self._frame, text="Mömmöystävä")

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._login_view
        )

        register_button = ttk.Button(
            master=self._frame,
            text="Luo käyttäjä",
            command=self._register_view
        )

        main_title.grid(row=0, column=0)
        login_button.grid(row=1, column=0)
        register_button.grid(row=2, column=0)
