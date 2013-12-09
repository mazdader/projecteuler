"""Project Euler problem 6 solve"""

from math import pow
 
def find_sum_squares(num):
    sum = 0
    for i in range(1,num+1):
        sum += pow(i,2)
    return int(sum)
 
 
def find_square_sum(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    return int(pow(sum,2))
 
 
def solve():
    num = 100
    print find_square_sum(num) - find_sum_squares(num)
    
