def parser(mode, path1, path2=None):
    with open(path1) as f:
        lines = f.read().splitlines()

    if mode == "resolution":
        clauses = []
        for line in lines:
            if line and not line.startswith("#"):
                clauses.append(set(line.upper().split(" V ")))
        goal = clauses.pop()
        return clauses, [{l} for l in goal]
