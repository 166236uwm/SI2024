
def is_consistent(rule, objects, target_decision):
    for obj in objects:
        if all(obj[attr] == value for attr, value in rule.items()) and obj['d'] != target_decision:
            return False
    return True


def generate_single_attribute_rules(objects, target_decision):
    rules = []
    attributes = [attr for attr in objects[0].keys() if attr.startswith('a')]

    for attr in attributes:
        values = set(obj[attr] for obj in objects)
        for value in values:
            rule = {attr: value}
            if is_consistent(rule, objects, target_decision):
                rules.append(rule)

    return rules


def generate_double_attribute_rules(objects, single_attribute_rules, target_decision):
    rules = []
    attributes = [attr for attr in objects[0].keys() if attr.startswith('a')]

    for i in range(len(attributes)):
        for j in range(i + 1, len(attributes)):
            for obj in objects:
                rule = {attributes[i]: obj[attributes[i]], attributes[j]: obj[attributes[j]]}
                if any(rule[sa_attr] == sa_rule[sa_attr] for sa_rule in single_attribute_rules for sa_attr in sa_rule):
                    if is_consistent(rule, objects, target_decision):
                        rules.append(rule)

    return rules


def sequential_covering(objects, target_decision):
    uncovered_objects = objects[:]
    single_attribute_rules = generate_single_attribute_rules(uncovered_objects, target_decision)

    for rule in single_attribute_rules:
        uncovered_objects = [obj for obj in uncovered_objects if
                             not all(obj[attr] == value for attr, value in rule.items())]

    double_attribute_rules = generate_double_attribute_rules(uncovered_objects, single_attribute_rules, target_decision)

    for rule in double_attribute_rules:
        uncovered_objects = [obj for obj in uncovered_objects if
                             not all(obj[attr] == value for attr, value in rule.items())]

    return single_attribute_rules + double_attribute_rules



rules = sequential_covering(objects, 1)
for rule in rules:
    print(rule)