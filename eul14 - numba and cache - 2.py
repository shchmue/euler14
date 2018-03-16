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
    for n in [1,7,9,11,15,25,27,31]:
        n = limit-32+n
        while n > maxi:
            if length[n] or n % 3 == 2:
                n -= 32
                continue
            terms = 1
            m = n
            chain = []
            while m > 1:
                if m % 2:
                    m = 3*m+1#+= (m << 1) + 1
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
            n -= 32
            tested += 1

    return nlong, longest, tested
# print(max(length), length.index(max(length)))
start = time()
limit = 10**7
a = collatz(limit)
print(a[0], a[1], a[2], time()-start)
