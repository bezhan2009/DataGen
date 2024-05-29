import logging
import unittest

from src.generators.string.generator import generate_string

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
