def pl_true(S, m):
    # Recursive function to evaluate the truth of a logical expression S under the assignment m

    # If S is a simple variable, return its value from the assignment m
    if isinstance(S, str) and S in m:
        return m[S]

    # Handle NOT operation
    if S[0] == '¬':
        operand = S[1]
        return not pl_true(operand, m)

    # Handle AND, OR, IMPLICATION operations
    op = S[1]
    left = S[0]
    right = S[2]

    if op == '∧':
        return pl_true(left, m) and pl_true(right, m)
    elif op == '∨':
        return pl_true(left, m) or pl_true(right, m)
    elif op == '⇒':
        return not pl_true(left, m) or pl_true(right, m)
    else:
        raise ValueError("Unsupported logical connective")


# Example usage:
S = ('p', '∧', ('¬', 'q'))  # Represents the logical expression p ∧ ¬q
m = {'p': True, 'q': False}  # p is True and q is False

print(pl_true(S, m))  # Output should be True since p is True and ¬q is True (q is False)
