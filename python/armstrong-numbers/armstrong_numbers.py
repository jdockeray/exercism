"""Armstrong numbers
"""
def is_armstrong_number(number):
    """
    The function `is_armstrong_number` checks if a given number is an Armstrong number.

    :param number: The parameter "number" is the input number that we want to check if it is an
    Armstrong number
    :return: a boolean value indicating whether the given number is an Armstrong number or not.
    """
    power = len(str(number))
    acc = 0

    for digit in [int(i) for i in str(number)]:
        acc += digit ** power

    return acc == number
