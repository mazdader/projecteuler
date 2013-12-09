"""Project Euler problem 5 solve"""

 
def evenly_divisible(curr,num):
    for i in range(2,num):
        if curr % i:
            return False
    return True
                
def find_min_div(num):
    curr = 1
    while True:
        if evenly_divisible(curr,num):
            return curr
        else:
            curr += 1
    return false
    
 
if __name__ == '__main__':
    print find_min_div(20)
