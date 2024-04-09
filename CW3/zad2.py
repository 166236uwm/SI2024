decision_system = [
    {'a1': 'wysoka', 'a2': 'bliski', 'a3': 'średni', 'dec': 'tak'},
    {'a1': 'wysoka', 'a2': 'bliski', 'a3': 'średni', 'dec': 'tak'},
    {'a1': 'więcej niż średnia', 'a2': 'daleki', 'a3': 'silny', 'dec': 'nie pewne'},
    {'a1': 'więcej niż średnia', 'a2': 'daleki', 'a3': 'silny', 'dec': 'nie'},
    {'a1': 'więcej niż średnia', 'a2': 'daleki', 'a3': 'lekki', 'dec': 'nie'},
    {'a1': 'wysoka', 'a2': 'bliski', 'a3': 'średni', 'dec': 'tak'},
    {'a1': 'więcej niż średnia', 'a2': 'daleki', 'a3': 'lekki', 'dec': 'tak'}
]


def find_rule(cases, target_decision):
    attribute_counts = {attr: {} for attr in cases[0] if attr != 'dec'}

    for case in cases:
        if case['dec'] == target_decision:
            for attr, value in case.items():
                if attr != 'dec':
                    if value not in attribute_counts[attr]:
                        attribute_counts[attr][value] = 1
                    else:
                        attribute_counts[attr][value] += 1

    rule = {'dec': target_decision}
    for attr, counts in attribute_counts.items():
        if counts:
            rule[attr] = max(counts, key=counts.get)

    if len(rule) == 1:
        return None
    return rule


def is_covered_by_rule(case, rule):
    for attr, value in rule.items():
        if attr != 'dec' and case.get(attr) != value:
            return False
    return True


def sequential_covering(decision_system, target_decision):
    rules = []
    uncovered_cases = decision_system[:]

    while uncovered_cases:
        rule = find_rule(uncovered_cases, target_decision)
        if not rule:
            break
        rules.append(rule)

        uncovered_cases = [case for case in uncovered_cases if not is_covered_by_rule(case, rule)]

    return rules


rules = sequential_covering(decision_system, 'tak')
print("Wygenerowane reguły:")
for rule in rules:
    print(rule)

