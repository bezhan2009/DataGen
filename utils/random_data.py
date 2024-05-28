import random
import typing

from data_gen_errors import errors_for_utils_data
from utils import str_generator


def random_data(
        data_type: typing.Union[int, float, str],
        length: int = 0
) -> typing.Union[int, float, str]:
    if data_type == int:
        return random.randint(-100, 100)

    elif data_type == float:
        random_int = random.randint(-100, 100)
        return random_int + (random.randint(10, 99) / 100)

    elif data_type == str:
        if length != 0:
            return str_generator.generate_string(length)

        else:
            raise errors_for_utils_data.LenNotProvidedError("Data length is not provided.")
