def sumNOdd(n):
    if n == 1:
        return 1
    return 2 * n - 1 + sumNOdd(n - 1)


print(sumNOdd(3))


def sumNEven(n):
    if n == 1:
        return 2
    return 2 * n + sumNEven(n - 1)


print(sumNEven(3))


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


def sum_of_squares_of_natural_numbers(n):
    if n == 1:
        return 1
    return n**2 + sum_of_squares_of_natural_numbers(n - 1)


print(sum_of_squares_of_natural_numbers(5))
