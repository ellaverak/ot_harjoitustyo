from tkinter import *
from tkinter.ttk import *


class UiTheme:
    """Vastaa sovelluksen ulkoasun pääelementeistä.
    """

    def __init__(self, root):
        """luokan konstruktori, joka luo uuden ulkoasun.

        Args:
            root (juuri): juurikomponentti.
        """

        self._root = root
        self._style = Style(root)

        self._set_theme()

    def _set_theme(self):
        """määrittää ikkunan koon ja teeman.
        """

        app_x = 600
        app_y = 520
        screen_x = self._root.winfo_screenwidth()
        screen_y = self._root.winfo_screenheight()
        x = (screen_x/2) - (app_x/2)
        y = (screen_y/2) - (app_y/2)
        self._root.geometry(f"{app_x}x{app_y}+{int(x)}+{int(y)}")
        self._root.config(bg="#d9ead3")

        self._set_frame_theme()
        self._set_label_theme()
        self._set_button_theme()
        self._set_checbutton_theme()

    def _set_frame_theme(self):
        """määrittää sivujen teeman.
        """

        self._style.configure("TFrame", background="#d9ead3")

    def _set_label_theme(self):
        """määrittää otsikoiden teeman.
        """

        self._style.configure(
            "Main.TLabel", background="#d9ead3", font=("Algerian", 30))
        self._style.configure(
            "Big.TLabel", background="#d9ead3", font=("Algerian", 20))
        self._style.configure(
            "Medium.TLabel", background="#d9ead3", font=("Algerian", 15))
        self._style.configure(
            "Small.TLabel", background="#d9ead3", font=("Algerian", 13))

    def _set_button_theme(self):
        """määrittää nappien teeman.
        """

        self._style.configure("Basic.TButton", font=(
            "Algerian", 15), background="#ddbbcc")
        self._style.configure("Back.TButton", font=(
            "Algerian", 12), background="#be7e9e")
        self._style.configure("Mommo.TButton", font=(
            "Algerian", 13), background="#eed2b4")

    def _set_checbutton_theme(self):
        """määrittää valintanappien teeman.
        """

        self._style.configure(
            "TCheckbutton", background="#d9ead3", font=("Algerian", 15))
