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
    for start in [1, 7, 9, 15, 25, 27, 31, 33, 39, 43, 57, 63, 73, 75, 79, 91]:
        n = maxi + start
        while n < limit:
            """if n % 3 == 2:  # or n % 32 in [3,5,13,17,19,21,23,29]:
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
                """if m > largest:
                    largest = m"""
            if terms > longest:
                longest = terms
                nlong = n
                # print(nlong, "took", longest, "steps")
            n += 96
            tested += 1

    return nlong, longest, tested, largest


# print(max(length), length.index(max(length)))
start = time()
limit = 10**9
a = collatz(limit)
print(a[0], a[1], a[2], a[3], time()-start)
