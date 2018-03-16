from time import time
from numba import jit
import numpy as np


@jit(nopython=True)
def collatz(limit):
    tested = 0
    maxi = limit//2
    length = np.zeros(limit, dtype=np.uint16)  # [0] * limit
    length[1] = 1
    longest = 0
    nlong = 0
    n = limit-1
    while n > maxi:
        if length[n] or n % 3 == 2 or n % 32 in [3, 5, 13, 17, 19, 21, 23, 29]:
            n -= 2
            continue
        terms = 1
        m = n
        chain = []
        while m > 1:
            if m % 2:
                m = 3*m + 1
            else:
                m >>= 1
            if m < limit and length[m]:
                terms += length[m]
                length[n] = terms
                break
            chain.append(m)
            terms += 1
        for i in range(len(chain)):
            if chain[i] < limit:
                length[chain[i]] = terms - i - 1
        if terms > longest:
            longest = terms
            nlong = n
            # print(nlong, "took", longest, "steps")
        n -= 2
        tested += 1

    return nlong, longest, tested

start = time()
limit = 10**7
a = collatz(limit)
print(a[0], a[1], a[2], time()-start)
