"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    print(numbers)
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    return [number ** 2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    if number == 1:
        return False
    if number % 2 == 0:
        return number == 2

    divider = 3
    while divider * divider <= number and number % divider != 0:
        divider += 2
    return divider * divider > number


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    if filter_type == ODD:
        return list(filter(lambda x: (x % 2 != 0), numbers))
    elif filter_type == EVEN:
        return list(filter(lambda x: (x % 2 == 0), numbers))
    elif filter_type == PRIME:
        return list(filter(is_prime, numbers))
    else:
        raise ValueError('Value filter_type is not correct')
