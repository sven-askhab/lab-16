def add_train(trains):
    """
    Добавить поезд.
    """
    train_number = input("Номер поезда: ")
    destination = input("Название пункта назначения: ")
    departure_time = input("Время отправления: ")

    train_info = {'номер поезда': train_number,
                  'название пункта назначения': destination,
                  'время отправления': departure_time}

    trains.append(train_info)

    if len(trains) > 1:
        trains.sort(key=lambda x: x['номер поезда'])