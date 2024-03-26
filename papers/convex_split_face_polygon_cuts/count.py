import sys

xs = []
xs_sum = 0

for arg in sys.argv[1:]:
    x = int(arg)
    if x <= 0:
        raise ValueError('invalid number of cuts: ' + repr(x))
    xs.append(x)
    xs_sum += x

N = len(xs)

if N < 3:
    # TypeError is what the python interpreter gives you when you
    # try to use a function with the wrong number of arguments, so
    # I do similar here for the script as a whole. What is the best
    # built-in error I could use for this stop?
    raise TypeError('script expected 2 arguments, got ' + str(len(xs)))

count_cuts = 0
multiplicand = xs_sum

for k in range(0, N):
    multiplicand -= xs[k]
    count_cuts += (xs[k] - 1) * multiplicand
    multiplicand += 1

count_cuts += N * (N - 1) // 2

print(count_cuts)
