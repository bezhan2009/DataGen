import random
import string

from dataclass import GeneratedEmail
from src.generators.string.generator import generate_string


def generate_email(real_domain: bool = True) -> GeneratedEmail:
    """
    Generates a random email address.
    :param real_domain: A boolean flag indicating whether to use real domain names or not.
    :return: A randomly generated email address.
    """
    real_domains = ["gmail.com", "outlook.com", "yahoo.com"]

    literal_part = generate_string(8, string.ascii_lowercase)
    number_part = generate_string(4, string.digits)
    local_part = literal_part + number_part
    if real_domain:
        domain = random.choice(real_domains)
    else:
        domain = (generate_string(6, string.ascii_lowercase)
                  + generate_string(3, string.ascii_lowercase))

    email = f"{local_part}@{domain}"
    return GeneratedEmail(email)


if __name__ == "__main__":
    print(generate_email(real_domain=True))
    print(generate_email(real_domain=False))
