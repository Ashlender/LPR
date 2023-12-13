def fib(n):
    a, b = 1, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1


fibonacci_sequence = list(fib(200))
print(fibonacci_sequence)
