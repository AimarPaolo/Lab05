from dataclasses import dataclass


@dataclass
class Corso:
    codins: str
    credits: int
    nome: str
    pd: int


    def __str__(self):
        return f'{self.nome} ({self.codins})'

    def __eq__(self, other):
        return self.codins == other.codins

    def __hash__(self):
        return hash(self.codins)
