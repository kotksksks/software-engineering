def fib(n):
    a, b = 1, 1
    file = open('fibonacci.txt', 'w')
    for _ in range(n):
        yield a
        a, b = b, a + b
        file.write(str(a) + '\n')


print(*[i for i in fib(500)])
