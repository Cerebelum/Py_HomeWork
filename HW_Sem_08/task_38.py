# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def name_data():
    return input("Введите имя: ")


def patronymic_data():
    return input("Введите отчество: ")


def surname_data():
    return input("Введите фамилию: ")


def phone_data():
    return input("Введите номер телефона: ")


def address_data():
    return input("Введите адрес: ")


def input_contact():
    surname = surname_data()
    name = name_data()
    patronymic = patronymic_data()
    phone_number = phone_data()
    address = address_data()
    return f'{surname} {name} {patronymic}\n{phone_number}\n{address}'


def add_contact():
    contact = input_contact()
    with open('phone.txt', 'a', encoding='utf-8') as data:
        data.write(contact + '\n\n')


def read_file():
    with open('phone.txt', 'r', encoding='utf-8') as data:
        return data.read()


def print_contacts():
    data = read_file()
    print()
    print(data)


def search_contact():
    print('Варианты поиска:\n'
          '1. По фамилии\n'
          '2. По имени\n'
          '3. По отчеству\n'
          '4. По номеру телефона\n'
          '5. По адресу')
    choice = input('Выберите вариант поиска: ')
    i_choice = int(choice) - 1
    search = input('Введите данные: ')
    data_str = read_file().rstrip()
    if search not in data_str:
        print('Нет такого контакта')
    else:
        data_lst = data_str.split('\n\n')
        for contact_str in data_lst:
            contact_lst = contact_str.replace('\n', ' ').split()
            if search in contact_lst[i_choice]:
                print()
                print(contact_str)
                choice_search = input('Вы искали этот контакт? 1 - да, 2 - нет: ')
                if choice_search == "1":
                    return contact_str
        print('Контакты закончились. Нужного нет.')


def delete_contact2():
    print('Какую запись вы хотите удалить? ')
    contact = search_contact()
    if contact:
        print(contact)
        data = read_file()
        with open('phone.txt', 'w', encoding='utf-8') as data2:
            data = data.replace(contact + "\n\n", '')
            data2.write(data)


def change_contact2():
    print('Какой контакт вы хотите изменить? ')
    contact = search_contact()
    if contact:
        print(contact)
        new_contact = contact.replace('\n', ' ').split()
        print()
        print('Варианты замены:\n'
              '1. Фамилия\n'
              '2. Имя\n'
              '3. Отчество\n'
              '4. Номер телефона\n'
              '5. Адрес\n'
              '6. Контакт полностью')
        choice = input('Выберите вариант замены: ')
        if choice != "6":
            i_choice = int(choice) - 1
            change = input('Введите изменяемую часть контакта: ')
            new_contact[i_choice] = change
            new_contact = f'{new_contact[0]} {new_contact[1]} {new_contact[2]}\n{new_contact[3]}\n{new_contact[4]}'
        else:
            new_contact = input_contact()
        data = read_file()
        with open('phone.txt', 'w', encoding='utf-8') as data2:
            data = data.replace(contact, new_contact)
            data2.write(data)


def user_interface():
    with open('phone.txt', 'a', encoding='utf-8'):  # создаем файл если его нет
        pass
    cmd = None
    while cmd != '6':
        print('\nМеню:\n'
              '1. Запись контакта\n'
              '2. Вывести данные на экран\n'
              '3. Поиск контакта\n'
              '4. Изменение контакта\n'
              '5. Удаление контакта\n'
              '6. Выход')
        cmd = input('Введите номер операции: ')
        print()
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод. Повторите: ')
            cmd = input('Введите номер операции: ')
        match cmd:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                change_contact2()
            case '5':
                delete_contact2()
            case '6':
                print('До свидания))')


user_interface()
