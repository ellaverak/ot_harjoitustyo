from tkinter import ttk, constants

class LoginView:
    def __init__(self, root, start):
        self.root = root
        self.start = start
        self.frame = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        login_label = ttk.Label(master=self.frame, text="Kirjaudu sisään")

        main_button = ttk.Button(
            master=self.frame,
            text="Takaisin päävalikkoon",
            command=self.start
        )

        login_label.grid(row=0, column=0)
        main_button.grid(row=1, column=0)