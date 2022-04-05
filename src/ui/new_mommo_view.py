from tkinter import ttk, constants

class NewMommoView:
    def __init__(self, root):
        self.root = root
        self.frame = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def initialize(self):
        self._frame = ttk.Frame(master=self.root)
        new_mommo_label = ttk.Label(master=self.frame, text="Uusi mömmöystävä")

        new_mommo_label.grid(row=0, column=0)