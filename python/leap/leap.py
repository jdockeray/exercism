def leap_year(year):
    """
    The function checks if a given year is a leap year or not.

    :param year: The "year" parameter is an integer representing a specific year
    :return: a boolean value indicating whether the given year is a leap year or not.
    """
    return year % 4 == 0 and not (year % 100 == 0 and not year % 400 == 0)
