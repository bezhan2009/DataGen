import random
import len_get

# class Name:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age


class Data:
    def __init__(self, letters, nums):
        self.letters = letters
        self.nums = nums


def get_some_str(len_word):
    data = [
        Data(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]),
        Data(['!', '@', '"', '#', '$', '%', '^', '&', '*', '(', ')', '?'],
             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]),
    ]

    word = ""

    while len(word) < len_word:
        data_choice = random.choice(data)
        letter_choice = random.choice(data_choice.letters)
        number_choice = random.choice(data_choice.nums)
        word += random.choice([letter_choice, str(number_choice)])

    return word

