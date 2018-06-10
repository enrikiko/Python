fibonacci_cache = {}
def fibonacci(n):
    if type(n) != int:
        raise TypeError(" must be positive int")
    if n < 1:
        raise TypeError(" must be positive int")
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_cache[n] = value
    return value

for i in range(1,10000):
    print(fibonacci(i))

# print(fibonacci(0))
