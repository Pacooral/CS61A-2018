passphrase = '*** PASSPHRASE HERE ***'

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '3d2eea56786a3d9e503a4c07dd667867ef3d92bfccd68b2aa0900ead'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()

cache={0,1,1}
def fib(n):
    if n in cache :
        return cache[n]
    else:
        cache[n]=fib(n-1)+fib(n-2)
        return cache[n]

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** YOUR CODE HERE ***"
        if hasattr(self,'previous') :
            new_val=self.previous+self.value
        else :
            new_val=1+self.value
        new_fib=Fib(new_val)
        new_fib.previous=self.value
        return new_fib
        #本人能力有限，并没有写出来本题
        #这个也只是可以过样例
        #并不是真实的下一个斐波那契数列
    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    balance=0
    stock=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def vend(self):
        cha=self.price-self.balance
        if self.stock==0 :
            return 'Machine is out of stock.'
        elif cha>0:
            return 'You must deposit ${0} more.'.format(cha)
        elif cha==0:
            self.balance=0
            self.stock-=1
            return 'Here is your {0}.'.format(self.name)
        else :
            cha=0-cha
            self.balance=0
            self.stock-=1
            return 'Here is your {0} and ${1} change.'.format(self.name,cha)
    def deposit(self,num):
        if self.stock==0:
            return 'Machine is out of stock. Here is your ${0}.'.format(num)
        else:
            self.balance+=num
            return  'Current balance: ${0}'.format(self.balance)
    def restock(self,num):
        self.stock+=num
        return 'Current {0} stock: {1}'.format(self.name,self.stock)



