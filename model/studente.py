from dataclasses import dataclass


@dataclass
class Studente:
    matricola: str
    cognome: str
    nome: str
    CDS: str

    def __str__(self):
        return f'{self.matricola} ({self.nome})'

    def __eq__(self, other):
        return self.matricola == other.codins

    def __hash__(self):
        return hash(self.matricola)
