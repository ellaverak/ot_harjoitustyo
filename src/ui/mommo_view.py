from tkinter import ttk, constants
from services.mommo_service import mommo_service


class MommoView:
    def __init__(self, root):
        self.root = root
        self.frame = None

        mommo_service.login_mommo()
        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def initialize_mommo(self):
        mommo_name_stat = ttk.Label(
            master=self.frame, text=mommo_service.mommo.name)
        mommo_hunger_stat = ttk.Label(
            master=self.frame, text=mommo_service.mommo.hunger)
        mommo_thirst_stat = ttk.Label(
            master=self.frame, text=mommo_service.mommo.thirst)
        mommo_clenliness_stat = ttk.Label(
            master=self.frame, text=mommo_service.mommo.clenliness)
        mommo_happiness_stat = ttk.Label(
            master=self.frame, text=mommo_service.mommo.happiness)

        mommo_name_stat.grid(row=1, column=1)
        mommo_hunger_stat.grid(row=2, column=1)
        mommo_thirst_stat.grid(row=3, column=1)
        mommo_clenliness_stat.grid(row=4, column=1)
        mommo_happiness_stat.grid(row=5, column=1)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        mommo_label = ttk.Label(master=self.frame, text="Mömmöystävä")
        mommo_name_label = ttk.Label(master=self.frame, text="Nimi:")
        mommo_hunger_label = ttk.Label(master=self.frame, text="Nälkäisyys")
        mommo_thirst_label = ttk.Label(master=self.frame, text="Janoisuus:")
        mommo_clenliness_label = ttk.Label(master=self.frame, text="Puhtaus:")
        mommo_happiness_label = ttk.Label(
            master=self.frame, text="Onnellisuus:")

        self.initialize_mommo()

        mommo_label.grid(row=0, column=0)
        mommo_name_label.grid(row=1, column=0)
        mommo_hunger_label.grid(row=2, column=0)
        mommo_thirst_label.grid(row=3, column=0)
        mommo_clenliness_label.grid(row=4, column=0)
        mommo_happiness_label.grid(row=5, column=0)
