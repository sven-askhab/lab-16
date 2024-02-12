def outer_function(f):
    """
    Внешняя функция
    """

    def inner_function(a, b):
        """
        Возвращает строку с вычисленным значением функции f
        """
        result = f(a, b)
        return f"Для значений {a}, {b} функция f(a, b) = {result}"

    return inner_function


def f(a, b):
    """
    Делит параметры друг на друга и умножает на 2
    """
    return a / b * 2
