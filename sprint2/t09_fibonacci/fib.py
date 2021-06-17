def fib(n: int) -> int:
    if n > 1:
        return fib(n-1) + fib(n-2)
    if n == 1:
        return 1
    if n == 0:
        return 0

def fib_generator(n: int) -> int:
    i = 0

    while i < n:
        yield fib(i)
        i += 1
