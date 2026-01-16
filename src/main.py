import sys
from parsing import parser
from resolution import rezolucija
from printing import klauzaUstring


def main():
    KR = sys.argv[1]
    FILE_PATH = sys.argv[2]

    if KR == "cooking":
        FILE_PATH1 = sys.argv[3]

    if KR == "resolution":
        klazule, cilj = parser(KR, FILE_PATH, None)
        rezultat = rezolucija(klazule, cilj, 0)

        pCilj = ""
        for c in cilj:
            if pCilj != "":
                pCilj += " v "
            pCilj += " v ".join(c).lower()

        if rezultat:
            print(f"[CONCLUSION]: {pCilj} is true")
        else:
            print(f"[CONCLUSION]: {pCilj} is unknown")

    elif KR == "cooking":
        klazule, upute = parser(KR, FILE_PATH, FILE_PATH1)

        for uputa in upute:
            if {'?'}.issubset(uputa):
                upit = (uputa - {'?'})
                rezultat = rezolucija(klazule, upit, 1)
                if rezultat:
                    print(f"[CONCLUSION]: {klauzaUstring(upit).lower()} is true")
                else:
                    print(f"[CONCLUSION]: {klauzaUstring(upit).lower()} is unknown")

            if {'-'}.issubset(uputa):
                klazula = (uputa - {'-', 'V'})
                if klazula in klazule:
                    klazule.remove(klazula)

            if {'+'}.issubset(uputa):
                klazula = (uputa - {'+', 'V'})
                if klazula not in klazule:
                    klazule.append(klazula)

    else:
        print("Greška: nepoznata opcija.")


if __name__ == "__main__":
    main()
