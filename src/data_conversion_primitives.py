def nochunk_PT2OS(text):
    return [ord(i) for i in text]

def PT2OS(text, l):
    ret = [ord(i) for i in text]
    l_2 = len(ret)
    if l_2 < l:
        newline = [10]
        spaces = [0] * (l - l_2 -1)
        ret.extend(newline)
        ret.extend(spaces)
    return ret

def OS2PT(stream):
    return ''.join(chr(i) for i in stream)

def OS2IP(X):
    l = len(X)
    i = 1
    sum_ = 0
    for X_i in X:
        sum_ = X_i*(256**(l-i)) + sum_
        i += 1
    return sum_

def I2OSP(x, l):
    if x >= 256**l:
        raise ValueError("Int too large.")
    i = 0
    X = []
    while i != (l-1):
        r = x % 256
        X.append(r)
        x = x // 256
        i += 1
    X.append(x)
    return X[::-1]
def read_in_chunks(file_object, chunk_size):
    '''Lazy function (generator) to read a file piece by piece.'''
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def kill_nulls(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    lines.pop()
    f = open(filename, 'w')
    for line in lines:
        f.write(line)
    f.close()
    f = open(filename, 'r')
    string = f.read()
    f.close()
    string = string[:-1]
    f = open(filename, 'w')
    f.write(string)
    f.close()
