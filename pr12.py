"""Project Euler problem 12 solve"""

import sys, math
 
 
def find_triangles(last=0,summ=0):
    return summ + last + 1
 
 
def find_num_divisors(num):
    i = 0
    summ = 0
    counter = 0
    last_divisor = 1
    while counter < num:
        i += 1
        summ += i
        counter = 0
        
        sqrt_num = int(math.sqrt(summ))
        
        for j in range(1,sqrt_num+1):
            if not summ % j:
                counter += 1
    return [summ,i,counter]
 
 
if __name__ == '__main__':
    print find_num_divisors(500)
