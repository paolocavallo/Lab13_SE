import flet as ft
import networkx as nx

from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        #grafo = self._model.build_grafo()
        #num_nodi = grafo.number_of_nodes()
        #num_archi = grafo.number_of_edges()

        num_nodes, num_edges = self._model.build_grafo()
        peso_min, peso_max = self._model.trova_valori_min_max()

        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Il grafo ha {num_nodes} nodi e {num_edges} archi\nvalore minimo: {peso_min}, valore maximo: {peso_max}"))
        self._view.update()



    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        # TODO
        soglia = self._view.txt_name.value
        if 3<=int(soglia)<=7:
            edges_minori, edges_maggiori = self._model.conta_edges(soglia)
            self._view.lista_visualizzazione_2.controls.clear()
            self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Numero di archi con peso maggiore della soglia: {edges_maggiori}\nNumero di archi con peso minori della soglia: {edges_minori} "))
            self._view.update()
        else:
            self._view.lista_visualizzazione_2.controls.clear()
            self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Scegliere una soglia valida"))
            self._view.update()


    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        # TODO