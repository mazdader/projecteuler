import math

def find_sum_digits(num):
    summ = 0

    for digit in str(num):
        summ += int(digit)

    return summ



def solve():
    print find_sum_digits(int(math.pow(2,1000)))