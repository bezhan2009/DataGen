import random


def generate_random_elements(input_list: list, num_elements: int):
    """
    Generates random elements from the given list.

    :param input_list: List from which to choose random elements.
    :param num_elements: Number of random elements to select.
    :return: List of randomly selected elements.
    :raises ValueError: If num_elements is greater than the length of input_list.
    """
    if num_elements > len(input_list):
        raise ValueError("Number of random elements cannot exceed the size of the input list.")

    return random.sample(input_list, num_elements)


# # Example usage
# try:
#     input_list = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi']
#     random_elements = generate_random_elements(input_list, 3)
#     print(random_elements)  # Outputs a list of 3 randomly selected elements from input_list
# except Exception as e:
#     print(e)
