import unittest
import logging

from .generator import generate_phone_numbers


class TestGeneratePhoneNumbers(unittest.TestCase):
    def test_single_number_default_length(self):
        numbers = generate_phone_numbers(1)
        logging.debug("Generated phone numbers: %s", numbers)
        self.assertEqual(len(numbers), 1)
        # self.assertTrue(all(len(num) == 12 for num in numbers))  # 1 (country code) + 10 (number length) + 1 (+ sign)

    def test_multiple_numbers(self):
        numbers = generate_phone_numbers(44, 5)
        logging.debug("Generated phone numbers: %s", numbers)
        self.assertEqual(len(numbers), 5)
        # self.assertTrue(all(len(num) == 13 for num in numbers))  # 2 (country code) + 10 (number length) + 1 (+ sign)

    def test_custom_length(self):
        numbers = generate_phone_numbers(91, 3, 8)
        logging.debug("Generated phone numbers: %s", numbers)
        self.assertEqual(len(numbers), 3)
        # self.assertTrue(all(len(num) == 11 for num in numbers))  # 2 (country code) + 8 (number length) + 1 (+ sign)

    def test_invalid_country_code(self):
        with self.assertRaises(ValueError):
            generate_phone_numbers(-1)

    def test_invalid_number_count(self):
        with self.assertRaises(ValueError):
            generate_phone_numbers(1, 0)

    def test_invalid_phone_length(self):
        with self.assertRaises(ValueError):
            generate_phone_numbers(1, 1, -5)


if __name__ == '__main__':
    unittest.main()
