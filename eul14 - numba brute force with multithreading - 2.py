from time import time
from numba import jit
from multiprocessing.dummy import Pool as ThreadPool

@jit(nopython=True,nogil=True)
def collatz(start, end):
    tested = 0
    longest = 0
    nlong = 0
    for delta in [1, 7, 9, 15, 25, 27, 31, 33, 39, 43, 57, 63, 73, 75, 79, 91]:#[1, 7, 9, 11, 15, 25, 27, 31]:
        n = start + delta - (start % 96)
        while n < end:
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
limit = 10**10
threads = 40
pool = ThreadPool(threads)
starts = [limit//2+limit//2//threads*i for i in range(threads)]
ends = [limit//2+limit//2//threads*i for i in range(1, threads+1)]
a = pool.starmap(collatz, zip(starts, ends))
pool.close()
pool.join()
m = [b[1] for b in a]
i = m.index(max(m))
print(a[i][0], a[i][1], sum(j[2] for j in a), time()-start)
