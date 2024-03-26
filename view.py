import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page

        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page
        self._DdSelettore_lingua = None
        self._DdSelettore_algoritmo = None
        self._testo_da_tradurre = None
        self._btnStart = None
        self._txt_output = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)

        self.page.controls.append(ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                                         alignment=ft.MainAxisAlignment.START))

        # Add your stuff here
        self._confermato_lingua = ft.TextField(value="you must select a language", width=250)
        self._DdSelettore_lingua = ft.Dropdown(label = "Language", width=750, on_change=self._conferma_Selezione_lingua)
        self._fill_selettore_lingua()

        self._confermato_algoritmo = ft.TextField(value="you must select an option", width=200)
        self._DdSelettore_algoritmo = ft.Dropdown(label="Choose the research algorthm", width=250, on_change=self._conferma_Selezionato_algoritmo)
        self._fill_selettore_algortimo()

        self._testo_da_tradurre = ft.TextField(label="Text you want to check", width=620)

        self._btnStart = ft.ElevatedButton(text="Spell Check", on_click=self._handleSpellCheck, width=150)

        row1 = ft.Row([self._DdSelettore_lingua, self._confermato_lingua])
        row2 = ft.Row([self._DdSelettore_algoritmo,self._confermato_algoritmo, self._testo_da_tradurre, self._btnStart])

        self.page.add(row1, row2, self._txt_output)

        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()


    def _fill_selettore_lingua(self):
        for i in ["None", "english", "italian", "spanish"]:
            self._DdSelettore_lingua.options.append(ft.dropdown.Option(i))

    def _fill_selettore_algortimo(self):
        for i in ["None", "Default", "Linear", "Dichotomic"]:
            self._DdSelettore_algoritmo.options.append(ft.dropdown.Option(i))

    def _conferma_Selezione_lingua(self, e):
        if self._DdSelettore_lingua.value != "None":
            self._confermato_lingua.value = f"{self._DdSelettore_lingua.value} selected"
        else:
            self._confermato_lingua = ft.TextField(value="you must select a language", width=250)
        self.page.update()
    def _conferma_Selezionato_algoritmo(self, e):
        if self._DdSelettore_lingua.value != "None":
            self._confermato_algoritmo.value = f"{self._DdSelettore_algoritmo.value} selected"
        else:
            self._confermato_algoritmo = ft.TextField(value="you must select an option", width=200)
        self.page.update()

    def _handleSpellCheck(self, e):
        if self._DdSelettore_lingua.value != "None" and self._DdSelettore_algoritmo.value != "None" and self._testo_da_tradurre.value != "":
            risultato = self.__controller.handleSentence(self._testo_da_tradurre.value, self._DdSelettore_lingua.value,
                                             self._DdSelettore_algoritmo.value)
            self._txt_output.controls.append(ft.Text(value=f"Frase inserita: {self._testo_da_tradurre.value}\n"
                                                           f"parole errate:{risultato[0]}\n"
                                                           f"tempo richiesto: {risultato[1]}\n"))
            self.page.update()
            self._DdSelettore_lingua.value = "None"
            self._DdSelettore_algoritmo.value = "None"
            self._testo_da_tradurre = "None"
            self._conferma_Selezione_lingua
            self._conferma_Selezionato_algoritmo
            self.page.update()

        else:
            pass
