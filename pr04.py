"""Project Euler problem 4 solve"""

import math 

def int_to_list(i):
    return [int(x) for x in str(i).zfill(len(str(i)))]

def find_palindromes(num):
    palindromes = []
    for i in range(find_min_num(num), find_max_num(num)):
        if int(str(i)[::-1]) == i:
            palindromes.append(i)
    return palindromes

def find_max_num(num_of_digits):
    result = int(pow(math.pow(10, num_of_digits) - 1, 2))
    return result

def find_min_num(num_of_digits):
    result = int(pow(math.pow(10, num_of_digits-1), 2))
    return result 
 
if __name__ == '__main__':
    num = 3
    print find_min_num(num)
    print find_max_num(num)
    print find_palindromes(num)[-1]
    