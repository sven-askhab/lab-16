def list_trains(trains):
    """
    Отобразить список поездов.
    """
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
    )
    print(line)
    print('| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
        "№",
        "Номер поезда",
        "Пункт назначения",
        "Время"
    ))
    print(line)

    for idx, train_info in enumerate(trains, 1):
        print('| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
            idx,
            train_info.get('номер поезда', ''),
            train_info.get('название пункта назначения', ''),
            train_info.get('время отправления', '')
        ))

    print(line)