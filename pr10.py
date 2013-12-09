"""Project Euler problem 1 solve"""

import sys,math

def is_prime(num):
    """Checks if num is prime number"""
    for i in range(2, int(math.sqrt(num)) + 1):
        if not num % i:
            return False
    return True 
 
def find_prime_sum(num):
    """Find prime factors of num"""
    result = 0
    for i in range(2, num):
        if is_prime(i):
            result += i
    return result
 
 
if __name__ == '__main__':
    print find_prime_sum(2000000)
