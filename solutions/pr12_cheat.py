import math

def main():
    l = []
    one = 0
    a = 1
    b = 2
    while one == 0:
        a = a + b 
        b += 1
        l = []

        sqrt_a = int(math.sqrt(a))
        sqrt_a_dec = math.sqrt(a)

        for x in range(1, sqrt_a + 1):
            if a % x == 0:
                l.append(x)
                if x < sqrt_a_dec:
                    l.append(a // x)
                if len(l) > 500:
                    # print(a)
                    one = 1
        if a > 70576500:
            print a

    print(a, b, len(l))

def solve():
    main()
