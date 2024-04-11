import flet as ft
from database.corso_DAO import CorsoDao
from database.studente_DAO import StudenteDAO
from model.corso import Corso

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._studenteDao = StudenteDAO()
        self._corsoDao = CorsoDao()

    def handle_cercaIscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        self._view.txt_result.controls.clear()
        name = self._view._menuCorsi.value
        if name is None:
            self._view.create_alert("Selezionare un corso")
            return
        studenti = self._studenteDao.studentsInCorso(name)
        self._view.txt_result.controls.append(ft.Text(f"Gli iscritti al corso di {name} sono {len(studenti)}: "))
        for student in studenti:
            self._view.txt_result.controls.append(ft.Text(f"{student.nome}, {student.cognome} ({student.matricola})"))
        self._view.update_page()

    def fill(self):
        corsi = self._corsoDao.getCorsi()
        for corso in corsi:
            self._view._menuCorsi.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
    def handle_cercaStudente(self, e):
        self._view.txt_result.controls.clear()
        matricola = self._view._txt_matricola.value
        if matricola == "":
            self._view.txt_result.controls.append(ft.Text("Inserisci una matricola!", color="red"))
            self._view.update_page()
            return
        studente = self._studenteDao.get_nome_cognome(matricola)
        if len(studente) == 0:
            self._view.create_alert("La matricola inserita non è presente nel database, inserirne una corretta.")
            self._view.update_page()
            return
        for student in studente:
            self._view._txt_nome.value = student.nome
            self._view._txt_cognome.value = student.cognome
        self._view.update_page()

    def handle_cercaCorsi(self, e):
        self._view.txt_result.controls.clear()
        matricola = self._view._txt_matricola.value
        if matricola == "":
            self._view.txt_result.controls.append(ft.Text("Inserisci una matricola!", color="red"))
            self._view.update_page()
            return
        corsi = self._corsoDao.getCorsiPerStudente(matricola)
        if len(corsi) == 0:
            self._view.create_alert("La matricola inserita non è presente nel database, inserirne una corretta.")
            self._view.update_page()
            return
        self._view.txt_result.controls.append(ft.Text(f"Lo studente è iscritto a {len(corsi)} corsi: "))
        for cor in corsi:
            self._view.txt_result.controls.append(ft.Text(cor.__str__()))
        self._view.update_page()

    def handle_iscrivi(self, e):
        self._view.txt_result.controls.clear()
        matricola = self._view._txt_matricola.value
        cod_corso = self._view._menuCorsi.value
        if matricola == "" or cod_corso is None:
            self._view.txt_result.controls.append(ft.Text("Per favore inserire un valori nel campo matricola e selezionare un corso", color="red"))
            self._view.update_page()
            return
        try:
            corsi_iscritto = self._corsoDao.getCorsiPerStudente(matricola)
            if len(corsi_iscritto) == 0:
                self._view.txt_result.controls.append(ft.Text("La persona non è iscritta a nessun corso", color="red"))
                self._view.update_page()
                return
            else:
                for cor in corsi_iscritto:
                    if cor.codins.__eq__(cod_corso):
                        self._view.txt_result.controls.append(ft.Text("La persona è già iscritta a questo corso", color="red"))
                        self._view.update_page()
                        return
                iscritto = self._corsoDao.iscrivi_al_corso(matricola, cod_corso)
                if iscritto:
                    self._view.txt_result.controls.append(
                        ft.Text(f"La matricola: {matricola} è stata iscritta correttamente al corso {cod_corso}!!", color="blue"))
                    self._view.update_page()
            return
        except TypeError as te:
            self._view.txt_result.controls.append(ft.Text("La persona non è iscritta a nessun corso", color="red"))
            self._view.update_page()
        pass

    def handle_clear(self, e):
        self._view._txt_matricola.value = ""
        self._view._txt_cognome.value = ""
        self._view._txt_nome.value = ""
        self._view.update_page()
