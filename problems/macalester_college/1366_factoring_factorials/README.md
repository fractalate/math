# 1366 Factoring Factorials

*November 14, 2023*

Express 30! as a product of triangular numbers.

## Result

I've created the [trifactors.py](./trifactors.py) script to find such factorizations. Here is one factorization for 30!

```
$ python3 trifactors.py 30
30! = 265252859812191058636308480000000 = [2016, 210, 2080, 2346, 7260, 4560, 4095, 10440, 36, 21, 120]
```

## Bonus

Using a linear integer programming approach described by Stan Wagon, I've found a factorization of 1993! which you can see in the notebook [1993.ipynb](./1993.ipynb).
