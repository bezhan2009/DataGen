import logging
import unittest

from src.generators.date.dataclass import Date
from src.generators.email.dataclass import Email
from src.generators.ip.dataclass import Ip
from src.generators.phone_number.dataclass import PhoneNumber
from src.generators.random_data.random_data import random_data
from src.generators.url.dataclass import Url

logging.basicConfig(level=logging.DEBUG)


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

    def test_random_data_bool(self):
        generated_bool = random_data(bool)
        logging.debug(f"Generated bool: {generated_bool}")
        self.assertIsInstance(generated_bool, bool)

    def test_random_data_ip(self):
        generated_ip = random_data(Ip)
        logging.debug(f"Generated ip: {generated_ip}")
        self.assertIsInstance(generated_ip, Ip)
        self.assertTrue(len(generated_ip) > 0)

    def test_random_data_dict(self):
        generated_dict = random_data(dict, 10)
        logging.debug(f"Generated dict: {generated_dict}")
        self.assertIsInstance(generated_dict, dict)
        self.assertEqual(len(generated_dict), 10)

    def test_random_data_url(self):
        generated_url = random_data(Url, 15)
        logging.debug(f"Generated url: {generated_url}")
        self.assertIsInstance(generated_url, Url)
        self.assertTrue(len(generated_url) > 0)

    def test_random_data_email(self):
        generated_email = random_data(Email, 15)
        logging.debug(f"Generated email: {generated_email}")
        self.assertIsInstance(generated_email, Email)
        self.assertEqual(len(generated_email), 15)

    def test_random_data_phone_number(self):
        generated_phone_number = random_data(PhoneNumber)
        logging.debug(f"Generated phone number: {generated_phone_number}")
        self.assertIsInstance(generated_phone_number, PhoneNumber)
        self.assertTrue(len(generated_phone_number) > 0)

    def test_random_data_date(self):
        generated_date = random_data(Date)
        logging.debug(f"Generated date: {generated_date}")
        self.assertIsInstance(generated_date, Date)

    def test_data_type_error(self):
        with self.assertRaises(ValueError):
            random_data("")
