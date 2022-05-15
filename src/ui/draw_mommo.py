from tkinter import ttk, constants, Canvas


class DrawMommo:
    """Mömmönäkymän käyttämä luokka, joka vastaa mömmöanimaatiosta.
    """

    def __init__(self, root):
        """luokan konstruktori, joka luo uuden mömmöanimaation.

        Args:
            root (juuri): juurikomponentti.
        """

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

    def _destroy_widgets(self):
        """poistaa kaikki piirretyt muodot.
        """

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
        """asettaa "litisty" koordinaatit ja kutsuu funktiota, joka alustaa mömmön paikan.
        """

        self._e_c = [240, 100, 4, 260, 100, 4]
        self._s_c = [240, 110, 250, 120, 260, 110]

        self._initialize_mommo_position("squish")

    def draw_jump(self):
        """asettaa "hyppää" koordinaatit ja kutsuu funktiota, joka alustaa mömmön paikan.
        """

        self._b_c = [250, 60, 40]
        self._e_c = [240, 40, 4, 260, 40, 4]
        self._s_c = [240, 55, 250, 65, 260, 55]

        self._initialize_mommo_position()

    def draw_play_dead(self):
        """asettaa "leiki koullutta" koordinaatit ja kutsuu funktiota, joka alustaa mömmön paikan.
        """

        self._b_c = [250, 90, 40]
        self._e_c = [240, 85, 4, 260, 85, 4]
        self._s_c = [240, 105, 250, 95, 260, 105]

        self._initialize_mommo_position("play_dead", None)

    def draw_pet(self):
        """asettaa "silitä" koordinaatit ja kutsuu funktiota, joka alustaa mömmön paikan.
        """

        self._b_c = [250, 90, 40]
        self._e_c = [240, 85, 4, 260, 85, 4]
        self._s_c = [240, 100, 250, 120, 260, 100]

        self._initialize_mommo_position("pet")

    def _draw_position_1(self):
        """asettaa 1. asennon koordinaatit ja kutsuu funktiota, joka alustaa mömmön paikan.
        """

        self._b_c = [250, 90, 40]
        self._e_c = [235, 85, 4, 255, 85, 4]
        self._s_c = [235, 100, 245, 110, 255, 100]

        self._initialize_mommo_position()
        self._frame.after(1000, self._draw_position_2)

    def _draw_position_2(self):
        """asettaa 2. asennon koordinaatit ja kutsuu funktiota, joka alustaa mömmön paikan.
        """

        self._b_c = [300, 90, 40]
        self._e_c = [300, 85, 4, 320, 85, 4]
        self._s_c = [300, 100, 310, 110, 320, 100]

        self._initialize_mommo_position()
        self._frame.after(1000, self._draw_position_1)

    def _draw_circle(self, x, y, r, canvas, color=None):
        """piirtää ympyrän.

        Args:
            x (int): keskipisteen x-koordinaatti.
            y (int): keskipisteen y-koordinaatti.
            r (int): säteen pituus.
            canvas (Canvas): piirtopohja.
            color (str, vapaaehtoinen): ympyrän täyttöväri. Oletusarvoltaan None.

        Returns:
            Canvas widget: ovaali.
        """

        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvas.create_oval(x0, y0, x1, y1, fill=color)

    def _draw_line(self, x1, y1, x2, y2, x3, y3, canvas):
        """piirtää viivan.

        Args:
            x1 (int): lähtöpisteen x-koordinaatti.
            y1 (int): lähtöpisteen y-koordinaatti.
            x2 (int): vetopisteen x-koordinaatti.
            y2 (int): vetopisteen y-koorditaatti.
            x3 (int): kohdepisteen x-koordinaatti.
            y3 (int): kohdepisteen y-koordinaatti.
            canvas (Canvas): piirtopohja.

        Returns:
            Canvas widget: viiva.
        """

        return canvas.create_line(x1, y1, x2, y2, x3, y3, smooth=1)

    def _draw_oval(self, canvas, color=None):
        """piirtää ovaalin.

        Args:
            canvas (Canvas): _description_

        Returns:
            Canvas widget: ovaali
        """

        return canvas.create_oval(200, 90, 300, 130, fill=color)

    def _initialize_mommo_position(self, option=None, eye_color="black"):
        """alustaa mömmön paikan.

        Args:
            option (str, vapaaehtoinen): piirtovalinta.. Oletusarvoltaan None.
            eye_color (str, vapaaehtoinen): silmien väri. Oletusarvoltaan "black".
        """

        self._destroy_widgets()

        if option == "squish":
            self._body = self._draw_oval(self._canvas, "#efffe9")
        else:
            self._body = self._draw_circle(
                self._b_c[0], self._b_c[1], self._b_c[2], self._canvas, "#efffe9")

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
        """alustaa piirtopohjan.
        """

        self._frame = ttk.Frame(master=self._root, style="TFrame")
        self._canvas = Canvas(master=self._frame, bg="#d9ead3",
                              height=140, width=600)

        self._draw_position_1()

        self._canvas.grid(row=1, column=0)
