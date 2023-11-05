import random
import time
import os
import tqdm
import prettytable


class PasswordGenerator:
    print('Генератор паролей')

    def __init__(self):
        self.alphabet = [chr(i) for i in range(97, 123)]
        self.saved_passwords = []
        self.dataCreationTime = []

    def commands(self):  # функция команд
        while True:
            self.cmd = input(
                '\nВыберите № команды для продолжения:\n\t1.Random password generation\n\t2.Show saved passwords\n\t3.Exit\n>>')
            if self.cmd.strip() == '1':
                self.attribute()
            elif self.cmd.strip() == '2':
                self.saved_passwd()
            elif self.cmd.strip() == '3':
                exit()
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
            random_lettter = random.choice(self.alphabet)
            random_num = random.randint(0, 9)
            x = random.randint(0, 4)
            if x == 0 or x == 1:
                self.gen.append(str(random_num))
            elif x == 2 or x == 3:
                self.gen.append(random_lettter)
            else:
                self.gen.append(random_lettter.upper())
        self.passwd = ''.join(self.gen)
        print('\nПодождите, ваш пароль генерируется...')
        for i in tqdm.tqdm(range(1, 101)):
            time.sleep(0.1)
        print(f'Ваш пароль успешно сгенерирован\nСгенерированный пароль:{self.passwd}')
        savepsswd = input('Хотите сохранить пароль(да/нет):')
        while True:
            if savepsswd.strip() == 'да':
                print('Пароль успешно сохранен!')
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
                print('Пароль не был сохранен')
                self.commands()
            else:
                print('Ошибка\nДля продолжения используйте только да/нет\nПопробуйте заново')
                savepsswd = input('Хотите сохранить пароль(да/нет):')

    def saved_passwd(self):  # сохраненные пароли
        print('Ваши сохраненные пароли:\n')
        f = open('generated saved passwords.txt', 'r')

        def is_empty_file(file_name):  # проверка пуст ли файл.txt
            file_info = os.stat(file_name)
            return file_info.st_size == 0

        file_name = 'generated saved passwords.txt'
        if is_empty_file(file_name):
            print('Password not found!\nДля создания новых паролей используйте команду "1.Random password generation"')
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


passwd_gen = PasswordGenerator()
passwd_gen.commands()
