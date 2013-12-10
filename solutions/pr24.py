import itertools

def get_permutations(num):
    num = [ i for i in str(num) ]
    num.sort()
    permutations = [ i for i in itertools.permutations(num) ]
    return permutations




def solve():
    print "".join(get_permutations('0123456789')[999999])