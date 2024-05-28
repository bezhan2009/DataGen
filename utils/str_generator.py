import random
import string


# class Name:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age


# class Data:
#     def __init__(self, letters, nums):
#         self.letters = letters
#         self.nums = nums


def generate_string(
        length: int,
        symbols_list: str = None
) -> str:
    """
    Get random string
    :param length: int: length of string
    :param symbols_list: str: list of symbols to generate string
    :return: str: random string
    """

    if symbols_list is None:
        symbols_list = string.ascii_letters + string.digits + string.punctuation

    word = [random.choice(symbols_list) for _ in range(length)]
    word = ''.join(word)

    return word
