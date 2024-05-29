import random
import string


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
    if not isinstance(length, int):
        raise ValueError("Length must be integer.")
    elif length < 0:
        raise ValueError("Length must be positive.")

    if symbols_list is None:
        symbols_list = string.ascii_letters + string.digits + string.punctuation

    word = [random.choice(symbols_list) for _ in range(length)]
    word = ''.join(word)

    return word
