import random
import utils

num_list = "0123456789"
small_letter_list = "abcdefghijklmnopqrstuvwxyz"
big_letter_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_symbols_list = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

print("Выберите нужные пункты, после пароль сгенерируется")
character_set = ""
generated_password = ""
num = input("Цифры 0-9, да/нет ") 
small_letter = input("Маленькие буквы, a-z да/нет ")
big_letter = input("Большие буквы, A-Z да/нет ")
special_symbols = input("Спец. символы, да/нет ")
password_length = utils.number_check(4, 64)
number_of_passwords = utils.number_check_lenght(1, 10)

if num == "да" or num == "ДА" or num == "Да":
    character_set += random.choice(num_list)
    generated_password += num_list
if small_letter == "да" or small_letter == "ДА" or small_letter == "Да":
    character_set += random.choice(small_letter_list)
    generated_password += small_letter_list
if big_letter == "да" or big_letter == "ДА" or big_letter == "Да":
    character_set += random.choice(big_letter_list)
    generated_password += big_letter_list
if special_symbols == "да" or special_symbols == "ДА" or special_symbols == "Да":
    character_set += random.choice(special_symbols_list)
    generated_password += special_symbols_list
    
if number_of_passwords >= 1 and number_of_passwords <= 10:
    for i in range(number_of_passwords):
        password = character_set
        for n in range(password_length - len(character_set)):
            password += random.choice(generated_password)
            password = list(password)
            random.shuffle(password)
            password_mix = ""
        for n in password:
            password_mix += n
        print(password_mix)