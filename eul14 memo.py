from time import time
d = {1: 1}


def collatz(x):
    if x in d:
        return d[x]

    nextTerm = x
    if x % 2 == 0:
        nextTerm /= 2
    else:
        nextTerm = 3*x + 1

    length = 1 + collatz(nextTerm)
    d[x] = length
    return d[x]

start = time()
maxLength = 0
ans = 0
for i in range(1, 1000000):
    length = collatz(i)
    if length > maxLength:
        ans = i
        maxLength = length

print(ans, time()-start)
