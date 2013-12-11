def fibonacci(num):
    if num==1 or num==2:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)

def fibonacci_cheat(n):
    phi = (1 + pow(5, 0.5))/2
    return int((pow(phi, n) - pow(-phi, -n))/pow(5, 0.5))

def solve():
    i = 1

    a, b = 1, 1
    x = 2
    while len(str(b)) < 1000:
        a, b = b, a+b
        x += 1
    print x
