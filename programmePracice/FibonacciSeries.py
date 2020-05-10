
# This will generate Fibonacci Series


def fibo_series(n):
    a = 0
    b = 1
    for i in range(n+1):
        print(a)
        c = a + b
        a = b
        b = c


fibo_series(10)

