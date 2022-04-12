from tkinter import ttk, constants
from services.mommo_service import mommo_service


class NewMommoView:
    def __init__(self, root, mommo_view):
        self.root = root
        self.mommo_view = mommo_view
        self.frame = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def create_new_mommo(self):
        name = self.name_entry.get()

        if len(name) == 0:
            # error
            print("length error")
            return

        mommo_service.create_mommo(name)
        self.mommo_view()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        new_mommo_label = ttk.Label(master=self.frame, text="Uusi mömmöystävä")

        self.initialize_name_field()

        accept_button = ttk.Button(
            master=self.frame,
            text="Hyväksy",
            command=self.create_new_mommo
        )

        new_mommo_label.grid(row=0, column=0)
        accept_button.grid(row=4, column=0)

    def initialize_name_field(self):
        name_label = ttk.Label(master=self.frame, text='Anna mömmöllesi nimi')

        self.name_entry = ttk.Entry(master=self.frame)

        name_label.grid(row=2, column=0)
        self.name_entry.grid(row=3, column=0)
