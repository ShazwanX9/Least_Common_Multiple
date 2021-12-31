"""
In arithmetic and number theory, 
    - least     common multiple
    - lowest    common multiple
    - smallest  common multiple 
of two integers a and b, usually denoted by lcm(a, b), 
is the smallest positive integer that is divisible by both a and b.

Since division of integers by zero is undefined, 
this definition has meaning only if a and b are both different from zero.
However, some authors define lcm(a,0) as 0 for all a, 
which is the result of taking the lcm to be the 
least upper bound in the lattice of divisibility.
(and in our case, we did the same returning 0 for any case 0)

Our lcm function batch compute all least common multiple of *args recursively
Formula used: lcm(a,b) = a*b / gcd(a,b)
"""

from math import gcd
def lcm(*args:int) -> int:
    """
    Batch compute least common multiple of *args
    :param *args:   -> int     - n
    :return:        -> int     - the least common multiple of all param
    """
    size = len(args)
    if not size : return -1
    if size==1  : return args[0]
    if size==2  : return args[0]*args[1]//(gcd(args[0],args[1]) or 1)
    left  = lcm(*args[:size//2])
    right = lcm(*args[size//2:])
    return lcm(left,right)

if __name__ == "__main__":
    print("Testing for " + __file__)

    result = lambda q, a, e: f"COMPUTE FOR `{q}`: \n\t => RESULT = `{a}`, EXPECTED = `{e}`, WORKS = `{a==e}`"

    q, e = (2, 3), 6
    print(result(q,lcm(*q),e))

    q, e = (2, 3, 5), 30
    print(result(q,lcm(*q),e))

    q, e = (), -1
    print(result(q,lcm(*q),e))

    q, e = (1, 3, 7, 9, 14, 32), 2016
    print(result(q,lcm(*q),e))

    q, e = (39, 3, 14, 14, 3, 7, 14, 21, 5, 12, 23, 22, 16, 11, 23, 12, 16, 18, 1), 16576560
    print(result(q,lcm(*q),e))