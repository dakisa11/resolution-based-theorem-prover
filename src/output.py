from clause_utils import klauzaUstring


def print_resolution_chain(roditelj):
    inverted = {v: k for k, v in roditelj.items()}

    pocetne = {
        v: klauzaUstring(k)
        for v, k in inverted.items()
        if isinstance(v, int)
    }

    for i in sorted(pocetne):
        print(f"{i}. {pocetne[i]}")
    print("=" * 15)
