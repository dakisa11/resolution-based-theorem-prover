import sys
from parser import parser
from resolution import rezolucija
from output import print_resolution_chain


def main():
    mode = sys.argv[1]

    if mode == "resolution":
        clauses, goal = parser(mode, sys.argv[2])
        result = rezolucija(clauses, goal, False, print_resolution_chain)

        goal_str = " v ".join(l.lower() for g in goal for l in g)
        print(f"[CONCLUSION]: {goal_str} is {'true' if result else 'unknown'}")
