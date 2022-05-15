from tkinter import *
from tkinter.ttk import *

class UiTheme:
    def __init__(self, root):

        self._root = root
        self._style = Style(root)

        self._set_theme()

    def _set_theme(self):
        app_x = 600
        app_y = 520
        screen_x = self._root.winfo_screenwidth()
        screen_y = self._root.winfo_screenheight()
        x = (screen_x/2) - (app_x/2)
        y = (screen_y/2) - (app_y/2)
        self._root.geometry(f"{app_x}x{app_y}+{int(x)}+{int(y)}")
        self._root.config(bg="#d9ead3")

        self._style.configure("Main.TButton", font=("Algerian", 15), background="#ddbbcc", width=20)

        self._style.configure("Login.TButton", font=("Algerian", 15), background="#ddbbcc", width=20)

        self._style.configure("Register.TButton", font=("Algerian", 15), background="#ddbbcc", width=20)

        self._style.configure("Back.TButton", font=("Algerian", 12), background="#be7e9e", width=20)

        self._style.configure("TFrame", background="#d9ead3")

        self._style.configure("TLabel", background="#d9ead3")

        self._style.configure("TCheckbutton", background="#d9ead3", font=("Algerian", 15))

        self._style.configure("Mommo.TButton", font=("Algerian", 13), background="#eed2b4")

        self._style.configure("Mommo.TLabel", font=("Algerian", 13), background="#d9ead3")

        self._style.configure("Mommo.TFrame", background="#d9ead3")