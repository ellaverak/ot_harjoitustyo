from ui.main_view import MainView
from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.new_mommo_view import NewMommoView
from ui.mommo_view import MommoView
from ui.all_mommos_view import AllMommosView


class UI:
    def __init__(self, root):
        """luokan konstruktori, joka luo käyttöliittymän.

        Args:
            root (juuri): juurikomponentti.
        """
        self._root = root
        self._current_view = None

    def main_view(self):
        """avaa päänäkymän.
        """

        self._show_main_view()

    def _login_view(self):
        """avaa kirjautumisnäkymän.
        """

        self._show_login_view()

    def _register_view(self):
        """avaa rekisteröitymisnäkymän.
        """

        self._show_register_view()

    def _new_mommo_view(self):
        """avaa uusi mömmö -näkymän.
        """

        self._show_new_mommo_view()

    def _mommo_view(self):
        """avaa mömmönäkymän.
        """

        self._show_mommo_view()

    def _all_mommos_view(self):
        """avaa kaikki mömmöt -näkymän.
        """

        self._show_all_mommos_view()

    def _show_main_view(self):
        """välittää attribuutit päänäkymälle ja näyttää näkymän.
        """

        self._hide_current_view()

        self._current_view = MainView(
            self._root,
            self._login_view,
            self._register_view
        )

        self._current_view.pack()

    def _show_login_view(self):
        """välittää attribuutit kirjautumisnäkymälle ja näyttää näkymän.
        """

        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self.main_view,
            self._mommo_view
        )

        self._current_view.pack()

    def _show_register_view(self):
        """välittää attribuutit rekisteröitymisnäkymälle ja näyttää näkymän.
        """

        self._hide_current_view()

        self._current_view = RegisterView(
            self._root,
            self.main_view,
            self._new_mommo_view
        )

        self._current_view.pack()

    def _show_new_mommo_view(self):
        """välittää attribuutit uusi mömmö -näkymälle ja näyttää näkymän.
        """

        self._hide_current_view()

        self._current_view = NewMommoView(
            self._root,
            self._mommo_view
        )

        self._current_view.pack()

    def _show_mommo_view(self):
        """välittää attribuutit mömmönäkymälle ja näyttää näkymän.
        """

        self._hide_current_view()

        self._current_view = MommoView(
            self._root,
            self.main_view,
            self._all_mommos_view
        )

        self._current_view.pack()

    def _show_all_mommos_view(self):
        """välittää attribuutit kaikki mömmöt -näkymälle ja näyttää näkymän.
        """

        self._hide_current_view()

        self._current_view = AllMommosView(
            self._root,
            self._mommo_view
        )

        self._current_view.pack()

    def _hide_current_view(self):
        """piilottaa nykyisen näkymän.
        """

        if self._current_view:
            self._current_view.destroy()

        self._current_view = None
