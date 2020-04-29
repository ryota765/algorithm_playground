def prime_factorize(n):
    a = {}
    while n % 2 == 0:
        if 2 in a:
            a[2] += 1
        else:
            a[2] = 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            if f in a:
                a[f] += 1
            else:
                a[f] = 1
            n //= f
        else:
            f += 2
    if n != 1:
        a[n] = 1
    return a

# print(prime_factorize(900))