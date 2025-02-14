from char_queue import CharQueue


def display_menu():
    """Вывод меню."""
    print("\nМеню:")
    print("1. Добавить элемент в очередь")
    print("2. Удалить элемент из очереди")
    print("3. Показать очередь")
    print("4. Выйти")


def main():
    """Основная функция для работы с меню."""
    size = int(input("Введите размер очереди: "))
    queue = CharQueue(size)

    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            item = input("Введите символ для добавления: ")
            try:
                queue.enqueue(item)
                print(f"Элемент '{item}' добавлен в очередь.")
            except OverflowError as e:
                print(e)
        elif choice == "2":
            try:
                item = queue.dequeue()
                print(f"Удаленный элемент: {item}")
            except IndexError as e:
                print(e)
        elif choice == "3":
            queue.show()
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()