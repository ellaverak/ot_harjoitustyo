from tkinter import ttk, constants, StringVar
from services.mommo_service import mommo_service
from services.user_service import user_service
from ui.draw_mommo import DrawMommo


class MommoView:
    def __init__(self, root, main_view, all_mommos_view):
        """luokan konstruktori, joka luo uuden mömmö-näkymän.

        Args:
            root (juuri): juurikomponentti.
            main_view (funktio): funktio, joka avaa päänäkymän
            all_mommos_view (funktio): funktio, joka avaa kaikki mömmöt -näkymän.
        """

        if not mommo_service.visit_state:
            mommo_service.login_mommo()

        self._root = root
        self._frame = None
        self._main_view = main_view
        self._all_mommos_view = all_mommos_view
        self._draw_mommo_view = None
        self._trick_variable = None
        self._trick_label = None
        self._trick_message = None

        self._initialize()

    def pack(self):
        """näyttää kaikki näkymän komponentit.
        """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """tuhoaa kaikki näkymän komponentit.
        """

        self._frame.destroy()

    def _show_message(self, text, message, variable, label):
        """näyttää viestin.

        Args:
            text (str): teksti.
            message (_type_): _description_
            variable (_type_): _description_
            label (_type_): _description_
        """

        message = text
        variable.set(message)
        label.grid()

    def _hide_message(self, message, variable, label):
        """piilottaa viestin.

        Args:
            message (_type_): _description_
            variable (_type_): _description_
            label (_type_): _description_
        """

        message = ""
        variable.set(message)
        label.grid()

    def _quit(self):
        """kirjaa kaiken ulos, tuhoaa mömmöanimaationäkymän ja avaa päänäkymän.
        """

        mommo_service.logout_mommo()
        user_service.logout()
        self._draw_mommo_view.destroy()
        self._main_view()

    def _quit_visit(self):
        """lopettaa vierailutilan, kirjaa mömmön ulos,
           tuhoaa mömmöanimaationäkymän ja avaa kaikki mömmöt-näkymän.
        """

        mommo_service.visit_state = False
        mommo_service.logout_mommo()
        self._draw_mommo_view.destroy()
        self._all_mommos_view()

    def _open_all_mommos_view(self):
        """avaa kaikki mömmöt -näkymän.
        """

        self._draw_mommo_view.destroy()
        self._all_mommos_view()

    def _feed_mommo(self):
        """ruokkii mömmän.
        """

        mommo_service.feed_mommo()
        self._initialize_mommo()

    def _water_mommo(self):
        """juottaa mömmän.
        """

        mommo_service.water_mommo()
        self._initialize_mommo()

    def _clean_mommo(self):
        """puhdistaa mömmön.
        """

        mommo_service.clean_mommo()
        self._initialize_mommo()

    def _pet_mommo(self):
        """silittää mömmöä.
        """

        self._draw_mommo_view.draw_pet()

    def _handle_trick(self, trick):
        """käynnistää tempun.

        Args:
            trick (int): tempun tunnusnumero.
        """

        if mommo_service.do_trick(trick):
            if trick == 0:
                self._draw_mommo_view.draw_jump()
            elif trick == 1:
                self._draw_mommo_view.draw_squish()
            elif trick == 2:
                self._draw_mommo_view.draw_play_dead()
        else:
            text = "Mömmö harjoittelee..."

            self._show_message(text, self._trick_message,
                               self._trick_variable, self._trick_label)

            self._frame.after(2000, lambda: self._hide_message(self._trick_message,
                                                               self._trick_variable, self._trick_label))

    def _initialize_mommo(self):
        """alustaa mömmön tiedot.
        """

        mommo_name_stat = ttk.Label(
            master=self._frame, text=mommo_service.mommo.name, style="Mommo.TLabel")
        mommo_hunger_stat = ttk.Label(
            master=self._frame, text=mommo_service.mommo.hunger, style="Mommo.TLabel")
        mommo_thirst_stat = ttk.Label(
            master=self._frame, text=mommo_service.mommo.thirst, style="Mommo.TLabel")
        mommo_clenliness_stat = ttk.Label(
            master=self._frame, text=mommo_service.mommo.clenliness, style="Mommo.TLabel")
        mommo_happiness_stat = ttk.Label(
            master=self._frame, text=mommo_service.mommo.happiness, style="Mommo.TLabel")

        mommo_name_stat.grid(row=1, column=1, pady=5)
        mommo_hunger_stat.grid(row=2, column=1, pady=5)
        mommo_thirst_stat.grid(row=3, column=1, pady=5)
        mommo_clenliness_stat.grid(row=4, column=1, pady=5)
        mommo_happiness_stat.grid(row=5, column=1, pady=5)

        if not mommo_service.visit_state:
            self._frame.after(1000, self._initialize_mommo)
            mommo_service.save_mommo()

    def _initialize_draw_mommo(self):
        """alustaa mömmöanimaationäkymän.
        """

        if self._draw_mommo_view:
            self._draw_mommo_view.destroy()

        self._draw_mommo_view = DrawMommo(self._root)
        self._draw_mommo_view.pack()

    def _initialize_base_state(self):
        """alustaa näkymän perustilan.
        """

        tricks_label = ttk.Label(master=self._frame, text="Temput", style="Mommo.TLabel")

        self._trick_variable = StringVar(self._frame)

        quit_button = ttk.Button(
            master=self._frame,
            text="Tallenna ja lopeta",
            command=self._quit,
            style="Back.TButton"
        )

        all_mommos_button = ttk.Button(
            master=self._frame,
            text="Mömmöystävät",
            command=self._open_all_mommos_view,
            style="Login.TButton"
        )

        all_mommos_button.config(width=15)

        trick_button_1 = ttk.Button(
            master=self._frame,
            text="Hyppää",
            command=lambda: self._handle_trick(0),
            style="Mommo.TButton"
        )

        trick_button_2 = ttk.Button(
            master=self._frame,
            text="Litisty",
            command=lambda: self._handle_trick(1),
            style="Mommo.TButton"
        )

        trick_button_3 = ttk.Button(
            master=self._frame,
            text="Leiki koullutta",
            command=lambda: self._handle_trick(2),
            style="Mommo.TButton"
        )

        self._trick_label = ttk.Label(
            master=self._frame,
            textvariable=self._trick_variable,
            foreground='purple',
            style="Mommo.TLabel"
        )

        tricks_label.grid(row=1, column=4)
        self._trick_label.grid(row=5, column=3)
        quit_button.grid(row=7, column=0, pady=10)
        all_mommos_button.grid(row=6, column=0, pady=5)
        trick_button_1.grid(row=2, column=4, padx=5, pady=5)
        trick_button_2.grid(row=3, column=4, padx=5, pady=5)
        trick_button_3.grid(row=4, column=4, padx=5, pady=5)

    def _initialize_extended_state(self):
        """alustaa näkymän jatkotilan.
        """

        feed_button = ttk.Button(
            master=self._frame,
            text="Ruoki",
            command=self._feed_mommo,
            style="Mommo.TButton"
        )

        water_button = ttk.Button(
            master=self._frame,
            text="Juota",
            command=self._water_mommo,
            style="Mommo.TButton"
        )

        clean_button = ttk.Button(
            master=self._frame,
            text="Puhdista",
            command=self._clean_mommo,
            style="Mommo.TButton"
        )

        feed_button.grid(row=2, column=2, padx=5, pady=5)
        water_button.grid(row=3, column=2, padx=5, pady=5)
        clean_button.grid(row=4, column=2, padx=5, pady=5)

    def _initialize_visit_state(self):
        """alustaa näkymän vierailutilan.
        """

        quit_visit_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._quit_visit,
            style="Back.TButton"
        )

        quit_visit_button.grid(row=7, column=0, pady=10)

    def _initialize(self):
        """alustaa näkymän.
        """

        self._frame = ttk.Frame(master=self._root, style="Mommo.TFrame")
        mommo_label = ttk.Label(master=self._frame, text="Mömmöystävä", font=("Algerian", 20))
        mommo_name_label = ttk.Label(master=self._frame, text="Nimi:", style="Mommo.TLabel")
        mommo_hunger_label = ttk.Label(master=self._frame, text="Nälkäisyys", style="Mommo.TLabel")
        mommo_thirst_label = ttk.Label(master=self._frame, text="Janoisuus:", style="Mommo.TLabel")
        mommo_clenliness_label = ttk.Label(master=self._frame, text="Puhtaus:", style="Mommo.TLabel")
        mommo_happiness_label = ttk.Label(
            master=self._frame, text="Onnellisuus:", style="Mommo.TLabel")

        self._initialize_mommo()
        self._initialize_draw_mommo()

        if not mommo_service.visit_state:
            self._initialize_base_state()

        if not mommo_service.visit_state or user_service.user.role == 1:
            self._initialize_extended_state()

        if mommo_service.visit_state:
            self._initialize_visit_state()

        pet_button = ttk.Button(
            master=self._frame,
            text="Silitä",
            command=self._pet_mommo,
            style="Mommo.TButton"
        )

        mommo_label.grid(row=0, column=0, padx=20, pady=20)
        mommo_name_label.grid(row=1, column=0)
        mommo_hunger_label.grid(row=2, column=0)
        mommo_thirst_label.grid(row=3, column=0)
        mommo_clenliness_label.grid(row=4, column=0)
        mommo_happiness_label.grid(row=5, column=0)

        pet_button.grid(row=5, column=2, padx=5, pady=5)

