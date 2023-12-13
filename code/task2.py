def fib(n, filename="fib.txt"):
    a, b = 1, 1
    count = 0

    with open(filename, 'w') as file:
        while count < n:
            file.write(f"{a}\n")
            yield a
            a, b = b, a + b
            count += 1


fibonacci_sequence = list(fib(200))
print(fibonacci_sequence)
