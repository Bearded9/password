def number_check(min, max):
    while True:
        try:
            num = int(input(f'Введите длинну пароля от {min} до {max}: '))

            if num < min or num > max:
                raise ValueError

            return num
        except ValueError:
            print(f'Вы ввели число за пределами диапазона, ведите число от {min} до {max}.')

def number_check_lenght(min, max):
    while True:
        try:
            num = int(input(f'Сколько паролей сгенерировать, введите число от {min} до {max}: '))

            if num < min or num > max:
                raise ValueError

            return num
        except ValueError:
            print(f'Вы ввели число за пределами диапазона, ведите число от {min} до {max}.')