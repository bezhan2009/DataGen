import random

import str_generator
from data_gen_errors import errors_for_utils_data


def random_data(data_type, length=0):
    if data_type == int:
        negative = random.randint(0, 1)
        if negative:
            return random.randint(-10, -100)
        else:
            return random.randint(10, 100)
    if data_type == 'float':
        random_int = random.randint(10, 100)
        return random_int + (random.randint(10, 99) / 100)
    if data_type == 'str':
        if len != 0:
            str_generator.generate_string(length)
        else:
            errors_for_utils_data.LenNotProvidedError("len data is not provided!!!")
