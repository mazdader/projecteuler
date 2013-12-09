"""Project Euler problem 7 solve"""

import math

def is_prime(num):
    """Checks if num is prime number"""
    for i in range(2, int(math.sqrt(num)) + 1):
        if not num % i:
            return False
    return True


def find_prime_at_pos(pos):
    primes_count = 0
    curr = 1
    while primes_count < pos:
        curr += 1
        if is_prime(curr):
            primes_count += 1
    return curr


if __name__ == '__main__':
    print find_prime_at_pos(10001)

