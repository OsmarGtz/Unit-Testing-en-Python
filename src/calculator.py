
def sum(a, b):
    '''
    >>> sum(5, 7)
    12
    '''
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    '''
    >>> divide(10, 0)
    Traceback (most recent call last):
    ValueError: Divide by zero is not allow
    '''
    if b == 0:
        raise ValueError("Divide by zero is not allow")
    return a / b

def multiply(a, b):
    return a * b