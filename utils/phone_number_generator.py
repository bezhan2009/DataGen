import random as rd


def generate_phone_numbers(country_code: int, number_count: int = 1, phone_length: int = 10):
    """
    Generates a list of random phone numbers for a given country code.

    :param country_code: The country code for the phone numbers.
    :param number_count: The number of phone numbers to generate. Default is 1.
    :param phone_length: The length of the phone number without the country code. Default is 10.
    :return: A list of generated phone numbers as strings.
    """
    if country_code <= 0:
        raise ValueError("Invalid country code. Please provide a positive integer for the country code.")
    if number_count <= 0:
        raise ValueError("Invalid number count. Please provide a positive integer for the number count.")
    if phone_length <= 0:
        raise ValueError("Invalid phone length. Please provide a positive integer for the phone length.")

    generated_phone_numbers = []

    for _ in range(number_count):
        phone_number = f"+{country_code}"
        phone_number += ''.join([str(rd.randint(0, 9)) for _ in range(phone_length)])
        generated_phone_numbers.append(phone_number)

    return generated_phone_numbers


# # Пример использования:
# print(generate_phone_numbers(1))  # Генерация 1 случайного номера с кодом страны 1 (США)
# print(generate_phone_numbers(44, 5))  # Генерация 5 случайных номеров с кодом страны 44 (Великобритания)
# print(generate_phone_numbers(91, 3, 8))  # Генерация 3 случайных номеров с кодом страны 91 (Индия) и длиной номера 8
