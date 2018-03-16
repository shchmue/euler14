from time import time
from numba import jit


@jit(nopython=True)
def collatz(limit):
    tested = 0
    maxi = limit//2
    maxi -= maxi % 96
    longest = 0
    largest = 0
    nlong = 0
    wheel = [6, 2, 6, 10, 2, 4, 2, 6, 4, 14, 6, 10, 2, 4, 12, 6]
    pos = 0
    n = 1#maxi + 1
    while n < limit:
        terms = 1
        m = n
        while m > 1:
            if m % 2:
                m = 3*m + 1
            else:
                m >>= 1
            terms += 1
            """if m > largest:
                largest = m"""
        if terms > longest:
            longest = terms
            nlong = n
            print(nlong, "took", longest, "steps")
        n += 1#wheel[pos]
        #pos = (pos + 1) & 15
        tested += 1

    return nlong, longest, tested, largest


# print(max(length), length.index(max(length)))
start = time()
limit = 10**7
a = collatz(limit)
print(a[0], a[1], a[2], a[3], time()-start)
