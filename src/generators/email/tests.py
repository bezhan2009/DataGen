import unittest

from src.generators.email.generator import generate_email, Email


class TestEmailGenerator(unittest.TestCase):
    def test_generate_email_real_domain(self):
        random_email = generate_email(real_domain=True)
        self.assertIsInstance(random_email, Email)
        self.assertIn(random_email.email.split('@')[1], ["gmail.com", "outlook.com", "yahoo.com"])

    def test_generate_email_random_domain(self):
        random_email = generate_email(real_domain=False)
        self.assertIsInstance(random_email, Email)
        domain = random_email.email.split('@')[1]
        self.assertIn('.', domain)

    def test_generated_email_str(self):
        email = "testuser1234@gmail.com"
        generated_email = Email(email)
        self.assertEqual(str(generated_email), email)

    def test_generated_email_repr(self):
        email = "testuser1234@gmail.com"
        generated_email = Email(email)
        self.assertEqual(repr(generated_email), 'GeneratedEmail(email=testuser1234@gmail.com)')


if __name__ == '__main__':
    unittest.main()
