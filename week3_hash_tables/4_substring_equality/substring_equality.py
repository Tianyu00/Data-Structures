# didn't pass test: failed case #8/14 time limit exceeded

# python3

import sys

class Solver:
    def __init__(self, s):
        self.s = [ord(x) for x in s]
        self.s = self.s[:-1]
        self.H1 = [0] + [None for x in s]
        self.H2 = self.H1.copy()
        self.m1 = 1111111 
        self.m2 = 11111111
        self.x = 3
        for i in range(len(self.s)):
            self.H1[i+1] = (self.H1[i]*self.x + self.s[i]) % self.m1
            #self.H2[i+1] = (self.H2[i]*self.x + self.s[i]) % self.m2
    def ask(self, a, b, l):
        if (self.s[a] != self.s[b]) or (self.s[a+l-1] != self.s[b+l-1]):
            return False
        h1 = self.hashfunc(a,l)
        h2 = self.hashfunc(b,l)
        if h1 != h2:
            return False
        else:
            return self.s[a:(a+l)] == self.s[b:(b+l)]
    def hashfunc(self, a, l):
        temp1 = self.H1[a+l]
        temp2 = self.H1[a]
        h1 = (temp1 - pow(self.x, l, self.m1) * (temp2 % self.m1)) % self.m1
        #temp1 = self.H2[a+l]
        #temp2 = self.H2[a]
        #h2 = (temp1 - pow(self.x, l, self.m2) * (temp2 % self.m2)) % self.m2
        return h1 #,h2


s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
