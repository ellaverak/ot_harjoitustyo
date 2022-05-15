from tkinter import ttk, constants
from services.mommo_service import mommo_service


class AllMommosView:
    def __init__(self, root, mommo_view):
        """luokan konstruktori, joka luo uuden kaikki mömmöt -näkymän.

        Args:
            root (juuri): juurikomponetti.
            mommo_view (funktio): funktio, joka avaa mömmö-näkymän.
        """
        self._root = root
        self._mommo_view = mommo_view
        self._frame = None

        mommo_service.login_mommo()

        self._all_mommos = mommo_service.get_all_mommos()

        self._initialize()

    def pack(self):
        """näyttää kaikki näkymän komponentit.
        """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """tuhoaa kaikki näkymän komponentit.
        """

        self._frame.destroy()

    def _handle_visit(self, visit_user_id):
        """asettaa vierailutilan ja siirtää näkymän mömmönäkymään.

        Args:
            visit_user_id (int): vierailtavan käyttäjän id-tunnus.
        """

        mommo_service.visit_state = True
        mommo_service.login_mommo(visit_user_id)
        self._mommo_view()

    def _initialize_mommo(self, mommo, i):
        """alustaa kaikkien mömmöjen tiedot.
        """

        visit_id = mommo[0]

        mommo_button = ttk.Button(
            master=self._frame,
            text=mommo[1],
            command=lambda: self._handle_visit(visit_id),
            style="Mommo.TButton"
        )

        mommo_owner_label = ttk.Label(
            master=self._frame, text=f"omistaja: {mommo[2]}", style="Mommo.TLabel")

        mommo_button.grid(row=i+1, column=0, pady=5)
        mommo_owner_label.grid(row=i+1, column=1)

    def _initialize(self):
        """alustaa näkymän.
        """

        self._frame = ttk.Frame(master=self._root, style="TFrame")
        main_label = ttk.Label(master=self._frame, text="Mömmöystävät", style="TLabel", font=("Algerian", 20))

        i = 1
        for mommo in self._all_mommos:
            self._initialize_mommo(mommo, i)
            i += 1

        back_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._mommo_view,
            style="Back.TButton"
        )

        back_button.config(width=10)

        main_label.grid(row=0, column=0, padx=20, pady=20)
        back_button.grid(row=6, column=0, pady=20)