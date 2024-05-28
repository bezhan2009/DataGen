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


def get_some_str(
        length: int
) -> str:
    """
    Get random string
    """
    symbols = string.ascii_letters + string.digits + string.punctuation
    word = [random.choice(symbols) for _ in range(length)]
    return word
