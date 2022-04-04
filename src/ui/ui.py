from ui.main_view import MainView
from ui.login_view import LoginView
from ui.register_view import RegisterView

class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def start(self):
        self.show_main_view()


    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None


    def login_view(self):
        self.show_login_view()


    def register_view(self):
        self.show_register_view()

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
            self.start
        )

        self.current_view.pack()

    def show_register_view(self):
        self.hide_current_view()

        self.current_view = RegisterView(
            self.root,
            self.start
        )

        self.current_view.pack()