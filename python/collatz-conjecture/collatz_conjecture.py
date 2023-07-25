"""collatz conjecture
"""
def steps(number):
    """counts the number of steps in the collatz conjecture

    Args:
        number int: must be a postive integer

    Raises:
        ValueError: if number is zero or negative

    Returns:
        int: the number of steps
    """

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while number != 1:
        count = count+1
        if number % 2 == 0:
            number = number//2
        else:
            number = (number * 3)+1

    return count
