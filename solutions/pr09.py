"""Project Euler problem 9 solve"""

import sys

def find_all_values(num):
    result=0
    for a in range(1,num-1):
        for b in range(a+1,num):
            for c in range(b+1,num+1):
                if a+b+c == num:
                    if a*a + b*b == c*c:
                        result = a*b*c
    return result
 
def find_triplet(target):
    return result
 
 
def solve():
    print find_all_values(1000)
    
