def klauzaUstring(fset):
    if fset == frozenset({'NIL'}):
        return "NIL"
    return " v ".join(sorted(fset, reverse=True))


def print_resolution_chain(roditelj):
    inverted = {}
    for key, value in roditelj.items():
        inverted[value] = key

    pocetneKlazule = {}
    for value, key in inverted.items():
        if isinstance(value, int):
            pocetneKlazule[value] = klauzaUstring(key)

    for broj in sorted(pocetneKlazule):
        print(f"{broj}. {pocetneKlazule[broj]}")
    print("=" * 15)

    processed = {}
    noviBroj = max(pocetneKlazule.keys()) + 1
    korakRezolucije = []

    def process(node):
        nonlocal noviBroj

        if isinstance(node, int):
            return node

        if node in processed:
            return processed[node]

        redak_str, lijevo, desno = node

        brLijevo = process(lijevo)
        brDesno = process(desno)
        brDjeca = sorted([brLijevo, brDesno])

        current = noviBroj
        noviBroj += 1

        klauzaFSet = inverted.get(node, frozenset())
        klauzaStr = klauzaUstring(klauzaFSet)

        korakRezolucije.append((current, klauzaStr, tuple(brDjeca)))
        processed[node] = current
        return current

    pocNode = roditelj[frozenset({'NIL'})]
    process(pocNode)

    korakRezolucije.sort(key=lambda x: x[0])
    for broj, clause, refs in korakRezolucije:
        print(f"{broj}. {clause} {refs}")
    print("=" * 15)
