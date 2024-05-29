import random
import string

from src.utils import str_generator


class Url:
    def __init__(
            self,
            protocol: str,
            address: str,
            domain: str
    ) -> None:
        self.protocol: str = protocol
        self.address: str = address
        self.domain: str = domain

    @property
    def full_address(self):
        return f"{self.protocol}{self.address}{self.domain}"

    def __str__(self):
        return f"{self.protocol}{self.address}{self.domain}"

    def __repr__(self):
        return f"{self.protocol}{self.address}{self.domain}"


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
    protocol = url
    possible_domains = [".com", ".net", ".org", ".info", ".biz", ".ua", ".de", ".fr", ".it", ".es", ".pl", ]
    selected_domain = random.choice(possible_domains)
    domain_length = length - len(url) - len(selected_domain)
    if domain_length < 0:
        raise ValueError("Length is too short for url.")
    address = str_generator.generate_string(domain_length, acceptable_symbols)
    url += address
    url += selected_domain
    return Url(
        protocol,
        address,
        selected_domain
    )
