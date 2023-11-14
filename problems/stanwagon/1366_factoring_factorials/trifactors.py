# Try Me:
#
# python3 trifactors.py 30
# python3 trifactors.py 10..30

import sys
import random

def factorial(n):
    return 1 if n <= 1 else factorial(n - 1) * n

def triangle(n):
    return n * (n + 1) // 2

def trifactors(n):
    k = 2
    while True:
        trin = triangle(k)
        if trin >= n:
            break
        elif n % trin == 0:
            yield trin
        else:
            yield None
        k += 1

def trifactorize(n, factors):
    result = []
    factors = set(factors)
    while factors:
        t = random.choice(list(factors))
        if n % t == 0:
            n //= t
            result.append(t)
            factors.remove(t)
            factors = set([f for f in factors if f <= n])
        else:
            factors.remove(t)
        if n in factors:
            result.append(n)
            n = 1
        if n == 1:
            return result
    return None

def search(n):
    nbang = factorial(n)

    factorsGenerator = trifactors(nbang)
    factors = []
    def findMoreFactors():
        try:
            fails = 0
            while len(factors) < 100 or fails < 100:
                f = next(factorsGenerator)
                if f is None:
                    fails += 1
                else:
                    factors.append(f)
        except StopIteration:
            pass
    findMoreFactors()
    looking = True
    while looking:
        for i in range(1000):
            result = trifactorize(nbang, factors)
            if result:
                print('{}! = {} = {}'.format(n, nbang, repr(result)))
                looking = False
                break
        findMoreFactors()

for n in sys.argv[1:]:
    search(int(n))
