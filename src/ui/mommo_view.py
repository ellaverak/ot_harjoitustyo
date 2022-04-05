from tkinter import ttk, constants

class MommoView:
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
        mommo_label = ttk.Label(master=self.frame, text="Mömmöystävä")

        mommo_label.grid(row=0, column=0)