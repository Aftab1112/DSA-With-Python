def sum(n):
    if n == 1:
        return 1
    temp = n + sum(n - 1)
    return temp


print(sum(100))
