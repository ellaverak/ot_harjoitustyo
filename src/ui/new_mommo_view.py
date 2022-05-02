from tkinter import ttk, constants, StringVar
from services.mommo_service import mommo_service, MommoNameLengthError


class NewMommoView:
    def __init__(self, root, mommo_view):
        self.root = root
        self.mommo_view = mommo_view
        self.frame = None
        self.error_variable = None
        self.error_label = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def show_error(self, message):
        self.error_variable.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def create_new_mommo(self):
        name = self.name_entry.get()

        try:
            mommo_service.create_mommo(name)
            self.mommo_view()
        except MommoNameLengthError:
            self.show_error(f"Mömmön nimen on oltava vähintään neljän merkin pituinen")

    def initialize_name_field(self):
        name_label = ttk.Label(master=self.frame, text='Anna mömmöllesi nimi')

        self.name_entry = ttk.Entry(master=self.frame)

        name_label.grid(row=2, column=0)
        self.name_entry.grid(row=3, column=0)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        new_mommo_label = ttk.Label(master=self.frame, text="Uusi mömmöystävä")
        self.error_variable = StringVar(self.frame)

        self.error_label = ttk.Label(
            master=self.frame,
            textvariable=self.error_variable,
            foreground='blue'
        )

        self.error_label.grid(row=0, column=0)

        self.initialize_name_field()

        accept_button = ttk.Button(
            master=self.frame,
            text="Hyväksy",
            command=self.create_new_mommo
        )

        new_mommo_label.grid(row=0, column=0)
        accept_button.grid(row=4, column=0)