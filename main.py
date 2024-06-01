from generators import *


print("Generate String: ", generate_string(10))
print("Generate Date: ", generate_date(second=50, minute=10, hour=23))
print("Generate Email: ", generate_email(_domain="github", _at=True))
print("Generate ip4: ", ipv4_generate())
print("Generate ip6: ", ipv6_generate())
print("Generate random data(choices: int, float, str): ", random_data(length=10, data_type=int))
print("Generate Json: ", generate_json())
print("Generate url: ", generate_url(20))
print("Generate Phone Number: ", generate_phone_numbers(country_code=1, phone_length=10))
print("Generate random elements: ", generate_random_elements(["apple", "grape", "pinnaple"], num_elements=2))
print("Generate random uuid", generate_uuid(version_uuid=1))
