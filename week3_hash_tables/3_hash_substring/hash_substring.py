# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def polyHash(S, p, x):
    hash = 0
    for i in range(len(S)-1, -1, -1):
        hash = (hash*x + S[i]) % p
    return hash

def precomputeHashes(T, lenP, p, x):
    lenT = len(T)
    H = [None for i in range(lenT-lenP+1)]
    S = T[(lenT-lenP) :]
    H[lenT - lenP] = polyHash(S, p, x)
    #y = 1
    #for i in range(1, lenP+1):
    #    y = (y*x) % p
    y = pow(x,lenP,p)
    for i in range(lenT - lenP - 1, -1, -1):
        H[i] = (x*H[i+1] + T[i] - y*T[i+lenP]) % p
    return H

def areEqual(S1, S2):
    if len(S1) != len(S2):
        return False
    for i in range(len(S2)):
        if S1[i] != S2[i]:
            return False
    return True

def preprocess(pattern, text):
    pattern = [ord(x) for x in pattern]
    text = [ord(x) for x in text]
    return pattern, text

def get_occurrences(pattern, text):
    pattern, text = preprocess(pattern, text)
    p = 599
    x = 15
    result = []
    pHash = polyHash(pattern, p, x)
    H = precomputeHashes(text, len(pattern), p, x)
    for i in range(len(text) - len(pattern)+1):
        if pHash != H[i]:
            continue
        if text[i:(i+len(pattern))] ==  pattern:
            ## when use "==" in the above comparison, runtime: 0.81 in the last test
            ## when use "areEqual()" function, runtime: 4.80
            ## don't know how python implements "==" though
            result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

