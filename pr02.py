"""Project Euler problem 2 solve"""
import sys
 
 
def create_fibonacci(num):
    result = [1,2]
    while num >= result[-1]:
        result.append(result[-1] + result[-2])
    return result
 
 
def find_sum_even(seq):
    result = 0
    for i in seq:
        if not i % 2:
            result += i
    return result
 
 
if __name__ == '__main__':
    print find_sum_even(create_fibonacci(4000000))
