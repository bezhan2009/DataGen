import random
import typing
from typing import Dict

from src.errors.generator_errors import errors
from src.generators.ip.generator import Ip, ipv4_generate
from src.generators.json.generator import generate_json
from src.generators.url.generator import Url, generate_url


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

    elif data_type == bool:
        return random.choice([True, False])

    elif data_type == Ip:
        return ipv4_generate()

    elif data_type == Dict or data_type == dict:
        return generate_json(length)

    elif data_type == Url:
        return generate_url(length)

    raise ValueError(
        "Data type(%s) is not supported.",
        data_type
    )
