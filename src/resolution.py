import queue
from clause_utils import negiraj
from cleanup import pocisti


def rezoliraj(k1, k2, roditelj, brojRoditelja):
    k1 = set(k1)

    for literal in k1:
        neg = negiraj(literal)
        if neg in k2:
            nova = (k1 - {literal}) | (k2 - {neg})
            if not nova:
                nova = {'NIL'}
            roditelj[frozenset(nova)] = (
                f"redak: {brojRoditelja}",
                roditelj[frozenset(k1)],
                roditelj[frozenset(k2)]
            )
            return nova, brojRoditelja + 1

    return False, brojRoditelja

def rezolucija(klazule, cilj, cooking, print_chain):
    baza = klazule.copy()
    sos = queue.Queue()
    posjeceni = []
    roditelj = {}
    broj = 1

    for k in klazule:
        roditelj[frozenset(k)] = broj
        broj += 1
