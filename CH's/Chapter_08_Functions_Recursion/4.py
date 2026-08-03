def sums(n):
    """
    Returns the sum of all integers from 1 to n.
    """
    if n == 1:
        return 1
    else:
        return n + sums(n - 1)