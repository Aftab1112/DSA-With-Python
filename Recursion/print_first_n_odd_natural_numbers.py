def print_odd_natural_numbers(n):
    if n > 0:
        print_odd_natural_numbers(n - 1)
        print(2 * n - 1, end=", ")


print_odd_natural_numbers(10)


def print_odd_natural_numbers_reverse(n):
    if n > 0:
        print(2 * n - 1, end=", ")
        print_odd_natural_numbers_reverse(n - 1)


print_odd_natural_numbers_reverse(10)
