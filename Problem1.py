def multiple_sum(limit):
    sum = 0;
    for i in range(limit):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
    return sum;

# Outputs 233168
print(str(multiple_sum(1000)))