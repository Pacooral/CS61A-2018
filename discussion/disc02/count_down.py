def count_down( n ) :
    """
    >>> countdown(3)
    3
    2
    1
    """
    print(n)
    if n==1:
        return None
    else :
        return count_down(n-1)

