import numpy as np 
import pandas as pd 
import sympy
from collections import deque
def main():
    """This program prints the number of circular primes below one million 
    and the list of these primes."""
    primes = []
    for i in range(2,1000000):
        if sympy.isprime(i) and IsCircular(i): 
            primes.append(i)
    print(f'The number of circular primes below one million is {len(primes)}. ')
    print(primes)

#    primes = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
#     for i in range(100,1000000):
def IsCircular(prime): 
    """
    The function checks whether the number is circular prime,
    which is a prime number where all the rotations of its digits
    are also prime numbers.

    Input: prime number
    Output: Boolean, where True means that the number is circular 
    """
    circular = True 
    prime = list(str(prime))
    d = deque()
    [d.append(x) for x in prime]
    for i in range(1, len(prime)):
        d.rotate(1)
        rotated_prime = int("".join(list(d)))
        if not sympy.isprime(rotated_prime):
            circular = False
    return circular


#IsPrime function (optional)
# def IsPrime(number):
#     prime = True
#     for i in range(2, number): 
#         if (number % i) == 0: 
#             prime = False             
#     return prime



if __name__ == '__main__':
    main()
