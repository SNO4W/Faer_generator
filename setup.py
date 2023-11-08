import password_generator
from Keygen import *


class Generator:
    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            self.menu_choice = input('Меню\n\t1.Генератор паролей\n\t2.Генератор ключей\n\t3.Выйти\n>>')
            match self.menu_choice.strip().lower():
                case '1':
                    password_generator.PasswordGenerator()
                case '2':
                    KeyGenerator()
                case '3':
                    exit()
                case _:
                    print(f'Ошибка\nКоманды {self.menu_choice} не существует\nПопробуйте еще раз')
                    continue


if __name__ == '__main__':
    Generator()
