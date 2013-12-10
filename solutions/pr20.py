def factor(curr, summ = 1):
    if curr != 1:
        summ = factor(curr - 1, summ)
    return summ * curr

def sum_digits(num):
    summ = 0
    for i in str(num):
        summ += int(i)
    return summ

def solve():
    print sum_digits(factor(100))
