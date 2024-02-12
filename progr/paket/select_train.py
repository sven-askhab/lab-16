def select_train(trains):
    """
    Выбрать поезд с заданным номером.
    """
    search_train_number = input("\nВведите номер поезда для поиска: ")
    found_train = None
    for train in trains:
        if train["номер поезда"] == search_train_number:
            found_train = train
            print(found_train)
            break

    if found_train is None:
        print(f"\nПоезда с номером {search_train_number} не найдено.")