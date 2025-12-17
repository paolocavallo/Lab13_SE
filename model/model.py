import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.DiGraph()



    def build_grafo(self):
        self.G.clear()
        lista_geni = DAO().get_geni()
        lista_cromosomi = []

        for gene in lista_geni:
            if gene.cromosoma != 0:
                lista_cromosomi.append(gene.cromosoma)
        self.G.add_nodes_from(lista_cromosomi)
        lista_interazioni = DAO().get_interazioni()
        for interazione in lista_interazioni:
            if interazione["cromosoma1"] in lista_cromosomi and interazione["cromosoma2"] in lista_cromosomi:
                self.G.add_edge(interazione["cromosoma1"], interazione["cromosoma2"], weight=interazione["peso"])
        #for interazione in lista_interazioni:
            #self.G.add_edge(interazione["cromosoma1"], interazione["cromosoma2"], weight=interazione["peso"])
        num_nodi = self.G.number_of_nodes()
        num_archi = self.G.number_of_edges()
        return num_nodi, num_archi

    def trova_valori_min_max(self):
        min = 100000
        max = -100000
        for u, v, data in self.G.edges(data=True):
            if data["weight"] < min:
                min = data["weight"]
            elif data["weight"] > max:
                max = data["weight"]
        return min, max

    def conta_edges(self, soglia):
        edges_minori = 0
        edges_maggiori = 0
        for u, v, data in self.G.edges(data=True):
            peso = data["weight"]
            if peso < int(soglia):
                edges_minori += 1
            elif peso > int(soglia):
                edges_maggiori += 1
        return edges_minori, edges_maggiori