def sheff(A, B):
    if not A and not B:
        return True
    if not A or not B:
        return B if not A else A
    return False
