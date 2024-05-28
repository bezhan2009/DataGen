import logging
import unittest

from datetime import datetime
from .date_generator import generate_date
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


class TestRandomDates(unittest.TestCase):
    def test_random_date_without_time(self):
        generated_date = generate_date()
        logging.debug(f"Generated date: {generated_date}")

        self.assertIsInstance(generated_date, datetime)
        self.assertTrue(1970 <= generated_date.year <= 2050)
        self.assertTrue(1 <= generated_date.month <= 12)
        self.assertTrue(1 <= generated_date.day <= 28)
        self.assertEqual(generated_date.hour, 0)
        self.assertEqual(generated_date.minute, 0)
        self.assertEqual(generated_date.second, 0)

    def test_random_date_with_time(self):
        generated_date = generate_date(hour=12, minute=30, second=45)
        logging.debug(f"Generated date: {generated_date}")

        self.assertIsInstance(generated_date, datetime)
        self.assertTrue(1970 <= generated_date.year <= 2050)
        self.assertTrue(1 <= generated_date.month <= 12)
        self.assertTrue(1 <= generated_date.day <= 28)
        self.assertEqual(generated_date.hour, 12)
        self.assertEqual(generated_date.minute, 30)
        self.assertEqual(generated_date.second, 45)

    def test_specific_date(self):
        generated_date = generate_date(day=15, month=8, year=2023, hour=14, minute=30)
        logging.debug(f"Generated date: {generated_date}")

        self.assertIsInstance(generated_date, datetime)
        self.assertEqual(generated_date.year, 2023)
        self.assertEqual(generated_date.month, 8)
        self.assertEqual(generated_date.day, 15)
        self.assertEqual(generated_date.hour, 14)
        self.assertEqual(generated_date.minute, 30)
        self.assertEqual(generated_date.second, 0)

    def test_partial_random_date(self):
        generated_date = generate_date(day=0, month=5, year=2022)
        logging.debug(f"Generated date: {generated_date}")

        self.assertIsInstance(generated_date, datetime)
        self.assertEqual(generated_date.year, 2022)
        self.assertEqual(generated_date.month, 5)
        self.assertTrue(1 <= generated_date.day <= 28)
        self.assertEqual(generated_date.hour, 0)
        self.assertEqual(generated_date.minute, 0)
        self.assertEqual(generated_date.second, 0)


if __name__ == '__main__':
    unittest.main()
