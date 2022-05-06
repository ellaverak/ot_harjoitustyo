from tkinter import ttk, constants, StringVar
from services.mommo_service import MommoService, mommo_service
from services.user_service import user_service


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
        self._pet_variable = None
        self._pet_label = None
        self._pet_message = None
        self._jump_variable = None
        self._jump_label = None
        self._jump_message = None
        self._squish_variable = None
        self._squish_label = None
        self._squish_message = None
        self._play_dead_variable = None
        self._play_dead_label = None
        self._play_dead_message = None

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
        message = text
        variable.set(message)
        label.grid()

    def _hide_message(self, message, variable, label):
        message = ""
        variable.set(message)
        label.grid()

    def _quit(self):
        """kirjaa kaiken ulos ja avaa päänäkymän.
        """

        mommo_service.logout_mommo()
        user_service.logout()
        self._main_view()

    def _quit_visit(self):
        mommo_service.visit_state = False
        mommo_service.logout_mommo()
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

        text = "Silitit mömmöä! :)"
        self._show_message(text, self._pet_message,
        self._pet_variable, self._pet_label)


        self._frame.after(2000, lambda: self._hide_message(self._pet_message,
        self._pet_variable, self._pet_label))

    def _handle_trick(self, trick):
        if trick == 1:
            text = mommo_service.do_trick(1)

            self._show_message(text, self._jump_message,
            self._jump_variable, self._jump_label)

            self._frame.after(2000, lambda: self._hide_message(self._jump_message,
            self._jump_variable, self._jump_label))

        if trick == 2:
            text = mommo_service.do_trick(2)

            self._show_message(text, self._squish_message,
            self._squish_variable, self._squish_label)

            self._frame.after(2000, lambda: self._hide_message(self._squish_message,
            self._squish_variable, self._squish_label))

        if trick == 3:
            text = mommo_service.do_trick(3)

            self._show_message(text, self._play_dead_message,
            self._play_dead_variable, self._play_dead_label)

            self._frame.after(2000, lambda: self._hide_message(self._play_dead_message,
            self._play_dead_variable, self._play_dead_label))

    def _initialize_mommo(self):
        """alustaa mömmön tiedot.
        """

        mommo_name_stat = ttk.Label(
            master=self._frame, text=mommo_service.mommo.name)
        mommo_hunger_stat = ttk.Label(
            master=self._frame, text=mommo_service.mommo.hunger)
        mommo_thirst_stat = ttk.Label(
            master=self._frame, text=mommo_service.mommo.thirst)
        mommo_clenliness_stat = ttk.Label(
            master=self._frame, text=mommo_service.mommo.clenliness)
        mommo_happiness_stat = ttk.Label(
            master=self._frame, text=mommo_service.mommo.happiness)

        mommo_name_stat.grid(row=1, column=1)
        mommo_hunger_stat.grid(row=2, column=1)
        mommo_thirst_stat.grid(row=3, column=1)
        mommo_clenliness_stat.grid(row=4, column=1)
        mommo_happiness_stat.grid(row=5, column=1)

        if not mommo_service.visit_state:
            self._frame.after(1000, self._initialize_mommo)
            mommo_service.save_mommo()

    def _initialize(self):
        """alustaa näkymän.
        """

        self._frame = ttk.Frame(master=self._root)
        mommo_label = ttk.Label(master=self._frame, text="Mömmöystävä")
        mommo_name_label = ttk.Label(master=self._frame, text="Nimi:")
        mommo_hunger_label = ttk.Label(master=self._frame, text="Nälkäisyys")
        mommo_thirst_label = ttk.Label(master=self._frame, text="Janoisuus:")
        mommo_clenliness_label = ttk.Label(master=self._frame, text="Puhtaus:")
        mommo_happiness_label = ttk.Label(
            master=self._frame, text="Onnellisuus:")

        if not mommo_service.visit_state:
            tricks_label = ttk.Label(master=self._frame, text="Temput")

            self._jump_variable = StringVar(self._frame)
            self._squish_variable = StringVar(self._frame)
            self._play_dead_variable = StringVar(self._frame)

        self._pet_variable = StringVar(self._frame)

        self._pet_label = ttk.Label(
            master=self._frame,
            textvariable=self._pet_variable,
            foreground='green'
        )

        self._pet_label.grid(row=1, column=2)

        self._initialize_mommo()

        if not mommo_service.visit_state:
            quit_button = ttk.Button(
                master=self._frame,
                text="Tallenna ja lopeta",
                command=self._quit
            )

            all_mommos_button = ttk.Button(
                master=self._frame,
                text="Mömmöystävät",
                command=self._all_mommos_view
            )

            tricks_button_1 = ttk.Button(
                master=self._frame,
                text="Hyppää",
                command=lambda: self._handle_trick(1)
            )

            self._jump_label = ttk.Label(
                master=self._frame,
                textvariable=self._jump_variable,
                foreground='green'
            )

            self._jump_label.grid(row=1, column=2)

            tricks_button_2 = ttk.Button(
                master=self._frame,
                text="Litisty",
                command=lambda: self._handle_trick(2)
            )

            self._squish_label = ttk.Label(
                master=self._frame,
                textvariable=self._squish_variable,
                foreground='green'
            )

            self._squish_label.grid(row=1, column=2)

            tricks_button_3 = ttk.Button(
                master=self._frame,
                text="Leiki koullutta",
                command=lambda: self._handle_trick(3)
            )

            self._play_dead_label = ttk.Label(
                master=self._frame,
                textvariable=self._play_dead_variable,
                foreground='green'
            )

            self._play_dead_label.grid(row=1, column=2)

        if not mommo_service.visit_state or user_service.user.role == 1:
            feed_button = ttk.Button(
                master=self._frame,
                text="Ruoki",
                command=self._feed_mommo
            )

            water_button = ttk.Button(
                master=self._frame,
                text="Juota",
                command=self._water_mommo
            )

            clean_button = ttk.Button(
                master=self._frame,
                text="Siivoa jätökset",
                command=self._clean_mommo
            )

        if mommo_service.visit_state:
            quit_visit_button = ttk.Button(
                master=self._frame,
                text="Takaisin",
                command=self._quit_visit
            )

        pet_button = ttk.Button(
            master=self._frame,
            text="Silitä",
            command=self._pet_mommo
        )

        mommo_label.grid(row=0, column=0)
        mommo_name_label.grid(row=1, column=0)
        mommo_hunger_label.grid(row=2, column=0)
        mommo_thirst_label.grid(row=3, column=0)
        mommo_clenliness_label.grid(row=4, column=0)
        mommo_happiness_label.grid(row=5, column=0)

        if not mommo_service.visit_state:
            tricks_label.grid(row=1, column=4)

        if not mommo_service.visit_state:
            quit_button.grid(row=7, column=0)
            all_mommos_button.grid(row=6, column=0)
            tricks_button_1.grid(row=2, column=4)
            tricks_button_2.grid(row=3, column=4)
            tricks_button_3.grid(row=4, column=4)

        if not mommo_service.visit_state or user_service.user.role == 1:
            feed_button.grid(row=2, column=2)
            water_button.grid(row=3, column=2)
            clean_button.grid(row=4, column=2)

        if mommo_service.visit_state:
            quit_visit_button.grid(row=7, column=0)

        pet_button.grid(row=2, column=3)
