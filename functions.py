"""Math functions."""


def digit_sum(number: int) -> int:
    """Compute the digit sum of an integer."""
    number = sum(int(char) for char in str(number))
    if number < 10:
        return number
    else:
        return digit_sum(number)
