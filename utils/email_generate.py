import random
import string


def generate_email(real_domain=True):
    real_domains = ["gmail.com", "outlook.com", "yahoo.com"]

    def random_string(length=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    local_part = random_string()

    if real_domain:
        domain = random.choice(real_domains)
    else:
        domain = f"{random_string(6)}.{random_string(3)}"

    email = f"{local_part}@{domain}"
    return email


if __name__ == "__main__":
    print(generate_email(real_domain=True))
    print(generate_email(real_domain=False))
