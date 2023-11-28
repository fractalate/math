import sympy
from functools import reduce
from operator import mul

def prod(primes, exponents):
  primePowers = [prime ** exponent for (prime, exponent) in zip(primes, exponents)]
  return reduce(mul, primePowers, 1)

def factorial(n):
  return prod(range(1, n + 1), [1] * n)

def iterfactors(n):
  primeFactorization = sympy.factorint(n)
  primes = list(primeFactorization)
  exponents = [0] * len(primes)

  def inc():
    index = len(exponents) - 1
    while index > -1:
      exponents[index] += 1
      if exponents[index] > primeFactorization[primes[index]]:
        exponents[index] = 0
      else:
        return True
      index -= 1
    return False

  yield prod(primes, exponents)
  while inc():
    yield prod(primes, exponents)
