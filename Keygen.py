import setup
import random
import tqdm
import time
import prettytable
from check_size_file import *


class KeyGenerator:

    def __init__(self):
        self.alphabet = [chr(i) for i in range(97, 123)]
        self.key_windows = []
        self.commands()

    def commands(self):
        while True:
            self.cmd = input(
                '\nВыберите № команды для продолжения:\n\t1.Сгенерировать лицензионные ключи\n\t2.Показать сохранные ключи\n\t3.Выход в главное меню\n>>')
            if self.cmd.strip() == '1':
                self.selection()
            elif self.cmd.strip() == '2':
                self.saved_key()
            elif self.cmd.strip() == '3':
                setup.Generator()
            else:
                print(f'Ошибка\nКоманды {self.cmd} не существует\nПопробуйте еще раз')
                continue

    def selection(self):
        while True:
            self.choice_key = input(
                '\nВыберите № ключа которого вы хотели бы сгенерировать(для выхода в меню введите exit):\n\t1.Windows OS\n>>')
            match self.choice_key.strip().lower():
                case '1':
                    self.keygen_windows()
                case 'exit':
                    self.commands()
                case _:
                    print(f'Ошибка\nКоманды {self.choice_key} не существует\nПопробуйте еще раз')
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
        print('\nПодождите, лицензионные ключи генерируются...')
        for i in tqdm.tqdm(range(1, 101)):
            time.sleep(0.1)
        print('Ключи активации успешно сгенерированы')
        save_key = input('Хотите сохранить сгенерированные ключи(да/нет):')
        while True:
            if save_key.strip() == 'да':
                print('Пароль успешно сохранен!')
                with open('resources/saved activion keys windows.txt', 'r') as file:
                    strings = file.readlines()
                n = len(strings)
                f = open('resources/saved activion keys windows.txt', 'a')
                if empty_file('resources/saved activion keys windows.txt'):
                    f.write('Ключи активации Windows OS:\n')
                    n += 1
                for i in self.key_windows:
                    f.write(f'{n}. {i}\n')
                    n += 1
                f.close()
                self.commands()
            elif save_key.strip() == 'нет':
                print('Лицензионные ключи не были сохранены')
                self.commands()
            else:
                print('Ошибка\nДля продолжения используйте только да/нет\nПопробуйте заново')
                save_key = input('Хотите сохранить сгенерированные ключи(да/нет):')
                continue
        self.commands()

    def saved_key(self):
        print('Ваши лицензионные ключи:\n')
        f = open(
            'resources/saved activion keys windows.txt',
            'r')
        file = 'resources/saved activion keys windows.txt'
        if empty_file(file):
            print(
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
