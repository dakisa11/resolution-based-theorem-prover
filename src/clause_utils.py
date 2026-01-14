def negiraj(izraz):
    if izraz.startswith("~"):
        return izraz[1:]
    return "~" + izraz


def klauzaUstring(fset):
    if fset == frozenset({'NIL'}):
        return "NIL"
    return " v ".join(sorted(fset, reverse=True))
