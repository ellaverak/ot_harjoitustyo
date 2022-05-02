from tkinter import ttk, constants

class AllMommosView:
    def __init__(self, root, mommo_view):
        self.root = root
        self.mommo_view = mommo_view
        self.frame = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        main_label = ttk.Label(master=self.frame, text="Mömmöystävät")

        back_button = ttk.Button(
            master=self.frame,
            text="Takaisin",
            command=self.mommo_view
        )

        main_label.grid(row=0, column=0)
        back_button.grid(row=6, column=0)