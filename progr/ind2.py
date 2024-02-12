#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from paket import *
import sys


def main():
    """
    Главная функция программы.
    """
    trains = []

    while True:
        user_input = input(">>> ").lower()

        if user_input == 'exit':
            break

        elif user_input == 'add':
            add_train.add_train(trains)

        elif user_input == 'list':
            list_trains.list_trains(trains)

        elif user_input == 'select':
            select_train.select_train(trains)

        elif user_input == 'help':
            help_command.help_command()

        else:
            print(f"Неизвестная команда {user_input}", file=sys.stderr)


if __name__ == '__main__':
    main()