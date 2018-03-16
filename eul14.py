n = 5
longest = 0
nlong = 0
while n < 1000000:
    terms = 1
    m = n
    while m > 1:
        if m % 2:
            m = 3 * m + 1
        else:
            m = m / 2
        terms += 1
    if terms > longest:
        longest = terms
        nlong = n
        print nlong, "took", longest, "steps"
    n += 1
print nlong, longest
