from dataclasses import dataclass


@dataclass
class Interazione:
    id_gene1 : str
    id_gene2 : str
    tipo : str
    correlazione : float

    def __eq__(self, other):
        return isinstance(other, Interazione) and self.tipo == other.tipo

    def __str__(self):
        return f"{self.id_gene1} {self.id_gene2} {self.tipo} {self.correlazione}"

    def __repr__(self):
        return f"{self.id_gene1} {self.id_gene2} {self.tipo} {self.correlazione}"

    def __hash__(self):
        return hash((self.id_gene1, self.id_gene2, self.tipo, self.correlazione))