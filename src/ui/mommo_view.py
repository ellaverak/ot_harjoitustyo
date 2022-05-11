from tkinter import ttk, constants, StringVar, Canvas
from services.mommo_service import mommo_service
from services.user_service import user_service

class DrawMommoView:
    def __init__(self, root):

        self._root = root
        self._frame = None
        self.canvas = None
        self.b_c = None
        self.e_c = None
        self.s_c = None
        self.body = None
        self.eye_1 = None
        self.eye_2 = None
        self.smile = None

        self._initialize()

    def pack(self):
        """näyttää kaikki näkymän komponentit.
        """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """tuhoaa kaikki näkymän komponentit.
        """

        self._frame.destroy()

    def _position_1(self):
        self.b_c = [250, 90, 40]
        self.e_c = [235, 85, 4, 255, 85, 4]
        self.s_c = [235,100,245,110,255,100]

        self._initialize_draw_mommo_position()
        self._frame.after(1000, self._position_2)

    def _position_2(self):
        self.b_c = [300, 90, 40]
        self.e_c = [300, 85, 4, 320, 85, 4]
        self.s_c = [300,100,310,110,320,100]

        self._initialize_draw_mommo_position()
        self._frame.after(1000, self._position_1)

    def _draw_jump(self):
        self.b_c = [90, 60, 40]
        self.e_c = [40, 55, 4, 60, 55, 4]
        self.s_c = [40,70,50,80,60,70]

        self._initialize_draw_mommo_position()

    def draw_mommo(self, x, y, r, canvas, color=None):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvas.create_oval(x0, y0, x1, y1, fill=color)

    def draw_mommo_smile(self, x1, y1, x2, y2, x3, y3, canvas):
        return canvas.create_line(x1,y1,x2,y2,x3,y3, smooth=1)

    def _initialize_draw_mommo_position(self):
        if self.body:
            self.canvas.delete(self.body)

        if self.eye_1:
            self.canvas.delete(self.eye_1)

        if self.eye_2:
            self.canvas.delete(self.eye_2)

        if self.smile:
            self.canvas.delete(self.smile)

        self.body = self.draw_mommo(self.b_c[0], self.b_c[1], self.b_c[2], self.canvas)
        self.eye_1 = self.draw_mommo(self.e_c[0], self.e_c[1], self.e_c[2], self.canvas, "black")
        self.eye_2 = self.draw_mommo(self.e_c[3], self.e_c[4], self.e_c[5], self.canvas, "black")
        self.smile = self.draw_mommo_smile(self.s_c[0], self.s_c[1], self.s_c[2],
        self.s_c[3], self.s_c[4], self.s_c[5], self.canvas)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self.canvas = Canvas(master=self._frame, bg=None, height=140, width=400)

        self._position_1()

        self.canvas.grid(row=0, column=0)


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
        self.canvas = None

        self._draw_mommo_view = None

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


    def _initialize_draw_mommo(self):
        if self._draw_mommo_view:
            self._draw_mommo_view.destroy()

        self._draw_mommo_view =DrawMommoView(self._root)
        self._draw_mommo_view.pack()

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
        self._initialize_draw_mommo()

        if not mommo_service.visit_state:
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
