from src.generators.string.generator import generate_string
from src.generators.date.generator import generate_date
from src.generators.email.generator import generate_email
from src.generators.ip.generator import ipv4_generate, ipv6_generate
from src.generators.random_data.random_data import random_data
from src.generators.json.generator import generate_json
from src.generators.url.generator import generate_url
from src.generators.phone_number.generator import generate_phone_numbers
from src.generators.random_elements.generator import generate_random_elements



print(generate_string(10))
print(generate_date(second=50, minute=10, hour=23))
print(generate_email(_domain="github", _at=True))
print(ipv4_generate())
print(ipv6_generate())
print(random_data(length=10, data_type=int))
print(generate_json())
print(generate_url(20))
print(generate_phone_numbers(country_code=1, phone_length=10))
print(generate_random_elements(["apple", "grape", "pinnaple"], num_elements=2))
