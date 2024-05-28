import logging
import unittest

from utils.json_generator import generate_json
from utils.url_generate import generate_url
from .ip_generator import ipv4_generate, ipv6_generate, Ip
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


class TestIpGenerator(unittest.TestCase):
    def test_ipv4_generate(self):
        generated_ipv4: Ip = ipv4_generate()
        logging.debug(f"Generated ipv4: {generated_ipv4}")
        self.assertEqual(generated_ipv4.type, "ipv4")
        self.assertTrue(generated_ipv4.valid())

    def test_ipv4_generate_invalid(self):
        generated_ipv4: Ip = ipv4_generate(False)
        logging.debug(f"Generated ipv4: {generated_ipv4}")
        self.assertEqual(generated_ipv4.type, "ipv4")
        self.assertFalse(generated_ipv4.valid())

    def test_ipv6_generate(self):
        generated_ipv6: Ip = ipv6_generate()
        logging.debug(f"Generated ipv6: {generated_ipv6}")
        self.assertEqual(generated_ipv6.type, "ipv6")
        self.assertTrue(generated_ipv6.valid())

    def test_ipv6_generate_invalid(self):
        generated_ipv6: Ip = ipv6_generate(False)
        logging.debug(f"Generated ipv6: {generated_ipv6}")
        self.assertEqual(generated_ipv6.type, "ipv6")
        self.assertFalse(generated_ipv6.valid())


class TestJsonGenerator(unittest.TestCase):
    def test_json_generate(self):
        generated_json = generate_json()
        logging.debug(f"Generated json: {generated_json}")
        self.assertIsInstance(generated_json, dict)
        self.assertEqual(len(generated_json), 10)

    def test_json_generate_error(self):
        with self.assertRaises(ValueError):
            generate_json(-1)

    def test_json_generate_error_type(self):
        with self.assertRaises(ValueError):
            generate_json("10")


class TestUrlGenerator(unittest.TestCase):
    def test_generate_url(self):
        generated_url = generate_url(15)
        logging.debug(f"Generated url: {generated_url}")
        self.assertIsInstance(generated_url, str)
        self.assertEqual(len(generated_url), 15)

    def test_generate_url_error(self):
        with self.assertRaises(ValueError):
            generate_url(-1)

    def test_generate_url_error_type(self):
        with self.assertRaises(ValueError):
            generate_url("10")

    def test_generate_url_error_too_short(self):
        with self.assertRaises(ValueError):
            generate_url(5)


if __name__ == '__main__':
    unittest.main()
