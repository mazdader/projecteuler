def find_recurring_cycle(num):
    if num == 1:
        return 1
    j = 1
    while True:
        cycle = str(int(pow(10, j) // num))
        if cycle[-1] == '0':
            return cycle[:-1]
        j += 1
        for i in range(1, len(cycle)):
            if (cycle[:i] * 2) in cycle:
                return len(cycle[:i])


def find_max_recurring_cycle(num):
    max_cycle = 0
    for i in range(1, num):
        recurring_cycle = find_recurring_cycle(i)
        print(i)
        if recurring_cycle > max_cycle:
            max_cycle = recurring_cycle
    return max_cycle


def solve():
    print(find_max_recurring_cycle(10))
