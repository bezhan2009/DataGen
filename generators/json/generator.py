from typing import Dict

from src.generators.string_gen import generator
from src.generators.string_gen.generator import generate_string


def generate_json(
        elements_number: int = 10
) -> Dict:
    """
    Generate json from pattern
    :param elements_number: int: number of elements in json
    :return: Dict: generated json
    """
    if not isinstance(elements_number, int):
        raise ValueError("Elements number must be integer.")
    elif elements_number < 0:
        raise ValueError("Elements number must be positive.")

    return {generate_string(10): generate_string(10) for _ in range(10)}
