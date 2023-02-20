def sumdigits(n):
    """
    >>> sumdigits(7)
    7
    >>> sumdigits(228)
    12
    """
    all_but_last,last=n//10,n%10
    if(n<10):
        return n
    else :
        return last+sumdigits(all_but_last)


sumdigits(228)


