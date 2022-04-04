from tkinter import ttk, constants

class MainView:
    def __init__(self, root, handle_login_view, handle_register_view):
        self._root = root
        self._handle_login_view = handle_login_view
        self._handle_register_view = handle_register_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Mömmöystävä")

        button_1 = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_login_view
        )

        button_2 = ttk.Button(
            master=self._frame,
            text="Luo käyttäjä",
            command=self._handle_register_view
        )

        label.grid(row=0, column=0)
        button_1.grid(row=1, column=0)
        button_2.grid(row=2, column=0)