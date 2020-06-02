

def sum_d(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + (i * i)
    return sum


print(sum_d(10))
print(sum_d(100))