import logging
import unittest
from datetime import datetime

from src.generators.date.generator import generate_date


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


if __name__ == "__main__":
    unittest.main()