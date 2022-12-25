import random
import json
from faker import Faker
from conf import MODEL
BOOKS_FILE = "books.txt"
pk = 1
def get_title() -> str: #Генерирем название книги случайным образом
    with open(BOOKS_FILE, encoding="utf-8") as f:
        data = f.readlines()
    return random.choice(data)

def get_year() -> int: #Генерируем год случайным образом
    return random.randint(1980, 2022)

def get_pages() -> int: #Генерируем номер страницы случайным образом
    return random.randint(1, 462)

def get_isbn13() -> str: #Генерируем книжный номер случайным образом
    fake = Faker()
    return fake.isbn13()

def get_rating() -> int: #Генерируем число с плавающей запятой в диапазоне от 0 до 5 обе границы включительно случайным образом
    return round(random.random(), 5)

def get_price() -> int: #Генерируем число с плавающей запятой случайным образом
    i = random.randint(1, 5)
    return round(random.random(), i)

def get_author() -> list: #Генерируем список авторов, который одержит от 1 до 3 авторов. Имя и фамилия автора выбираются случайным образом с помощью модуля Faker
    fake = Faker()
    list_author = []
    for i in range(random.randint(1, 3)):
        list_author.append(fake.name())
    return list_author

def count(start_number: float = 1, step: float = 1) -> dict:
    """
    Создём функцию-генератор, которая возвращает словарь
    :param start_number:
    :param step:
    :yield:
    """
    pk = start_number #стартовая позиция автоинкремента
    while True:
        dict_ = {
            "model": MODEL,
                    "pk": pk,
                           "fields": {
            "title": get_title(),
            "year": get_year(),
            "pages": get_pages(),
            "isbn13": get_isbn13(),
            "rating": get_rating(),
            "price": get_price(),
            "author": get_author()
        }
        }
        yield dict_
        pk += 1  # увеличиваем показатель счётчика на 1

def main():
    my_count = count() # инициализировать генератор книг
    data = [next(my_count) for _ in range(100)]# составить список из 100 книг
    with open("spisok.json", "w", encoding="utf-8") as f: # записать этот список в json
        f.write(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == '__main__': #Запуск программы
    main()
    my_count = count()
    print(next(my_count))





