import os


def solve():
    data_raw = open(os.path.join('data_files', 'pr11.txt'), 'r').read().split('\n')
    data_raw = [a.split(' ') for a in data_raw]
    data = list()
    for row in data_raw:
        data.append([int(x) for x in row])
    # print(data)

    max_product = 0

    # Horizontal
    for row in range(len(data)):
        for col in range(len(data[row]) - 3):
            product = 1
            for i in range(0, 4):
                product *= data[row][col + i]
            #     print(data[row][col + i])
            # print('product:', product)
            if product > max_product:
                max_product = product

    # Vertical
    for col in range(len(data)):
        for row in range(len(data[col]) - 3):
            product = 1
            for i in range(0, 4):
                product *= data[row + i][col]
            #     print(data[row + i][col])
            # print('product:', product)
            if product > max_product:
                max_product = product

    # Diagonal to the right
    for row in range(len(data) - 3):
        for col in range(len(data[row]) - 3):
            product = 1
            for i in range(0, 4):
                product *= data[row + i][col + i]
                # print(data[row + i][col + i])
            # print('product:', product)
            if product > max_product:
                max_product = product

    # Diagonal to the left
    for col in range(len(data) - 3):
        for row in range(3, len(data[col])):
            product = 1
            for i in range(0, 4):
                product *= data[row - i][col + i]
                # print(data[row - i][col + i])
            # print('product:', product)
            if product > max_product:
                max_product = product

    print('max_product:', max_product)
