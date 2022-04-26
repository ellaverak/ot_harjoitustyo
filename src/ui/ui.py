from ui.main_view import MainView
from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.new_mommo_view import NewMommoView
from ui.mommo_view import MommoView


class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def main_view(self):
        self.show_main_view()

    def login_view(self):
        self.show_login_view()

    def register_view(self):
        self.show_register_view()

    def new_mommo_view(self):
        self.show_new_mommo_view()

    def mommo_view(self):
        self.show_mommo_view()

    def show_main_view(self):
        self.hide_current_view()

        self.current_view = MainView(
            self.root,
            self.login_view,
            self.register_view
        )

        self.current_view.pack()

    def show_login_view(self):
        self.hide_current_view()

        self.current_view = LoginView(
            self.root,
            self.main_view,
            self.mommo_view
        )

        self.current_view.pack()

    def show_register_view(self):
        self.hide_current_view()

        self.current_view = RegisterView(
            self.root,
            self.main_view,
            self.new_mommo_view
        )

        self.current_view.pack()

    def show_new_mommo_view(self):
        self.hide_current_view()

        self.current_view = NewMommoView(
            self.root,
            self.mommo_view
        )

        self.current_view.pack()

    def show_mommo_view(self):
        self.hide_current_view()

        self.current_view = MommoView(
            self.root,
            self.main_view
        )

        self.current_view.pack()

    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None