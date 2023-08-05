def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        return 'Error'
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b
x=4782
a=0
print(x)
print(fibonacci(x))
print(len(str(fibonacci(x))))




