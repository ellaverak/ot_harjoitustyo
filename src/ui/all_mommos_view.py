from tkinter import ttk, constants

from pyrsistent import v
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
            command=lambda: self._handle_visit(visit_id)
        )

        mommo_owner_label = ttk.Label(
            master=self._frame, text=f"omistaja: {mommo[2]}")

        mommo_button.grid(row=i+1, column=0)
        mommo_owner_label.grid(row=i+1, column=1)

    def _initialize(self):
        """alustaa näkymän.
        """

        self._frame = ttk.Frame(master=self._root)
        main_label = ttk.Label(master=self._frame, text="Mömmöystävät")

        i = 1
        for mommo in self._all_mommos:
            self._initialize_mommo(mommo, i)
            i += 1

        back_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._mommo_view
        )

        main_label.grid(row=0, column=0)
        back_button.grid(row=6, column=0)
