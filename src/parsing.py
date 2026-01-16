def parser(KR, FILE_PATH, FILE_PATH1):

    with open(FILE_PATH, "r") as file:
        ulazni_niz = file.read()

    if KR == "resolution":
        klazule = []
        cilj = []
        for linija in ulazni_niz.split("\n"):
            if linija.startswith("#") or linija == "":
                continue
            klazula = set(linija.upper().strip().split(" V "))
            klazule.append(klazula)

        ciljna_klazula = set(klazule.pop())
        for literal in ciljna_klazula:
            cilj.append({literal})

        cilj.sort()
        return klazule, cilj

    if FILE_PATH1:
        with open(FILE_PATH1, "r") as file1:
            ulazni_niz1 = file1.read()

    if KR == "cooking":
        klazule = []
        upute = []

        for linija in ulazni_niz.split("\n"):
            if linija.startswith("#") or linija == "":
                continue
            klazula = set(linija.upper().strip().split(" V "))
            klazule.append(klazula)

        for linija in ulazni_niz1.split("\n"):
            if linija.startswith("#") or linija == "":
                continue
            uputa = set(linija.upper().strip().split(" "))
            upute.append(uputa)

        return klazule, upute
