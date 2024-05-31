import random

from src.generators.email.utils import generate_string_with_digits
try:
    from .dataclass import GeneratedEmail
except ImportError:
    from dataclass import GeneratedEmail


def generate_email(real_domain=True) -> GeneratedEmail:
    """
    Generates a random email address.

    Args:
        real_domain (bool): If True, use a real domain from a predefined list.
                            If False, generate a random domain.

    Returns:
        GeneratedEmail: An instance of GeneratedEmail containing the generated email.
    """
    real_domains = ["gmail.com", "outlook.com", "yahoo.com"]

    local_part = generate_string_with_digits(8, 4)  # 8 letters followed by 4 digits
    if real_domain:
        domain = random.choice(real_domains)
    else:
        domain = f"{generate_string_with_digits(6, 0)}.{generate_string_with_digits(3, 0)}"

    email = f"{local_part}@{domain}"
    return GeneratedEmail(email)


if __name__ == "__main__":
    print(generate_email(real_domain=True))
    print(generate_email(real_domain=False))
