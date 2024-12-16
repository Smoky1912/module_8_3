# класс исключения для некорр. VIN номера
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message  # сохр. сообщ. об ошибке

# класс исключения для некорр. номера авто
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message  # сохр. сообщ. об ошибке

# зададим класс Car
class Car:
    def __init__(self, model, vin, numbers):
        self.model = model  # название автомобиля (строка) - публ.
        self.__vin = vin  # vin номер автомобиля (целое число) - приват.
        self.__numbers = numbers  # атрибут для номера авто - приват.

        # проверка корр. VIN номера
        if not self.__is_valid_vin(self.__vin):
            raise IncorrectVinNumber('Некорректный тип vin номер')

        # проверка корр. номера авто
        if not self.__is_valid_numbers(self.__numbers):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

    # приват. метод для проверки корр. VIN номера
    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):  # целое ли число vin_number
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin_number <= 9999999):  # находится ли vin_number в задан. диапазоне
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True  # возврат True, если искл. не были выброшены

    # приват. метод проверки корр. номера авто
    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):  # строка ли numbers
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:  # состоит ли строка ровно из 6 символов
            raise IncorrectCarNumbers('Неверная длина номера')
        return True  # возврат True, если искл. не были выброшены

# Пример Car
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')