import random
import string

from src.generators.email.dataclass import Email
from src.generators.string_gen.generator import generate_string


def generate_email(
        real_domain: bool = True,
        length: int = 12
) -> Email:
    """
    Generates a random email address.
    :param real_domain: A boolean flag indicating whether to use real domain names or not.
    :param length: The length of the local part of the email address.
    :return: A randomly generated email address.
    """
    real_domains = ["gmail.com", "outlook.com", "yahoo.com"]

    if real_domain:
        domain = random.choice(real_domains)
    else:
        domain = (generate_string(6, string.ascii_lowercase)
                  + "."
                  + generate_string(3, string.ascii_lowercase))

    local_part_length = length - len(domain) - 1

    if local_part_length < 0:
        raise ValueError("Local part length must be greater than domain length.")

    literal_part_length = local_part_length // 3
    number_part_length = local_part_length - literal_part_length

    literal_part = generate_string(literal_part_length, string.ascii_lowercase)
    number_part = generate_string(number_part_length, string.digits)
    local_part = literal_part + number_part

    email = f"{local_part}@{domain}"
    return Email(email)


if __name__ == "__main__":
    print(generate_email(real_domain=True))
    print(generate_email(real_domain=False))
