from dataclasses import dataclass


@dataclass
class Corso:
    codins: str
    credits: int
    nome: str
    pd: int

    def __str__(self):
        return f'{self.nome} ({self.codins})'
