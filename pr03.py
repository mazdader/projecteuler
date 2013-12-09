"""Project Euler problem 3 solve"""

import sys
from math import sqrt
 
 
def is_prime(num):
    """Checks if num is prime number"""
    for i in range(2, int(sqrt(num))):
        if not num % i:
            return False
    return True
 
 
def find_prime_factors(num):
    """Find prime factors of num"""
    result = []
    for i in range(2, int(sqrt(num))):
        if is_prime(i) and not num % i:
            result.append(i)
    return result
 
 
if __name__ == '__main__':
 
    prime_factors = find_prime_factors(600851475143)
    print prime_factors[-1]
