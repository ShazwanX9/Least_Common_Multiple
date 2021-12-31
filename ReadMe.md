# Least Common Multiple

___
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

    Our lcm function receive a number of int and compute the lcm of all arguments
    Formula used: lcm(a,b) = a*b / gcd(a,b)
___

    Required:
        :*param: -> int     - n
        :return: -> int     - the least common multiple of all param

    Example:
        lcm(39, 3, 14, 14, 3, 7, 14, 21, 5, 12, 23, 22, 16, 11, 23, 12, 16, 18, 1)
            => 16576560

## DISCLAIMER!
    no guarantee of completeness, accuracy, timeliness or 
    of the results obtained from the use of this information

### For more information:
	Visit [Wikipedia](https://en.wikipedia.org/wiki/Combination)