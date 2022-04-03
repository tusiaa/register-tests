from hamcrest.core.base_matcher import BaseMatcher
import doctest

def pesel(pesel: str):

    r"""Checks if pesel is valid.
        >>> pesel("96032687885")
        True
        >>> pesel("94071449639")
        True
        >>> pesel("03241311845")
        True
        >>> pesel("12345678901")
        False
        >>> pesel("")
        False
        >>> pesel("123456789")
        False
        >>> pesel("96032687886")
        False
        >>> pesel("96033687884")
        False
        >>> pesel("12345678910")
        False
        >>> pesel(96032687886)
        False
        >>> pesel(9603.2687885)
        False
        >>> pesel(True)
        False
        >>> pesel(None)
        False
        >>> pesel([1,2,3])
        False
        >>> pesel({'name': 2, 'grades': 4})
        False
        """

    if not isinstance(pesel, str):
        return False
    if len(pesel) != 11 or not pesel.isdigit():
        return False

    wagi = [1, 3, 7, 9]
    value = 0
    months = list(range(81, 93)) + list(range(1, 13)) + list(range(21, 33))    

    for i in range(0, 10):
        value += int(pesel[i]) * wagi[i % 4]

    value = value % 10

    if value != 0:
        value = 10 - value

    if value != int(pesel[10]):
        return False

    if int(pesel[2:4]) not in months:
        return False

    if int(pesel[4:6]) not in range(1, 32):
        return False

    return True

class IsValidPesel(BaseMatcher):
    def __init__(self):
        doctest.testmod()

    def _matches(self, item):
        return pesel(item)

    def describe_to(self, description):
        description.append_text("Invalid pesel!")