import random
import typing
from typing import Dict, Any

from src.errors.generator_errors import errors
from src.generators.date.dataclass import Date
from src.generators.date.generator import generate_date
from src.generators.email.dataclass import Email
from src.generators.email.generator import generate_email
from src.generators.ip.generator import Ip, ipv4_generate
from src.generators.json.generator import generate_json
from src.generators.phone_number.dataclass import PhoneNumber
from src.generators.phone_number.generator import generate_phone_numbers
from src.generators.string_gen.generator import generate_string
from src.generators.url.generator import Url, generate_url


def random_data(
        data_type: typing.Union[int, float, str],
        length: int = 0
) -> Any:
    if data_type == int:
        return random.randint(-100, 100)

    elif data_type == float:
        random_int = random.randint(-100, 100)
        return random_int + (random.randint(10, 99) / 100)

    elif data_type == str:
        if length != 0:
            return generate_string(length)

        else:
            raise errors.LenNotProvidedError("Data length is not provided.")

    elif data_type == bool:
        return random.choice([True, False])

    elif data_type == Ip:
        return ipv4_generate()

    elif data_type == Dict or data_type == dict:
        return generate_json(length)

    elif data_type == Url:
        return generate_url(length)

    elif data_type == Email:
        return generate_email(True, length)

    elif data_type == PhoneNumber:
        return generate_phone_numbers(1)

    elif data_type == Date:
        return generate_date()

    raise ValueError(
        "Data type {} is not supported.".format(data_type)
    )
