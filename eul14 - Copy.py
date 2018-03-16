from time import time
start = time()
limit = 10**5
length = [0] * limit
length[1] = 1
longest = 0
nlong = 0
n = 2
while n < limit:
    terms = 1
    m = n
    while m > 1:
        if m % 2:
            m = 3 * m + 1
        else:
            m //= 2
            if m < n:
                terms += length[m]
                length[n] = terms
                break
        terms += 1
    if terms > longest:
        longest = terms
        nlong = n
        print(nlong, "took", longest, "steps")
    n += 1
print(nlong, longest, time()-start)
