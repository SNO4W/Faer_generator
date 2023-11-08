import random
import time
import os
import tqdm
import prettytable


class Generator:
    def __init__(self):
        self.alphabet = [chr(i) for i in range(97, 123)]
        self.saved_passwords = []
        self.dataCreationTime = []
        self.key_assembly_windows = []
        self.menu()

    def menu(self):
        while True:
            self.menu_choice = input('Меню\n\t1.Генератор паролей\n\t2.Генератор ключей\n\t3.Выйти\n>>')
            match self.menu_choice.strip().lower():
                case '1':
                    PasswordGenerator().commands_passwd()
                case '2':
                    KeyGenerator()
                case '3':
                    exit()
                case _:
                    print(f'Ошибка\nКоманды {self.menu_choice} не существует\nПопробуйте еще раз')
                    continue


class PasswordGenerator(Generator):
    print('Генератор паролей')

    def commands_passwd(self):  # функция команд
        while True:
            self.cmd = input(
                '\nВыберите № команды для продолжения:\n\t1.Сгенерировать рандомный пароль\n\t2.Показать сохраненные пароли\n>>')
            if self.cmd.strip() == '1':
                self.attribute()
            elif self.cmd.strip() == '2':
                self.saved_passwd()
            else:
                print(f'Ошибка\nКоманды {self.cmd} не существует\nПопробуйте еще раз')
                continue

    def attribute(self):  # функция подбора количества символов в пароле
        self.length = input('\nВведите кол-во символов в пароле(6-12):')
        while True:
            if self.length.strip().isdigit():
                if 5 < int(self.length) < 13:
                    break
                else:
                    print('Ошибка!\nПароль должен быть не больше 12  и не меньше 6 символов \nПопробуйте заново')
                    self.length = input('Введите кол-во цифр пароля(6-12):')
            else:
                print(
                    'Ошибка!\nДля определения размера сгенерированного пароля используйте только цифры\nПопробуйте заново')
                self.length = input('Введите кол-во цифр пароля(6-12): ')
        self.passwd_gen()

    def passwd_gen(self):  # функция генерирования пароля
        self.gen = []
        for i in range(0, int(self.length)):
            self.random_lettter = random.choice(self.alphabet)
            self.random_num = random.randint(0, 9)
            x = random.randint(0, 4)
            if x == 0 or x == 1:
                self.gen.append(str(self.random_num))
            elif x == 2 or x == 3:
                self.gen.append(self.random_lettter)
            else:
                self.gen.append(self.random_lettter.upper())
        self.passwd = ''.join(self.gen)
        print('\nПодождите, ваш пароль генерируется...')
        for i in tqdm.tqdm(range(1, 101)):
            if 6 <= int(self.length) < 8:
                time.sleep(0.05)
            elif 8 <= int(self.length) < 10:
                time.sleep(0.1)
            else:
                time.sleep(0.2)
        print(f'Ваш пароль успешно сгенерирован\nСгенерированный пароль:{self.passwd}')
        savepsswd = input('Хотите сохранить пароль(да/нет):')
        while True:
            if savepsswd.strip() == 'да':
                print('Пароль успешно сохранен!')
                self.data_create = time.asctime()
                self.dataCreationTime.append(self.data_create)
                self.saved_passwords.append(self.passwd)
                f = open(
                    '/my console projects/password generator + activion key/generated saved passwords.txt',
                    'a')
                data_passwd = self.saved_passwords.index(self.passwd)
                with open('generated saved passwords.txt', 'r') as file:
                    old_password = file.readlines()
                f.write(
                    f'{len(old_password) + 1}. {self.saved_passwords[data_passwd]} . (Дата создания : {self.dataCreationTime[data_passwd]})\n')
                f.close()
                self.commands_passwd()
            elif savepsswd.strip() == 'нет':
                print('Пароль не был сохранен')
                self.commands_passwd()
            else:
                print('Ошибка\nДля продолжения используйте только да/нет\nПопробуйте заново')
                savepsswd = input('Хотите сохранить пароль(да/нет):')

    def saved_passwd(self):  # сохраненные пароли
        print('Ваши сохраненные пароли:\n')
        f = open(
            '/my console projects/password generator + activion key/generated saved passwords.txt',
            'r')

        def is_empty_file(file_name):  # проверка пуст ли файл.txt
            file_info = os.stat(file_name)
            return file_info.st_size == 0

        file_name = '/my console projects/password generator + activion key/generated saved passwords.txt'
        if is_empty_file(file_name):
            print(
                'Password not found!\nДля создания новых паролей используйте команду "1.Сгенерировать рандомный пароль"')
        else:
            table = prettytable.PrettyTable()
            table.field_names = ['№', 'Password', "Data of creation"]
            for i in f:
                x = i.split('.')
                x = list([j.strip() for j in x])
                table.add_row(x)
            print(table)
        f.close()
        self.commands_passwd()


class KeyGenerator(Generator):
    print('Генератор ключей')

    def commands_key(self):
        while True:
            self.cmnd = input(
                '\nВыберите № команды для продолжения:\n\t1.Сгенерировать лицензионный ключ\n\t2.Показать сохранные ключи\n>>')
            if self.cmnd.strip() == '1':
                self.selection()
            elif self.cmnd.strip() == '2':
                self.saved_key()
            else:
                print(f'Ошибка\nКоманды {self.cmnd} не существует\nПопробуйте еще раз')
                continue

    def selection(self):
        while True:
            self.choice_key = input(
                '\nВыберите № ключа которого вы хотели бы сгенерировать(для выхода в меню введите exit):\n\t1.Windows OS')
            match self.choice_key.strip().lower():
                case '1':
                    self.keygen_windows()
                case 'exit':
                    pass
                case _:
                    print(f'Ошибка\nКоманды {self.choice_key} не существует\nПопробуйте еще раз')
                    continue

    def keygen_windows(self):
        pass

    def saved_key(self):
        pass


if __name__ == '__main__':
    gen = Generator()
