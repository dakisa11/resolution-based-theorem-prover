import queue
from printing import print_resolution_chain


def negiraj(izraz):
    if izraz.startswith("~"):
        return izraz[1:]
    else:
        return '~' + izraz


def tautologije(klazule):
    nisu = klazule.copy()
    for klazula in klazule:
        for literal in klazula:
            neg_literal = negiraj(literal)
            if neg_literal in klazula:
                if klazula in nisu:
                    nisu.remove(klazula)
                break
    return nisu


def apsorpcija(klazule):
    bezRedundantnih = klazule.copy()
    for c1 in klazule:
        if c1 == "NIL":
            continue
        for c2 in klazule:
            if c1 == c2 or c2 not in bezRedundantnih:
                continue
            if c1.issubset(c2):
                if c2 in bezRedundantnih:
                    bezRedundantnih.remove(c2)
    return bezRedundantnih


def pocisti(klazula):
    return apsorpcija(tautologije(klazula))


def rezoliraj(k1, k2, roditelj, brojRoditelja):
    k1 = set(k1)
    nova_klauzula = set()

    for literal1 in k1:
        negacija = negiraj(literal1)
        if negacija in k2:
            nova_klauzula = (k1 - {literal1}) | (k2 - {negacija})
            if not nova_klauzula:
                nova_klauzula = {'NIL'}

            roditelj[frozenset(nova_klauzula)] = (
                "redak: " + str(brojRoditelja),
                roditelj[frozenset(k1)],
                roditelj[frozenset(k2)]
            )
            brojRoditelja += 1
            return nova_klauzula, brojRoditelja

    return False, brojRoditelja


def formatirajRoditelje(klazule, roditelj, brRod):
    for j, roditeljskeKlazule in enumerate(klazule, start=brRod):
        roditelj[frozenset(roditeljskeKlazule)] = j
        brRod += 1
    return roditelj, brRod


def rezolucija(klazule, cilj, cooking):
    baza_znanja = klazule.copy()
    sos = queue.Queue()
    posjeceni = []
    roditelj = {}
    brojRoditelja = 1
    negCilj = []

    roditelj, brojRoditelja = formatirajRoditelje(
        klazule, roditelj, brojRoditelja
    )

    for klazulaCilja in cilj:
        if not cooking:
            for literalCilja in klazulaCilja:
                negLiteralCilja = {negiraj(literalCilja)}
                if negLiteralCilja not in posjeceni:
                    negCilj.append(negLiteralCilja)
                    sos.put(negLiteralCilja)
        else:
            negKlazulaCilja = {negiraj(klazulaCilja)}
            negCilj.append(negKlazulaCilja)
            sos.put(negKlazulaCilja)

    roditelj, brojRoditelja = formatirajRoditelje(
        negCilj, roditelj, brojRoditelja
    )

    while not sos.empty():
        trenutna_klauzula = sos.get()
        posjeceni.append(trenutna_klauzula)

        if trenutna_klauzula == {'NIL'}:
            if not cooking:
                print_resolution_chain(roditelj)
            return True

        nove_klauzule = []

        for klazula in baza_znanja:
            if trenutna_klauzula == klazula:
                continue
            rez, brojRoditelja = rezoliraj(
                trenutna_klauzula, klazula, roditelj, brojRoditelja
            )
            if rez:
                nove_klauzule.append(rez)

        if nove_klauzule:
            nove_klauzule = pocisti(nove_klauzule)
            for nova in nove_klauzule:
                if nova not in baza_znanja and nova not in posjeceni:
                    sos.put(nova)
                    baza_znanja.append(nova)
                    baza_znanja = pocisti(baza_znanja)

    return False
