from functools import lru_cache

@lru_cache(maxsize = 10000)
def fibonacci(n):
    if type(n) != int:
        raise TypeError(" must be positive int")
    if n < 1:
        raise TypeError(" must be positive int")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1,10000):
    print(i, " : ", fibonacci(i))
