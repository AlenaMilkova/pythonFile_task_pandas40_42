def read_contacts(file_name):
    contacts = []
    with open(file_name, 'r') as file:
        for line in file:
            contact = line.strip().split(',')
            contacts.append(contact)
    return contacts


def write_contacts(file_name, contacts):
    with open(file_name, 'w') as file:
        for contact in contacts:
            line = ','.join(contact)
            file.write(line + '\n')


def search_contacts(contacts, key):
    results = []
    for contact in contacts:
        for field in contact:
            if key.lower() in field.lower():
                results.append(contact)
                break
    return results


def display_contacts(contacts):
    if not contacts:
        print("Нет данных о контактах")
    else:
        for contact in contacts:
            print(', '.join(contact))


def update_contact(contacts, key):
    for contact in contacts:
        if key.lower() in contact[1].lower() or key.lower() in contact[0].lower():
            print("Найден контакт:")
            print(', '.join(contact))
            field = input("Выберите поле для обновления (фамилия, имя, отчество, номер): ")
            if field == 'фамилия':
                contact[0] = input("Введите новую фамилию: ")
            elif field == 'имя':
                contact[1] = input("Введите новое имя: ")
            elif field == 'отчество':
                contact[2] = input("Введите новое отчество: ")
            elif field == 'номер':
                contact[3] = input("Введите новый номер телефона: ")
            else:
                print("Некорректное поле. Обновление отменено.")


def delete_contact(contacts, key):
    deleted = False
    for contact in contacts:
        if key.lower() in contact[1].lower() or key.lower() in contact[0].lower():
            print("Найден контакт для удаления:")
            print(', '.join(contact))
            confirmation = input("Вы уверены, что хотите удалить этот контакт? (да/нет): ")
            if confirmation.lower() == 'да':
                contacts.remove(contact)
                deleted = True
                print("Контакт успешно удален.")
            else:
                print("Удаление отменено.")
            break
    if not deleted:
        print("Контакт не найден.")


def main():
    file_name = 'contacts.txt'
    contacts = read_contacts(file_name)

    while True:
        print("\n=== Телефонный справочник ===")
        print("1. Вывести все контакты")
        print("2. Добавить контакт")
        print("3. Найти контакт")
        print("4. Обновить контакт")
        print("5. Удалить контакт")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            contacts = read_contacts(file_name)
            display_contacts(contacts)
        elif choice == '2':
            contact = []
            contact.append(input("Введите фамилию: "))
            contact.append(input("Введите имя: "))
            contact.append(input("Введите отчество: "))
            contact.append(input("Введите номер телефона: "))
            contacts.append(contact)
            write_contacts(file_name, contacts)
            print("Контакт успешно добавлен")
        elif choice == '3':
            key = input("Введите ключевое слово для поиска: ")
            search_results = search_contacts(contacts, key)
            display_contacts(search_results)
        elif choice == '4':
            key = input("Введите имя или фамилию для поиска контакта: ")
            update_contact(contacts, key)
            write_contacts(file_name, contacts)
        elif choice == '5':
            key = input("Введите имя или фамилию для поиска контакта: ")
            delete_contact(contacts, key)
            write_contacts(file_name, contacts)
        elif choice == '0':
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()