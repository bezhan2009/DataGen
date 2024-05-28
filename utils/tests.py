import logging
import unittest

from .random_data import random_data
from .str_generator import generate_string

logging.basicConfig(level=logging.DEBUG)


class TestStringGenerating(unittest.TestCase):
    def test_generate(self):
        generated_string = generate_string(10)
        logging.debug(f"Generated string: {generated_string}")
        self.assertEqual(len(generated_string), 10)

    def test_generate_with_symbols(self):
        symbols = ['a', 'b']
        generated_string = generate_string(10, symbols)
        logging.debug(f"Generated string: {generated_string}")
        self.assertEqual(len(generated_string), 10)

    def test_generate_error(self):
        with self.assertRaises(ValueError):
            generate_string(-1)

    def test_generate_error_type(self):
        with self.assertRaises(ValueError):
            generate_string("10")


class TestRandomData(unittest.TestCase):
    def test_random_data_int(self):
        generated_int = random_data(int)
        logging.debug(f"Generated int: {generated_int}")
        self.assertIsInstance(generated_int, int)

    def test_random_data_float(self):
        generated_float = random_data(float)
        logging.debug(f"Generated float: {generated_float}")
        self.assertIsInstance(generated_float, float)

    def test_random_data_str(self):
        generated_str = random_data(str, 10)
        logging.debug(f"Generated str: {generated_str}")
        self.assertIsInstance(generated_str, str)
        self.assertEqual(len(generated_str), 10)

    def test_bool_error(self):
        with self.assertRaises(ValueError):
            random_data(bool)


if __name__ == '__main__':
    unittest.main()
