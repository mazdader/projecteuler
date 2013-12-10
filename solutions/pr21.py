def sum_divisors(num):
    summ = 0
    for i in range(1,(num // 2) + 1):
        if num % i == 0:
            summ += i
    return summ

def find_amicables(num):
    summs_divisors = []
    amicables = []

    for i in range(1, num+1):
        summs_divisors.append([i, sum_divisors(i)])

    for i in summs_divisors:
        if ([i[1],i[0]] in summs_divisors) and i[1] != i[0]:
            amicables.append(i)

    summ = 0
    for i in amicables:
        summ += i[0]

    return summ

def solve():
    print find_amicables(10000)
    pass