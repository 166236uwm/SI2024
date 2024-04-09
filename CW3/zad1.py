variables = ['X1', 'X2', 'X3']
domains = {
    'X1': ['R', 'B', 'G'],
    'X2': ['R'],
    'X3': ['G']
}


def is_consistent(assignment, variable, value):
    for other_variable, other_value in assignment.items():
        if other_variable == variable:
            continue
        if other_value == value:
            return False
    return True


def select_unassigned_variable(assignment):
    candidates = [v for v in variables if v not in assignment]

    return min(candidates, key=lambda var: len(domains[var]))


def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment

    variable = select_unassigned_variable(assignment)

    # Sprawdzenie domeny zmiennej
    for value in domains[variable]:
        if is_consistent(assignment, variable, value):
            local_assignment = assignment.copy()
            local_assignment[variable] = value
            result = backtrack(local_assignment)
            if result is not None:
                return result

    return None


solution = backtrack({})
print(solution)