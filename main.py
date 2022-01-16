# Python Version: 10.0.0
# 6th Computer's Group
#
import csv
from os import system


class File:
    def __init__(self, position):
        self.position_login = position
        self.position = None
        self.users = None
        self.data_base = None
        self.user = None

    def registry(self):
        system('cls')
        print(' $ Registry new user $ ')
        # select position
        print(
            '[1] register an employee\n'
            '[2] register a teacher\n'
            '[3] register a student'
        )
        self.position = ['employee', 'teacher', 'student'][int(input('=> ')) - 1]
        # create username for new user
        unique = True
        while True:
            username = input('username: ')
            with open('users.csv', 'r') as file:
                _users = csv.reader(file)
                for user in _users:
                    if username == user[0]:
                        _unique = False
                        print('username is not unique!\ntry another username')
                        break
            if unique:
                break
        info = [
            username,
            input('password: '),
            input('national ID: '),
            input('first name: '),
            input('last name: '),
            self.position
        ]
        with open('users.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(info)
        input('registry was successful!\npress the enter key to continue ...')

    def login(self):
        system('cls')
        print(' $ Login $')
        username = input('username: ')
        password = input('password: ')

        with open('users.csv', 'r') as file:
            users = csv.reader(file)
            for _user in users:
                _user = list(_user)
                if self.position_login == _user[5]:
                    if username == _user[0]:
                        if password == _user[1]:
                            return _user
            else:
                print('username or password is incorrect')
                exit()

    def edit(self):
        system('cls')
        print('$ edit user info $')
        while True:
            username = input('username: ')
            with open('users.csv', 'r') as file:
                self.users = list(csv.reader(file))
                index = 0
                for user in self.users:
                    if user[0] == username:
                        self.position = user[5]
                        self.user = index
                        break
                    index += 1
            if self.user is not None:
                break
            else:
                print('user not found!\ntry again')
        print('enter new info: ')
        info = [
            username,
            input('password: '),
            input('national ID: '),
            input('first name: '),
            input('last name: '),
            self.position,
        ]
        self.users[index] = info
        system('del users.csv')
        with open('users.csv', 'w', ) as file:
            writer = csv.writer(file)
            self.users.remove([])
            writer.writerows(self.users)
        input('edit was successful!\npress the enter key to continue ...')

    def delete(self):
        system('cls')
        print('$ delete user info $')
        while True:
            username = input('username: ')
            with open('users.csv', 'r') as file:
                self.users = list(csv.reader(file))
                index = 0
                for user in self.users:
                    if user[0] == username:
                        self.position = user[5]
                        self.user = index
                        break
                    index += 1
            if self.user is not None:
                break
            else:
                print('user not found!\ntry again')
        self.users.remove(self.users[index])
        system('del users.csv')
        with open('users.csv', 'w', ) as file:
            writer = csv.writer(file)
            self.users.remove([])
            writer.writerows(self.users)
        input('delete was successful!\npress the enter key to continue ...')


class Employee:
    def __init__(self):
        file = File('employee')
        user = file.login()
        while True:
            print(f' $ Employee $ {user[3]}, {user[2]}\n[1]')
            print(
                '[1] manage users\n'
                '[2] manage lessons\n'
                '[0] exit'
            )
            option = input('=> ').strip()
            match option:
                case '1':
                    system('cls')
                    print(
                        ' $ manage users $\n'
                        '[1] register a new user\n'
                        '[2] edit an existing user account\n'
                        '[3] delete an existing user account'
                    )
                    option = input('=> ').strip()
                    match option:
                        case '1':
                            file.registry()
                        case '2':
                            file.edit()
                        case '3':
                            file.delete()
                case '0':
                    exit()


if __name__ == '__main__':
    system('cls')
    print(
        ' $ university system $\n'
        'select your position:\n'
        '[1] employee\n'
        '[2] teacher\n'
        '[3] student'
    )
    position = input('=> ').strip()

    match position:
        case '1':
            employee = Employee()
