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


def generate_string(length: int, symbols_list: str = None) -> str:
    """
    Get random string
    :param length: int: length of string
    :param symbols_list: str: list of symbols to generate string
    :return: str: random string
    """
    if not isinstance(length, int):
        raise ValueError("Length must be an integer.")
    elif length < 0:
        raise ValueError("Length must be positive.")

    if symbols_list is None:
        symbols_list = string.ascii_letters + string.digits + string.punctuation

    word = [random.choice(symbols_list) for _ in range(length)]
    word = ''.join(word)

    return word


# Example usage
try:
    random_string = generate_string(10)
    print(random_string)  # Outputs a random string of length 10
except Exception as e:
    print(e)
