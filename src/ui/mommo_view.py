from tkinter import ttk, constants, StringVar, Canvas
from services.mommo_service import mommo_service
from services.user_service import user_service


class DrawMommoView:
    def __init__(self, root):

        self._root = root
        self._frame = None
        self._canvas = None
        self._b_c = None  # body coordinates
        self._e_c = None  # eye coordinates
        self._s_c = None  # smile coordinates
        self._body = None
        self._eye_1 = None
        self._eye_2 = None
        self._smile = None
        self._pet_heart = None

        self._initialize()

    def pack(self):
        """näyttää kaikki näkymän komponentit.
        """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """tuhoaa kaikki näkymän komponentit.
        """

        self._frame.destroy()

    def destroy_widgets(self):
        if self._body:
            self._canvas.delete(self._body)

        if self._eye_1:
            self._canvas.delete(self._eye_1)

        if self._eye_2:
            self._canvas.delete(self._eye_2)

        if self._smile:
            self._canvas.delete(self._smile)

        if self._pet_heart:
            self._canvas.delete(self._pet_heart)

    def draw_squish(self):
        self._e_c = [240, 100, 4, 260, 100, 4]
        self._s_c = [240, 110, 250, 120, 260, 110]

        self._initialize_mommo_position("squish")

    def draw_jump(self):
        self._b_c = [250, 60, 40]
        self._e_c = [240, 40, 4, 260, 40, 4]
        self._s_c = [240, 55, 250, 65, 260, 55]

        self._initialize_mommo_position()

    def draw_play_dead(self):
        self._b_c = [250, 90, 40]
        self._e_c = [240, 85, 4, 260, 85, 4]
        self._s_c = [240, 105, 250, 95, 260, 105]

        self._initialize_mommo_position("play_dead", None)

    def draw_pet(self):
        self._b_c = [250, 90, 40]
        self._e_c = [240, 85, 4, 260, 85, 4]
        self._s_c = [240, 100, 250, 120, 260, 100]

        self._initialize_mommo_position("pet")

    def _draw_position_1(self):
        self._b_c = [250, 90, 40]
        self._e_c = [235, 85, 4, 255, 85, 4]
        self._s_c = [235, 100, 245, 110, 255, 100]

        self._initialize_mommo_position()
        self._frame.after(1000, self._draw_position_2)

    def _draw_position_2(self):
        self._b_c = [300, 90, 40]
        self._e_c = [300, 85, 4, 320, 85, 4]
        self._s_c = [300, 100, 310, 110, 320, 100]

        self._initialize_mommo_position()
        self._frame.after(1000, self._draw_position_1)

    def _draw_circle(self, x, y, r, canvas, color=None):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvas.create_oval(x0, y0, x1, y1, fill=color)

    def _draw_line(self, x1, y1, x2, y2, x3, y3, canvas):
        return canvas.create_line(x1, y1, x2, y2, x3, y3, smooth=1)

    def _draw_oval(self, canvas):
        return canvas.create_oval(200, 90, 300, 130)

    def _initialize_mommo_position(self, option=None, eye_color="black"):
        self.destroy_widgets()

        if option == "squish":
            self._body = self._draw_oval(self._canvas)
        else:
            self._body = self._draw_circle(
                self._b_c[0], self._b_c[1], self._b_c[2], self._canvas)

        if option == "pet":
            self._pet_heart = self._canvas.create_text(
                195, 70, text="❤", fill="black", font=('Helvetica 20'))

        self._eye_1 = self._draw_circle(
            self._e_c[0], self._e_c[1], self._e_c[2], self._canvas, eye_color)
        self._eye_2 = self._draw_circle(
            self._e_c[3], self._e_c[4], self._e_c[5], self._canvas, eye_color)
        self._smile = self._draw_line(self._s_c[0], self._s_c[1], self._s_c[2],
                                      self._s_c[3], self._s_c[4], self._s_c[5], self._canvas)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._canvas = Canvas(master=self._frame, bg=None,
                              height=140, width=400)

        self._draw_position_1()

        self._canvas.grid(row=0, column=0)


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
        self._draw_mommo_view.destroy()
        self._main_view()

    def _quit_visit(self):
        mommo_service.visit_state = False
        mommo_service.logout_mommo()
        self._draw_mommo_view.destroy()
        self._all_mommos_view()

    def _open_all_mommos_view(self):
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

    def _initialize_draw_mommo(self):
        if self._draw_mommo_view:
            self._draw_mommo_view.destroy()

        self._draw_mommo_view = DrawMommoView(self._root)
        self._draw_mommo_view.pack()

    def _initialize_base_state(self):
        tricks_label = ttk.Label(master=self._frame, text="Temput")

        self._trick_variable = StringVar(self._frame)

        quit_button = ttk.Button(
            master=self._frame,
            text="Tallenna ja lopeta",
            command=self._quit
        )

        all_mommos_button = ttk.Button(
            master=self._frame,
            text="Mömmöystävät",
            command=self._open_all_mommos_view
        )

        trick_button_1 = ttk.Button(
            master=self._frame,
            text="Hyppää",
            command=lambda: self._handle_trick(0)
        )

        trick_button_2 = ttk.Button(
            master=self._frame,
            text="Litisty",
            command=lambda: self._handle_trick(1)
        )

        trick_button_3 = ttk.Button(
            master=self._frame,
            text="Leiki koullutta",
            command=lambda: self._handle_trick(2)
        )

        self._trick_label = ttk.Label(
            master=self._frame,
            textvariable=self._trick_variable,
            foreground='green'
        )

        tricks_label.grid(row=1, column=4)
        self._trick_label.grid(row=1, column=2)
        quit_button.grid(row=7, column=0)
        all_mommos_button.grid(row=6, column=0)
        trick_button_1.grid(row=2, column=4)
        trick_button_2.grid(row=3, column=4)
        trick_button_3.grid(row=4, column=4)

    def _initialize_extended_state(self):
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

        feed_button.grid(row=2, column=2)
        water_button.grid(row=3, column=2)
        clean_button.grid(row=4, column=2)

    def _initialize_visit_state(self):
        quit_visit_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._quit_visit
        )

        quit_visit_button.grid(row=7, column=0)

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
            command=self._pet_mommo
        )

        mommo_label.grid(row=0, column=0)
        mommo_name_label.grid(row=1, column=0)
        mommo_hunger_label.grid(row=2, column=0)
        mommo_thirst_label.grid(row=3, column=0)
        mommo_clenliness_label.grid(row=4, column=0)
        mommo_happiness_label.grid(row=5, column=0)

        pet_button.grid(row=2, column=3)
