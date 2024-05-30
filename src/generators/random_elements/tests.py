import unittest

from .generator import generate_random_elements


class TestGenerateRandomElements(unittest.TestCase):
    def test_valid_input(self):
        input_list = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi']
        num_elements = 3
        result = generate_random_elements(input_list, num_elements)
        self.assertEqual(len(result), num_elements)
        self.assertTrue(all(elem in input_list for elem in result))

    def test_empty_list(self):
        input_list = []
        num_elements = 0
        result = generate_random_elements(input_list, num_elements)
        self.assertEqual(result, [])

    def test_zero_elements(self):
        input_list = ['apple', 'banana', 'cherry']
        num_elements = 0
        result = generate_random_elements(input_list, num_elements)
        self.assertEqual(result, [])

    def test_num_elements_equals_list_length(self):
        input_list = ['apple', 'banana', 'cherry']
        num_elements = 3
        result = generate_random_elements(input_list, num_elements)
        self.assertEqual(set(result), set(input_list))

    def test_num_elements_greater_than_list_length(self):
        input_list = ['apple', 'banana', 'cherry']
        num_elements = 5
        with self.assertRaises(ValueError):
            generate_random_elements(input_list, num_elements)

    def test_input_list_with_duplicates(self):
        input_list = ['apple', 'apple', 'banana', 'cherry']
        num_elements = 2
        result = generate_random_elements(input_list, num_elements)
        self.assertEqual(len(result), num_elements)
        self.assertTrue(all(elem in input_list for elem in result))


if __name__ == "__main__":
    unittest.main()

