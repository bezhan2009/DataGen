import random
import typing


class RandomElements(typing.List):
    """
    Class for generating random elements from a list.
    """

    def __init__(self, input_list, num_elements):
        """
        Initializes the RandomElements class with an input list and the number of elements to select.

        :param input_list: The list from which random elements will be selected.
        :param num_elements: The number of random elements to select.
        """
        super().__init__()
        self.input_list = input_list
        self.num_elements = num_elements
        self.validate_input()

    def validate_input(self):
        """
        Validates the input list and the number of elements to ensure they are appropriate for random selection.

        :raises ValueError: If the number of elements exceeds the size of the input list.
        """
        if not isinstance(self.input_list, list):
            raise TypeError("Input must be a list.")
        if not isinstance(self.num_elements, int):
            raise TypeError("Number of elements must be an integer.")
        if self.num_elements > len(self.input_list):
            raise ValueError("Number of random elements cannot exceed the size of the input list.")
        if self.num_elements < 0:
            raise ValueError("Number of elements must be a non-negative integer.")

    def generate(self):
        """
        Generates a list of random elements from the input list.

        :return: A list containing randomly selected elements from the input list.
        """
        return random.sample(self.input_list, self.num_elements)


# Example usage
try:
    random_elements = RandomElements([1, 2, 3, 4, 5], 3)
    print(random_elements.generate())
except (TypeError, ValueError) as e:
    print(e)
