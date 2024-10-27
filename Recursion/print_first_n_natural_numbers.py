def print_natural_numbers(n):
    if n > 0:
        print_natural_numbers(n - 1)
        print(n, end=", ")


# print_natural_numbers(20)


def print_natural_numbers_in_reverse_order(n):
    if n > 0:
        print(n, end=", ")
        print_natural_numbers_in_reverse_order(n - 1)


print_natural_numbers_in_reverse_order(10)
