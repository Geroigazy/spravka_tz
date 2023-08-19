import json

def load_data(file_path: str):
    """
    Загружает данные из JSON-файла.

    Parameters:
        file_path (str): Путь к JSON-файлу.

    Returns:
        List[Dict[str, Any]]: Список записей из JSON-файла.
    """
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []
    return data

def save_data(file_path, data):
    """
    Сохраняет данные в JSON-файл.

    Parameters:
        file_path (str): Путь к JSON-файлу.
        data (List[Dict[str, Any]]): Список записей для сохранения.
    """
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

def display_records(records):
    """
    Выводит записи на экран.

    Parameters:
        records (List[Dict[str, Any]]): Список записей для вывода.
    """
    for record in records:
        print("Фамилия:", record.get("surname"))
        print("Имя:", record.get("name"))
        print("Отчество:", record.get("fathers_name"))
        print("Организация:", record.get("dep"))
        print("Рабочий телефон:", record.get("wphone"))
        print("Личный телефон:", record.get("lphone"))
        print("=" * 40)

def add_record():
    """
    Добавляет новую запись.

    Returns:
        Dict[str, Any]: Новая запись.
    """
    record = {}
    record["surname"] = input("Фамилия: ")
    record["name"] = input("Имя: ")
    record["fathers_name"] = input("Отчество: ")
    record["dep"] = input("Организация: ")
    record["wphone"] = input("Рабочий телефон: ")
    record["lphone"] = input("Личный телефон: ")
    return record

def edit_record(record):
    """
    Редактирует существующую запись.

    Parameters:
        record (Dict[str, Any]): Запись для редактирования.

    Returns:
        Dict[str, Any]: Отредактированная запись.
    """
    record["surname"] = input("Новая фамилия: ")
    record["name"] = input("Новое имя: ")
    record["fathers_name"] = input("Новое отчество: ")
    record["dep"] = input("Новая организация: ")
    record["wphone"] = input("Новый рабочий телефон: ")
    record["lphone"] = input("Новый личный телефон: ")
    return record

def search_records(records):
    """
    Выполняет поиск записей по заданным критериям.

    Parameters:
        records (List[Dict[str, Any]]): Список записей для поиска.
    """
    search_term = input("Введите фамилию или имя для поиска: ")
    search_results = []

    for record in records:
        if search_term.lower() in record["surname"].lower() or search_term.lower() in record["name"].lower():
            search_results.append(record)

    if search_results:
        print("Результаты поиска:")
        display_records(search_results)
    else:
        print("Записей не найдено.")

def main():
    """
    Основная функция программы. Взаимодействие с пользователем.
    """

    file_path = "phonebook.json"
    records = load_data(file_path)

    while True:
        print("\n1. Вывод записей")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск записей")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            display_records(records)
        elif choice == "2":
            new_record = add_record()
            records.append(new_record)
            save_data(file_path, records)
            print("Запись добавлена.")
        elif choice == "3":
            display_records(records)
            index = int(input("Введите индекс записи для редактирования: "))
            if 0 <= index < len(records):
                edited_record = edit_record(records[index])
                records[index] = edited_record
                save_data(file_path, records)
                print("Запись отредактирована.")
            else:
                print("Неверный индекс.")
        elif choice == "4":
            search_records(records)
        elif choice == "5":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите корректное действие.")

if __name__ == "__main__":
    main()
