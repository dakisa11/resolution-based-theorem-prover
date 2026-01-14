from clause_utils import negiraj


def tautologije(klazule):
    rezultat = klazule.copy()
    for klazula in klazule:
        for literal in klazula:
            if negiraj(literal) in klazula:
                if klazula in rezultat:
                    rezultat.remove(klazula)
                break
    return rezultat


def apsorpcija(klazule):
    rezultat = klazule.copy()
    for c1 in klazule:
        for c2 in klazule:
            if c1 != c2 and c1.issubset(c2) and c2 in rezultat:
                rezultat.remove(c2)
    return rezultat


def pocisti(klazule):
    return apsorpcija(tautologije(klazule))
