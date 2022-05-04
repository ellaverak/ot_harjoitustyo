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

        self.root = root
        self.frame = None
        self.main_view = main_view
        self.all_mommos_view = all_mommos_view
        self.pet_variable = None
        self.pet_label = None
        self.pet_message = None

        self.initialize()

    def pack(self):
        """näyttää kaikki näkymän komponentit.
        """

        self.frame.pack(fill=constants.X)

    def destroy(self):
        """tuhoaa kaikki näkymän komponentit.
        """

        self.frame.destroy()

    def quit(self):
        """kirjaa kaiken ulos ja avaa päänäkymän.
        """

        mommo_service.logout_mommo()
        user_service.logout()
        self.main_view()

    def quit_visit(self):
        mommo_service.visit_state = False
        mommo_service.logout_mommo()
        self.all_mommos_view()

    def feed_mommo(self):
        """ruokkii mömmän.
        """

        mommo_service.feed_mommo()
        self.initialize_mommo()

    def water_mommo(self):
        """juottaa mömmän.
        """

        mommo_service.water_mommo()
        self.initialize_mommo()

    def pet_mommo(self):
        """silittää mömmöä.
        """

        self.pet_message = "Silitit mömmöä! :)"
        self.pet_variable.set(self.pet_message)
        self.pet_label.grid()

        self.frame.after(2000, self.hide_pet_message)

    def hide_pet_message(self):
        """piilottaa pet_mommo-funtkion luoman viestin.
        """

        self.pet_message = ""
        self.pet_variable.set(self.pet_message)
        self.pet_label.grid()

    def clean_mommo(self):
        """puhdistaa mömmön.
        """

        mommo_service.clean_mommo()
        self.initialize_mommo()

    def initialize_mommo(self):
        """alustaa mömmön tiedot.
        """

        mommo_name_stat = ttk.Label(
            master=self.frame, text=mommo_service.mommo.name)
        mommo_hunger_stat = ttk.Label(
            master=self.frame, text=mommo_service.mommo.hunger)
        mommo_thirst_stat = ttk.Label(
            master=self.frame, text=mommo_service.mommo.thirst)
        mommo_clenliness_stat = ttk.Label(
            master=self.frame, text=mommo_service.mommo.clenliness)
        mommo_happiness_stat = ttk.Label(
            master=self.frame, text=mommo_service.mommo.happiness)

        mommo_name_stat.grid(row=1, column=1)
        mommo_hunger_stat.grid(row=2, column=1)
        mommo_thirst_stat.grid(row=3, column=1)
        mommo_clenliness_stat.grid(row=4, column=1)
        mommo_happiness_stat.grid(row=5, column=1)

        if not mommo_service.visit_state:
            self.frame.after(1000, self.initialize_mommo)
            mommo_service.save_mommo()

    def initialize(self):
        """alustaa näkymän.
        """

        self.frame = ttk.Frame(master=self.root)
        mommo_label = ttk.Label(master=self.frame, text="Mömmöystävä")
        mommo_name_label = ttk.Label(master=self.frame, text="Nimi:")
        mommo_hunger_label = ttk.Label(master=self.frame, text="Nälkäisyys")
        mommo_thirst_label = ttk.Label(master=self.frame, text="Janoisuus:")
        mommo_clenliness_label = ttk.Label(master=self.frame, text="Puhtaus:")
        mommo_happiness_label = ttk.Label(
            master=self.frame, text="Onnellisuus:")
        self.pet_variable = StringVar(self.frame)

        self.pet_label = ttk.Label(
            master=self.frame,
            textvariable=self.pet_variable,
            foreground='green'
        )

        self.pet_label.grid(row=1, column=2)

        self.initialize_mommo()

        if not mommo_service.visit_state:
            quit_button = ttk.Button(
                master=self.frame,
                text="Tallenna ja lopeta",
                command=self.quit
            )

            all_mommos_button = ttk.Button(
            master=self.frame,
            text="Mömmöystävät",
            command=self.all_mommos_view
            )

        if not mommo_service.visit_state or user_service.user.role == 1:
            feed_button = ttk.Button(
                master=self.frame,
                text="Ruoki",
                command=self.feed_mommo
            )

            water_button = ttk.Button(
                master=self.frame,
                text="Juota",
                command=self.water_mommo
            )

            clean_button = ttk.Button(
                master=self.frame,
                text="Siivoa jätökset",
                command=self.clean_mommo
            )


        if mommo_service.visit_state:
            quit_visit_button = ttk.Button(
            master=self.frame,
            text="Takaisin",
            command=self.quit_visit
            )


        pet_button = ttk.Button(
            master=self.frame,
            text="Silitä",
            command=self.pet_mommo
        )

        mommo_label.grid(row=0, column=0)
        mommo_name_label.grid(row=1, column=0)
        mommo_hunger_label.grid(row=2, column=0)
        mommo_thirst_label.grid(row=3, column=0)
        mommo_clenliness_label.grid(row=4, column=0)
        mommo_happiness_label.grid(row=5, column=0)

        if not mommo_service.visit_state:
            quit_button.grid(row=7, column=0)
            all_mommos_button.grid(row=6, column=0)

        if not mommo_service.visit_state or user_service.user.role == 1:
            feed_button.grid(row=2, column=2)
            water_button.grid(row=3, column=2)
            clean_button.grid(row=4, column=2)

        if mommo_service.visit_state:
            quit_visit_button.grid(row=7, column=0)

        pet_button.grid(row=5, column=2)

