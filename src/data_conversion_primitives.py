
def PT2OS(text):
    return [ord(i) for i in text]

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
