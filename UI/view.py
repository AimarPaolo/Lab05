import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_cercaIscritti = None
        self._txt_matricola = None
        self.txt_container = None
        self._menuCorsi = None
        self._txt_nome = None
        self._txt_cognome = None
        self.txt_result = None
        self._btn_cercaCorsi = None
        self._btn_cercaStudente = None
        self._btn_iscrivi = None
        self._btn_clear = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)
        self._menuCorsi = ft.Dropdown(label="Selezionare un corso", options=[], width=600)
        self._controller.fill()
        #ROW with some controls
        # text field for the name
        # button for the "hello" reply
        self.btn_cercaIscritti = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handle_cercaIscritti, width=200)
        row1 = ft.Row([self._menuCorsi, self.btn_cercaIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._txt_matricola = ft.TextField(label="Matricola", width=200)
        self._txt_nome = ft.TextField(label="Nome", width=200, read_only=True)
        self._txt_cognome = ft.TextField(label="Cognome", width=200, read_only=True)
        row2 = ft.Row([self._txt_matricola, self._txt_nome, self._txt_cognome], alignment=ft.MainAxisAlignment.CENTER)
        self._btn_cercaStudente = ft.ElevatedButton(text="Cerca Studente", on_click=self._controller.handle_cercaStudente, width=200)
        self._btn_cercaCorsi = ft.ElevatedButton(text="Cerca Corsi", on_click=self._controller.handle_cercaCorsi, width=200)
        self._btn_iscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_iscrivi, width=200)
        self._btn_clear = ft.ElevatedButton(text="Clear", on_click=self._controller.handle_clear, width=200)
        row3 = ft.Row([self._btn_cercaStudente, self._btn_cercaCorsi, self._btn_iscrivi, self._btn_clear], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1, row2, row3)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
