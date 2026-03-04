
def is_odd_or_even(number):
    """
    Checks if a given number is odd or even.

    Args:
        number: An integer.

    Returns:
        "Odd" if the number is odd, "Even" if the number is even.
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
