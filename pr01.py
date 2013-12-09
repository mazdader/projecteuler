"""Project Euler problem 1 solve"""
import sys
 
def find_sum(num):
    result = 0
    for i in range(1, num):
        if not i % 3 or not i % 5:
            result += i
    return result
 
 
if __name__ == '__main__':
    print find_sum(1000)

"""    
    try:
        num = int(sys.argv[1])
    except (TypeError, ValueError, IndexError):
        sys.exit("Usage: pr1.py number")
    if num < 1:
        sys.exit("Error: number must be greater than zero")
 
    prime_factors = find_prime_factors(num)
    if len(prime_factors) == 0:
        print("Can't find prime factors of %d" % num)
    else:
        print("Answer: %d" % prime_factors[-1])
"""
