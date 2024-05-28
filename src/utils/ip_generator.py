import random


class Ip:
    """
    Class for ip address
    """

    def __init__(self, ip):
        self.ip = ip
        self.type = "ipv4" if "." in ip else "ipv6"

    def valid(self):
        """
        Check if ip is valid
        """
        try:
            if self.type == "ipv4":
                return all(0 <= int(i) <= 255 for i in self.ip.split("."))
            else:
                return all(0 <= int(i, 16) <= 65535 for i in self.ip.split(":"))
        except ValueError:
            return False

    def __str__(self):
        return self.ip

    def __repr__(self):
        return f"Ip({self.ip})"


def ipv4_generate(
        valid: bool = True
) -> str:
    """
    Generate random ipv4 address
    :param valid: bool: valid or invalid ip
    :return: str: ipv4 address
    """
    if valid:
        ip_string = ".".join(str(random.randint(0, 255)) for _ in range(4))
        return Ip(ip_string)
    else:
        ip_string = ".".join(str(random.randint(255, 999)) for _ in range(4))
        return Ip(ip_string)


def ipv6_generate(
        valid: bool = True
) -> str:
    """
    Generate random ipv6 address
    :param valid: bool: valid or invalid ip
    :return: str: ipv6 address
    """
    if valid:
        ip_string = ":".join("".join(random.choices("0123456789abcdef", k=4)) for _ in range(8))
        return Ip(ip_string)
    else:
        ip_string = ":".join("".join(random.choices("ghijklmnopqrstuvwxyz", k=4)) for _ in range(8))
        return Ip(ip_string)
