from ui.main_view import MainView
from ui.login_view import LoginView
from ui.register_view import RegisterView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main_view()


    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None


    def _handle_login_view(self):
        self._show_login_view()


    def _handle_register_view(self):
        self._show_register_view()

    def _show_main_view(self):
        self._hide_current_view()

        self._current_view = MainView(
            self._root,
            self._handle_login_view,
            self._handle_register_view
        )

        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self.start
        )

        self._current_view.pack()

    def _show_register_view(self):
        self._hide_current_view()

        self._current_view = RegisterView(
            self._root,
            self.start
        )

        self._current_view.pack()