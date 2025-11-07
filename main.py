from address_book import AddressBook, Record
from serialization import save_data, load_data


def main():
    book = load_data()
    print("Адресна книга завантажена!")

    while True:
        command = input("Введіть команду (add/show/exit): ").strip().lower()

        if command == "add":
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            record = Record(name, phone)
            book.add_record(record)
            print(f"Додано запис: {record}")

        elif command == "show":
            print("Поточна адресна книга:")
            print(book)

        elif command == "exit":
            save_data(book)
            print("Дані збережено. До зустрічі!")
            break

        else:
            print("Невідома команда")


if __name__ == "__main__":
    main()
