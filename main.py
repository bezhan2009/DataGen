from src.generators.string.generator import generate_string
from src.generators.date.generator import generate_date
from src.generators.email.generator import generate_email

print(generate_string(10))
print(generate_date(second=50, minute=10, hour=23))
print(generate_email())
