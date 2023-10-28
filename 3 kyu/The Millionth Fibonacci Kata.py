import gmpy2

def fib(n):
    a, b = gmpy2.mpz(0), gmpy2.mpz(1)
    if n < 0:
        for _ in range(abs(n)):
            a, b = b - a, a
        return a
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib(1_000_000))