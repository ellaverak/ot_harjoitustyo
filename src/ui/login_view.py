from tkinter import ttk, constants

class LoginView:
    def __init__(self, root, start):
        self._root = root
        self.start = start
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        login_label = ttk.Label(master=self._frame, text="Kirjaudu sisään")

        main_button = ttk.Button(
            master=self._frame,
            text="Takaisin päävalikkoon",
            command=self.start
        )

        login_label.grid(row=0, column=0)
        main_button.grid(row=1, column=0)