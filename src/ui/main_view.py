from tkinter import ttk, constants


class MainView:
    def __init__(self, root, login_view, register_view):
        self.root = root
        self.login_view = login_view
        self.register_view = register_view
        self.frame = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        main_title = ttk.Label(master=self.frame, text="Mömmöystävä")

        login_button = ttk.Button(
            master=self.frame,
            text="Kirjaudu sisään",
            command=self.login_view
        )

        register_button = ttk.Button(
            master=self.frame,
            text="Luo käyttäjä",
            command=self.register_view
        )

        main_title.grid(row=0, column=0)
        login_button.grid(row=1, column=0)
        register_button.grid(row=2, column=0)
