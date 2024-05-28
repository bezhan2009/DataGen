import logging
import unittest
import uuid

from data_gen_errors import errors_for_utils_data
from .uuid_generator import generate_uuid
from .phone_number_generator import generate_phone_numbers
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


class TestGeneratePhoneNumbers(unittest.TestCase):
    def test_single_number_default_length(self):
        numbers = generate_phone_numbers(1)
        logging.debug("Generated phone numbers: %s", numbers)
        self.assertEqual(len(numbers), 1)
        self.assertTrue(all(len(num) == 12 for num in numbers))  # 1 (country code) + 10 (number length) + 1 (+ sign)

    def test_multiple_numbers(self):
        numbers = generate_phone_numbers(44, 5)
        logging.debug("Generated phone numbers: %s", numbers)
        self.assertEqual(len(numbers), 5)
        self.assertTrue(all(len(num) == 13 for num in numbers))  # 2 (country code) + 10 (number length) + 1 (+ sign)

    def test_custom_length(self):
        numbers = generate_phone_numbers(91, 3, 8)
        logging.debug("Generated phone numbers: %s", numbers)
        self.assertEqual(len(numbers), 3)
        self.assertTrue(all(len(num) == 11 for num in numbers))  # 2 (country code) + 8 (number length) + 1 (+ sign)

    def test_invalid_country_code(self):
        with self.assertRaises(ValueError):
            generate_phone_numbers(-1)

    def test_invalid_number_count(self):
        with self.assertRaises(ValueError):
            generate_phone_numbers(1, 0)

    def test_invalid_phone_length(self):
        with self.assertRaises(ValueError):
            generate_phone_numbers(1, 1, -5)


class TestGenerateUUID(unittest.TestCase):
    def test_generate_uuid_v1(self):
        result = generate_uuid(1)
        self.assertIsInstance(result, uuid.UUID)
        self.assertEqual(result.version, 1)

    def test_generate_uuid_v3(self):
        result = generate_uuid(3, "example.com")
        self.assertIsInstance(result, uuid.UUID)
        self.assertEqual(result.version, 3)

    def test_generate_uuid_v4(self):
        result = generate_uuid(4)
        self.assertIsInstance(result, uuid.UUID)
        self.assertEqual(result.version, 4)

    def test_generate_uuid_v5(self):
        result = generate_uuid(5, "example.com")
        self.assertIsInstance(result, uuid.UUID)
        self.assertEqual(result.version, 5)

    def test_invalid_version(self):
        with self.assertRaises(errors_for_utils_data.UuidError):
            generate_uuid(0)

    def test_missing_namespace_v3(self):
        with self.assertRaises(errors_for_utils_data.UuidNameSpaceDNSIsNotProvidedError):
            generate_uuid(3)

    def test_missing_namespace_v5(self):
        with self.assertRaises(errors_for_utils_data.UuidNameSpaceDNSIsNotProvidedError):
            generate_uuid(5)


if __name__ == '__main__':
    unittest.main()
