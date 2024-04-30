
def PL_RESOLUTION(KB, alpha):
    clauses = KB + [negate([alpha])]  # Dodaj negację alpha do KB
    new = set()

    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i + 1, n)]

        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            if [] in resolvents:  # Pusta klauzula oznacza sukces
                return True
            new.update(tuple(sorted(clause)) for clause in resolvents)

        if new.issubset({tuple(clause) for clause in clauses}):  # Brak nowych klauzul oznacza niepowodzenie
            return False
        clauses.extend(list(clause) for clause in new)
        new.clear()


def negate(clause):
    negated_clause = []
    for literal in clause:
        if literal.startswith('~'):
            negated_clause.append(literal[1:])  # Usuń negację
        else:
            negated_clause.append('~' + literal)  # Dodaj negację
    return negated_clause


def resolve(ci, cj):
    resolvents = []
    for li in ci:
        for lj in cj:
            if li == negate_literal(lj):
                new_clause = set(ci) | set(cj)
                new_clause.discard(li)
                new_clause.discard(lj)
                if len(new_clause) == 0:
                    resolvents.append([])  # Pusta klauzula
                else:
                    resolvents.append(list(new_clause))
    return resolvents


def negate_literal(literal):
    return literal[1:] if literal.startswith('~') else '~' + literal


KB = [['~B1,2', 'S1,2'], ['~W1,1'], ['B1,2']]
alpha = 'S1,2'

result = PL_RESOLUTION(KB, alpha)
print("Czy KB implikuje alpha? ", result)
