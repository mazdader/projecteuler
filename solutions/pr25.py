def fibonacci(num):
    if num==1 or num==2:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)

def solve():
    i = 1
    last_len = len(str(fibonacci(i)))
    while last_len != 1000:
        i += 1
        last_len = len(str(fibonacci(i)))

    print i