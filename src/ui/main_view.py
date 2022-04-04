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
        main_title = ttk.Label(master=self._frame, text="Mömmöystävä")

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_login_view
        )

        register_button = ttk.Button(
            master=self._frame,
            text="Luo käyttäjä",
            command=self._handle_register_view
        )

        main_title.grid(row=0, column=0)
        login_button.grid(row=1, column=0)
        register_button.grid(row=2, column=0)