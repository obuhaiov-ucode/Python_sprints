def cube(n: int) -> int:
    if isinstance(n, int):
        while n > 0:
            yield n * n * n
            n -= 1
