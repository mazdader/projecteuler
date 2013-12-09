def find_num_seq(last, count = 0):
    if last != 1:
        if last % 2 == 0:
            count = find_num_seq(last / 2, count+1)
        else:
            count = find_num_seq((last * 3) + 1, count + 1)
        return count
    else:
        return count + 1


def find_max_seq(max_num):

    max_seq = [0,0]

    for i in range(2,max_num+1):
        last_seq = find_num_seq(i)
        if max_seq[0] < last_seq:
            max_seq[0] = last_seq
            max_seq[1] = i

    return max_seq

def solve():
    print find_max_seq(1000000)