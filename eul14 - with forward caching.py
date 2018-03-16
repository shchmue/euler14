from time import time
start = time()
limit = 10**6
maxi = limit//4*3
length = [0] * limit
length[1] = 1
longest = 0
nlong = 0
n = limit-1#//10*9
while n > maxi:
    if length[n]:
        n -= 1
        continue
    terms = 1
    m = n
    chain = []
    while m > 1:
        if m % 2:
            m = 3 * m + 1
        else:
            m //= 2
        if m < limit and length[m]:
            terms += length[m]
            length[n] = terms
            break
        chain += [m]
        terms += 1
    for i in range(len(chain)):
        if chain[i] < limit:
            length[chain[i]] = terms - i - 1
    if terms > longest:
        longest = terms
        nlong = n
        #print(nlong, "took", longest, "steps")
    n -= 1
# print(max(length), length.index(max(length)))
print(nlong, longest, time()-start)
