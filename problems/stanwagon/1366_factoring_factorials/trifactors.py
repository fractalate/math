# Try Me:
#
# python3 trifactors.py 30
# python3 trifactors.py 10..30

import sys
import random
from factors import iterfactors, factorial
from sympy import divisors

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


def isTriangle(n):
    j = 1
    k = 1
    while True:
        num = k * (k + 1) // 2
        if n == num:
            return True
        if num > n:
            break
        j = k
        k *= 2
    while num > n:
        k -= 1
        num = k * (k + 1) // 2
        if n == num:
            return True
    return False

def isTriangle2(n):
    j = 1
    k = 1
    while True:
        num = k * (k + 1) // 2
        if n == num:
            return True
        if num > n:
            break
        j = k
        k *= 2
    while j <= k:
        m = (j + k) // 2
        num = m * (m + 1) // 2
        if num == n:
            return True
        elif num < n:
            j = m + 1
        else:
            k = m - 1
    return False

def search2(n):
    nbang = factorial(n)
    for f1 in iterfactors(nbang):
        if not isTriangle(f1): continue
        nbangoverf1 = nbang // f1
        for f2 in iterfactors(nbangoverf1):
            if not isTriangle(f2): continue
            nbangoverf1f2 = nbangoverf1 // f2
            f3 = nbangoverf1f2
            if not isTriangle(f3): continue
            print(f1, f2, f3)

def search3(n):
    nbang = factorial(n)
    for f1 in divisors(nbang):
        if not isTriangle2(f1): continue
        nbangoverf1 = nbang // f1
        for f2 in divisors(nbangoverf1):
            if not isTriangle2(f2): continue
            nbangoverf1f2 = nbangoverf1 // f2
            f3 = nbangoverf1f2
            if not isTriangle2(f3): continue
            print(f1, f2, f3)

def search4(n):
    nbang = factorial(n)
    for f1 in reversed(divisors(nbang)):
        if not isTriangle2(f1): continue
        nbangoverf1 = nbang // f1
        for f2 in reversed(divisors(nbangoverf1)):
            if not isTriangle2(f2): continue
            nbangoverf1f2 = nbangoverf1 // f2
            f3 = nbangoverf1f2
            if not isTriangle2(f3): continue
            print(f1, f2, f3)

def search5(n):
    nbang = factorial(n)
    for f1 in reversed(divisors(nbang)):
        if not isTriangle2(f1): continue
        nbangoverf1 = nbang // f1
        for f2 in reversed(divisors(nbangoverf1)):
            if not isTriangle2(f2): continue
            nbangoverf1f2 = nbangoverf1 // f2
            for f3 in reversed(divisors(nbangoverf1f2)):
                if not isTriangle2(f3): continue
                f4 = nbangoverf1f2 // f3
                if not isTriangle2(f4): continue
                print(f1, f2, f3, f4)

for n in sys.argv[1:]:
    search(int(n))
