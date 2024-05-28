import random
import string

from utils import str_generator


def generate_url(
        length: int,
        protocol: str = "http"
) -> str:
    """
    Generate random url
    :param length: int: length of url
    :param protocol: str: protocol of url
    :return: str: random url
    """
    if not isinstance(length, int):
        raise ValueError("Length must be integer.")
    elif length < 0:
        raise ValueError("Length must be positive.")

    if protocol not in ["http", "https"]:
        raise ValueError("Protocol must be http or https.")

    acceptable_symbols = string.ascii_letters + string.digits
    url = f"{protocol}://"
    possible_domains = [".com", ".net", ".org", ".info", ".biz", ".ua", ".de", ".fr", ".it", ".es", ".pl", ]
    selected_domain = random.choice(possible_domains)
    domain_length = length - len(url) - len(selected_domain)
    if domain_length < 0:
        raise ValueError("Length is too short for url.")
    url += str_generator.generate_string(domain_length, acceptable_symbols)
    url += selected_domain
    return url
