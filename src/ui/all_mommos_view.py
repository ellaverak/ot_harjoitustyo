from tkinter import ttk, constants
from services.mommo_service import mommo_service


class AllMommosView:
    def __init__(self, root, mommo_view):
        self.root = root
        self.mommo_view = mommo_view
        self.frame = None

        mommo_service.login_mommo()

        self.all_mommos = mommo_service.get_all_mommos()

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def initialize_all_mommos(self):
        for i in range(len(self.all_mommos)):
            mommo_button = ttk.Button(
            master=self.frame,
            text=self.all_mommos[i][1],
            command=None
            )

            mommo_owner_label = ttk.Label(master=self.frame, text=f"omistaja: {self.all_mommos[i][2]}")

            mommo_button.grid(row=i+1, column=0)
            mommo_owner_label.grid(row=i+1, column=1)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        main_label = ttk.Label(master=self.frame, text="Mömmöystävät")

        self.initialize_all_mommos()

        back_button = ttk.Button(
            master=self.frame,
            text="Takaisin",
            command=self.mommo_view
        )

        main_label.grid(row=0, column=0)
        back_button.grid(row=6, column=0)