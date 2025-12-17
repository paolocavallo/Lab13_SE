from dataclasses import dataclass


@dataclass
class Classificazione:
    id_gene : str
    localizzazione : str


    def __eq__(self, other):
        return isinstance(other, Classificazione) and self.id_gene == other.id_gene

    def __str__(self):
        return f"{self.id_gene} {self.localizzazione}"

    def __repr__(self):
        return f"{self.id_gene} {self.localizzazione}"

    def __hash__(self):
        return hash((self.id_gene, self.localizzazione))