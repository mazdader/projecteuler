from num2words import num2words


def solve():
    total_len = 0
    for num in range(1, 1001):
        text = num2words(num).replace(' ', '').replace('-', '')
        total_len += len(text)
        print(text)

    print(total_len)
