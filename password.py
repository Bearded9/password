import random

num_list = "0123456789"
small_letter_list = "abcdefghijklmnopqrstuvwxyz"
big_letter_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_symbols_list = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

print("Выберите нужные пункты, после пароль сгенерируется")
chars = ""
chars2 = ""
num = input("Цифры 0-9, да/нет ")
small_letter = input("Маленькие буквы, a-z да/нет ")
big_letter = input("Большие буквы, A-Z да/нет ")
special_symbols = input("Спец. символы, да/нет ")
password_length = int(input("Введите длинну пароля от 4 до 64: "))
while password_length < 4 or password_length > 64:
    print("Вы ввели число за пределами диапазона, повторите попытку")
    password_length = int(input("Введите длинну пароля от 4 до 64: "))
generate_password = int(input("Сколько вариантов пароля сгенерировать(введите от 1 до 10) "))
while generate_password < 1 or generate_password > 10:
    print("Вы ввели число за пределами диапазона, повторите попытку")
    generate_password = int(input("Сколько вариантов пароля сгенерировать(введите от 1 до 10) "))

if num == "да":
    chars += random.choice(num_list)
    chars2 += num_list
if small_letter == "да":
    chars += random.choice(small_letter_list)
    chars2 += small_letter_list
if big_letter == "да":
    chars += random.choice(big_letter_list)
    chars2 += big_letter_list
if special_symbols == "да":
    chars += random.choice(special_symbols_list)
    chars2 += special_symbols_list
    
if generate_password >= 1 and generate_password <= 10:
    for i in range(generate_password):
        password = chars
        for n in range(password_length - len(chars)):
            password += random.choice(chars2)
        mix_password = password.split()
        for i, word in enumerate(map(list, mix_password)):
            random.shuffle(word)
            mix_password[i] = ''.join(word)
        print(*mix_password)