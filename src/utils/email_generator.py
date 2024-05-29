import random

from str_generator import generate_string


def generate_email(real_domain=True):
    real_domains = ["gmail.com", "outlook.com", "yahoo.com"]

    local_part = generate_string(8)
    if real_domain:
        domain = random.choice(real_domains)
    else:
        domain = f"{generate_string(6)}.{generate_string(3)}"

    return f"{local_part}@{domain}"


if __name__ == "__main__":
    print(generate_email(real_domain=True))
    print(generate_email(real_domain=False))
