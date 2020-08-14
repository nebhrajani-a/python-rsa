
def nochunk_PT2OS(text):
    return [ord(i) for i in text]

def PT2OS(text, l):
    ret = [ord(i) for i in text]
    l_2 = len(ret)
    if l_2 < l:
        spaces = [32] * (l - l_2)
        ret.extend(spaces)
    return ret

def OS2PT(stream):
    return ''.join(chr(i) for i in stream)

def OS2IP(X):
    l = len(X)
    i = 1
    sum = 0
    for X_i in X:
        sum = X_i*(256**(l-i)) + sum
        i += 1
    return sum

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
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

def l_reader(filename):
    f = open(filename, 'r')
    line = f.readline()
    l_s = (line[2:-1:])
    l_s = l_s.strip('][').split(', ')
    return l_s

def line_killer(filename):
    with open(filename, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(filename, 'w') as fout:
        fout.writelines(data[1:])
