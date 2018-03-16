from time import time
from numba import jit


@jit(nopython=True)
def collatz(limit):
    tested = 0
    maxi = limit//2
    longest = 0
    nlong = 0
    n = maxi+1
    while n < limit:
        if n % 3 == 2 or n % 32 in [3,5,13,17,19,21,23,29]:
            n += 2
            continue
        terms = 1
        m = n
        while m > 1:
            if m % 2:
                m = 3*m + 1
            else:
                m >>= 1
            terms += 1
        if terms > longest:
            longest = terms
            nlong = n
            # print(nlong, "took", longest, "steps")
        n += 2
        tested += 1

    return nlong, longest, tested
# print(max(length), length.index(max(length)))
start = time()
limit = 10**8
a = collatz(limit)
print(a[0], a[1], a[2], time()-start)
