from time import time
from numba import jit
from multiprocessing.dummy import Pool as ThreadPool

@jit(nopython=True,nogil=True)
def collatz(start):
    tested = 0
    maxi = limit//2
    maxi -= maxi % 96
    longest = 0
    nlong = 0
    n = maxi + start
    while n < limit:
        """if n % 3 == 2:
            n += 32
            continue"""
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
        n += 96
        tested += 1

    return nlong, longest, tested

start = time()
limit = 10**9
starters = [1, 7, 9, 15, 25, 27, 31, 33, 39, 43, 57, 63, 73, 75, 79, 91]#[1, 7, 9, 11, 15, 25, 27, 31]
pool = ThreadPool(40)
a = pool.map(collatz, starters)
pool.close()
pool.join()
m = [b[1] for b in a]
i = m.index(max(m))
print(a[i][0], a[i][1], sum(j[2] for j in a), time()-start)
