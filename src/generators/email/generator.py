import random

from dataclass import GeneratedEmail
from src.generators.email.utils import generate_string_with_digits


def generate_email(real_domain: bool = True) -> GeneratedEmail:
    """
    Generates a random email address.
    :param real_domain: A boolean flag indicating whether to use real domain names or not.
    :return: A randomly generated email address.
    """
    real_domains = ["gmail.com", "outlook.com", "yahoo.com"]

    local_part = generate_string_with_digits(8, 4)
    if real_domain:
        domain = random.choice(real_domains)
    else:
        domain = f"{generate_string_with_digits(6, 0)}.{generate_string_with_digits(3, 0)}"

    email = f"{local_part}@{domain}"
    return GeneratedEmail(email)


if __name__ == "__main__":
    print(generate_email(real_domain=True))
    print(generate_email(real_domain=False))
