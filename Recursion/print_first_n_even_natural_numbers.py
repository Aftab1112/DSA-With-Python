def print_even_numbers(n):
    if n > 0:
        print_even_numbers(n - 1)
        print(2 * n, end=", ")


print_even_numbers(10)


def print_even_numbers_reverse(n):
    if n > 0:
        print(2 * n, end=", ")
        print_even_numbers_reverse(n - 1)


print_even_numbers_reverse(10)
