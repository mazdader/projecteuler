def get_data():
    data = open('data_files/pr22_names.txt', 'r').readline()
    data = data.replace('"','')
    data = data.split(',')
    data.sort()
    return data

def get_num_of_char(ch):
    return (ord(ch) - 64)

def get_worth(txt):
    result = 0
    for i in txt:
        result += get_num_of_char(i)
    return result

def get_position(data, txt):
    pos = [i for i,x in enumerate(data) if x == txt]
    return pos[0] + 1

def get_score(data, txt):
    return get_worth(txt) * get_position(data, txt)

def get_total_score(data):
    score = 0
    for i in data:
        score += get_score(data, i)
    return score

def solve():

    print get_total_score(get_data())