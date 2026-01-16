# Resolution-Based Theorem Prover

This repository contains a resolution-based theorem prover for propositional logic implemented in Python. The project supports classical resolution by refutation as well as an expert-system-style interactive mode (referred to as cooking mode) that allows querying, adding, and removing knowledge from a knowledge base.

The implementation operates on clauses written in Conjunctive Normal Form (CNF) and produces a resolution proof when a contradiction (NIL) is derived.

## Features

- Resolution by refutation for propositional logic
- Detailed resolution proof with parent clause references
- Set-of-support strategy
- Removal of tautological and redundant clauses
- Expert system mode with query, add, and remove operations
- Uses only the Python standard library

## Project Structure

The repository is organized as follows:

```
resolution-based-theorem-prover/
├── examples/
│ ├── cooking/
│ │ ├── cooking_chicken_broccoli.txt
│ │ ├── cooking_coffee_input.txt
│ │ ├── cooking_heldout_large.txt
│ │ └── new_pizza_input.txt
│ └── resolution/
│ ├── cooking_chicken_broccoli.txt
│ ├── new_example_5.txt
│ ├── new_example_6.txt
│ └── resolution_ai.txt
│
├── src/
│ ├── main.py
│ ├── parsing.py
│ ├── resolution.py
│ └── printing.py
│
├── README.md
├── .gitignore
└── LICENSE
```

The src directory contains the full implementation. The examples directory contains input files for both resolution mode and cooking mode.

## Requirements

- Python 3.x
- No external dependencies

## Input Format

Clause files contain one clause per line written in CNF. Disjunction is written using the symbol V, negation is written as ~ directly before a literal, and literals are case-insensitive. Lines starting with # are treated as comments and ignored. In resolution mode, the last clause in the file is treated as the goal clause.

Example clause file:

    ~a V b
    c V ~b

Cooking mode command files contain one command per line. Each command consists of a clause followed by a command identifier. The identifier ? represents a query, + represents adding a clause to the knowledge base, and - represents removing a clause from the knowledge base.

Example command file:

    water ?
    heater +
    coffee -

## Usage

All commands are executed from the src directory.

Resolution mode runs classical resolution by refutation on a clause set:

python main.py resolution ../examples/resolution/resolution_ai.txt

If the goal clause is proven, the program prints the resolution proof followed by a conclusion line. If the goal cannot be proven, only the conclusion line is printed. The output always ends with one of the following lines:

    [CONCLUSION]: clause is true
    [CONCLUSION]: clause is unknown

Cooking mode runs an expert system that processes user commands sequentially:

python main.py cooking ../examples/cooking/cooking_chicken_broccoli.txt ../examples/cooking/cooking_coffee_input.txt

Only query commands produce output. Add and remove commands modify the knowledge base silently.

## Output Format

When a proof is found, the output contains the initial clauses, all derived clauses used to obtain NIL, references to parent clauses for each derived clause, separator lines, and a final conclusion line starting with [CONCLUSION]:. Only clauses that contribute to the derivation of NIL are printed.

## Algorithm Overview

The algorithm negates the goal clause and adds it to the set of support. Resolution is applied iteratively using breadth-first search. Complementary literals are resolved to produce new clauses, while tautological and subsumed clauses are removed. If the empty clause (NIL) is derived, the goal clause is proven true. If no contradiction is found, the goal clause is reported as unknown.

## Concepts Demonstrated

- Automated theorem proving
- Resolution in propositional logic
- Knowledge base management
- Expert systems
- Logical inference