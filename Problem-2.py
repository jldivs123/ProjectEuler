def fib_sum(max):
    a, b = 0, 1
    sum = 0
    while a < max:
        if a % 2 == 0:
            sum += a
        a,b = b, a+b
    return  sum

print(str(fib_sum(90)))