def mul(m,n) :
    assert m>=0,'m should be positive number'
    assert n>=0,'n should be positive number'
    if n==1 :
        return m
    else :
        return mul(m,n-1)+m

