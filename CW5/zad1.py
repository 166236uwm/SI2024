def pl_true(S, m):
    if isinstance(S, str) and S in m:
        return m[S]
    if S[0] == '¬':
        operand = S[1]
        return not pl_true(operand, m)
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
S = ('p', '∧', ('¬', 'q'))  # p ∧ ¬q
m = {'p': True, 'q': False}

print(pl_true(S, m))
