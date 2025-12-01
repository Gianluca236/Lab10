import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO

        if not self._view.guadagno_medio_minimo.value.isdigit():
            self._view.show_alert('inserisci valore valido')
            return None

        self._model.costruisci_grafo(float(self._view.guadagno_medio_minimo.value))

        num_hub = self._model.get_num_nodes()
        num_tratte = self._model.get_num_edges()
        tratte= self._model.get_all_edges()

        self._view.lista_visualizzazione.controls.clear()
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Hub: {num_hub}"))
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Tratte: {num_tratte}"))
        self._view.lista_visualizzazione.controls.append(ft.Text('-'*30))

        for tratta in tratte:
            self._view.lista_visualizzazione.controls.append(ft.Text(f"{tratta[0]} --> {tratta[1]} --> Guadagno medio per spedizione:{tratta[2]}$"))

        self._view.update()

