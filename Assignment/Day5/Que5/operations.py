def add(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be int or float.")
    return a + b


def multiply(a, b):
    
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be int or float.")
    return a * b

def reverse_string(s):
    if not isinstance(s, str):
        raise TypeError("Argument must be a string.")
    return s[::-1]