import random
import time
import os
import tqdm
import prettytable
from colorama import Fore, Back, Style


def empty_file(filename):  # проверка пуст ли файл.txt
    file_info = os.stat(filename)
    return file_info.st_size == 0


class PasswordGenerator:

    def __init__(self):
        self.alphabet = [chr(i) for i in range(97, 123)]
        self.saved_passwords = []
        self.dataCreationTime = []
        self.commands()

    def commands(self):  # функция команд
        while True:
            self.cmd = input(Fore.BLUE +
                             '\nВыберите № команды для продолжения:\n\t1.Сгенерировать рандомный пароль\n\t2.Показать сохраненные пароли\n\t3.Выход в меню\n>>')
            if self.cmd.strip() == '1':
                self.attribute()
            elif self.cmd.strip() == '2':
                self.saved_passwd()
            elif self.cmd.strip() == '3':
                Generator()
            else:
                print(Fore.RED + f'Ошибка\nКоманды {self.cmd} не существует\nПопробуйте еще раз')
                continue

    def attribute(self):  # функция подбора количества символов в пароле
        self.length = input(Fore.BLUE + '\nВведите кол-во символов в пароле(6-12):')
        while True:
            if self.length.strip().isdigit():
                if 5 < int(self.length) < 13:
                    break
                else:
                    print('Ошибка!\nПароль должен быть не больше 12  и не меньше 6 символов \nПопробуйте заново')
                    self.length = input(Fore.BLUE + 'Введите кол-во цифр пароля(6-12):')
            else:
                print(
                    'Ошибка!\nДля определения размера сгенерированного пароля используйте только цифры\nПопробуйте заново')
                self.length = input(Fore.BLUE + 'Введите кол-во цифр пароля(6-12): ')
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
        print(Fore.BLUE + '\nПодождите, ваш пароль генерируется...')
        for i in tqdm.tqdm(range(1, 101)):
            if 6 <= int(self.length) < 8:
                time.sleep(0.05)
            elif 8 <= int(self.length) < 10:
                time.sleep(0.1)
            else:
                time.sleep(0.2)
        print(Fore.BLUE + f'Ваш пароль успешно сгенерирован\nСгенерированный пароль:{self.passwd}')
        savepsswd = input(Fore.BLUE + 'Хотите сохранить пароль(да/нет):')
        while True:
            if savepsswd.strip() == 'да':
                print(Fore.GREEN + 'Пароль успешно сохранен!')
                self.data_create = time.asctime()
                self.dataCreationTime.append(self.data_create)
                self.saved_passwords.append(self.passwd)
                f = open('generated saved passwords.txt', 'a')
                data_passwd = self.saved_passwords.index(self.passwd)
                with open('generated saved passwords.txt', 'r') as file:
                    old_password = file.readlines()
                f.write(
                    f'{len(old_password) + 1}. {self.saved_passwords[data_passwd]} . (Дата создания : {self.dataCreationTime[data_passwd]})\n')
                f.close()
                self.commands()
            elif savepsswd.strip() == 'нет':
                print(Fore.YELLOW + 'Пароль не был сохранен')
                self.commands()
            else:
                print(Fore.RED + 'Ошибка\nДля продолжения используйте только да/нет\nПопробуйте заново')
                savepsswd = input(Fore.BLUE + 'Хотите сохранить пароль(да/нет):')

    def saved_passwd(self):  # сохраненные пароли
        print(Fore.BLUE + 'Ваши сохраненные пароли:\n')
        f = open(
            'generated saved passwords.txt',
            'r')

        def is_empty_file(file_name):  # проверка пуст ли файл.txt
            file_info = os.stat(file_name)
            return file_info.st_size == 0

        file_name = 'generated saved passwords.txt'
        if is_empty_file(file_name):
            print(Fore.YELLOW +
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
        self.commands()


class KeyGenerator:

    def __init__(self):
        self.alphabet = [chr(i) for i in range(97, 123)]
        self.key_windows = []
        self.commands()

    def commands(self):
        while True:
            self.cmd = input(Fore.MAGENTA +
                             '\nВыберите № команды для продолжения:\n\t1.Сгенерировать лицензионные ключи\n\t2.Показать сохранные ключи\n\t3.Выход в главное меню\n>>')
            if self.cmd.strip() == '1':
                self.selection()
            elif self.cmd.strip() == '2':
                self.saved_key_windows()
            elif self.cmd.strip() == '3':
                Generator()
            else:
                print(Fore.RED + f'Ошибка\nКоманды {self.cmd} не существует\nПопробуйте еще раз')
                continue

    def selection(self):
        while True:
            self.choice_key = input(Fore.MAGENTA +
                                    '\nВыберите № ключа которого вы хотели бы сгенерировать(для выхода в меню введите exit):\n\t1.Windows OS\n>>')
            match self.choice_key.strip().lower():
                case '1':
                    self.keygen_windows()
                case 'exit':
                    self.commands()
                case _:
                    print(Fore.RED + f'Ошибка\nКоманды {self.choice_key} не существует\nПопробуйте еще раз')
                    continue

    def keygen_windows(self):
        self.key_windows.clear()
        for i in range(5):
            self.key_assembly_completely = []
            self.key_assembly_parts = []
            for j in range(5):
                for k in range(5):
                    self.random_letter = random.choice(self.alphabet)
                    self.random_num = random.randint(0, 9)
                    x = random.randint(1, 2)
                    match x:
                        case 1:
                            self.key_assembly_parts.append(self.random_letter.upper())
                        case 2:
                            self.key_assembly_parts.append(str(self.random_num))
                self.key_assembly_completely.append(''.join(self.key_assembly_parts) + '-')
                self.key_assembly_parts = []
            self.key_windows.append((''.join(self.key_assembly_completely))[0:-1])
        print(Fore.MAGENTA + '\nПодождите, лицензионные ключи генерируются...')
        for i in tqdm.tqdm(range(1, 101)):
            time.sleep(0.1)
        print(Fore.GREEN + 'Ключи активации успешно сгенерированы')
        save_key = input(Fore.MAGENTA + 'Хотите сохранить сгенерированные ключи(да/нет):')
        while True:
            if save_key.strip() == 'да':
                print(Fore.GREEN + 'Пароль успешно сохранен!')
                with open('saved activion keys windows.txt', 'r') as file:
                    strings = file.readlines()
                n = len(strings)
                f = open('saved activion keys windows.txt', 'a')
                if empty_file('saved activion keys windows.txt'):
                    f.write(Fore.MAGENTA + 'Ключи активации Windows OS:\n')
                    n += 1
                for i in self.key_windows:
                    f.write(f'{n}. {i}\n')
                    n += 1
                f.close()
                self.commands()
            elif save_key.strip() == 'нет':
                print(Fore.YELLOW + 'Лицензионные ключи не были сохранены')
                self.commands()
            else:
                print(Fore.RED + 'Ошибка\nДля продолжения используйте только да/нет\nПопробуйте заново')
                save_key = input(Fore.MAGENTA + 'Хотите сохранить сгенерированные ключи(да/нет):')
                continue
        self.commands()

    def saved_key_windows(self):
        print(Fore.MAGENTA + 'Ваши лицензионные ключи:\n')
        f = open(
            'saved activion keys windows.txt',
            'r')
        file = 'saved activion keys windows.txt'
        if empty_file(file):
            print(Fore.YELLOW +
                  'Activioin keys not found!\nДля создания новых лицензионных ключей используйте команду "1.Сгенерировать лицензионные ключи"')
        else:
            table = prettytable.PrettyTable()
            table.field_names = ['№', 'Activion keys']
            for i in f:
                if not 'Ключи' in i:
                    x = i.split('.')
                    x = list([j.strip() for j in x])
                    table.add_row(x)
            print(table)
        f.close()
        self.commands()


class Generator:
    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            self.menu_choice = input(Fore.MAGENTA + 'Меню\n\t1.Генератор паролей\n\t2.Генератор ключей\n\t3.Выйти\n>>')
            match self.menu_choice.strip().lower():
                case '1':
                    PasswordGenerator()
                case '2':
                    KeyGenerator()
                case '3':
                    exit()
                case _:
                    print(f'Ошибка\nКоманды {self.menu_choice} не существует\nПопробуйте еще раз')
                    continue


if __name__ == '__main__':
    Generator()
