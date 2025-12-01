from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self.G = nx.Graph()

        spedizioni = DAO.get_spedizioni()

        archi_filtrati = [(n[0], n[1], n[2]) for n in spedizioni if n[2] >= threshold]

        nodi = set()
        for u, v, w in archi_filtrati:
            nodi.add(u)
            nodi.add(v)

        self.G.add_nodes_from(nodi)

        for u, v, w in archi_filtrati:
            self.G.add_edge(u, v, weight=w)


    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        num_edges = self.G.number_of_edges()
        return num_edges

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        num_nodi = self.G.number_of_nodes()
        return num_nodi

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        hub= DAO.get_hub()
        archi = [(hub[u], hub[v], d['weight']) for u, v, d in self.G.edges(data=True)]

        return archi



