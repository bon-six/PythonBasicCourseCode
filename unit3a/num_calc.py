
def add(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) :
        return 'Err: not numeric'
    return a+b

def multiply(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) :
        return 'Err: not numeric'
    return a*b
