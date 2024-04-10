import flet as ft

from database.corso_DAO import CorsoDao


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_cercaIscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view._menuCorsi.value
        if name is None:
            self._view.create_alert("Selezionare un corso")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def fill(self):
        corso_dao = CorsoDao()
        corsi = corso_dao.getCorsi()
        for corso in corsi:
            self._view._menuCorsi.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
