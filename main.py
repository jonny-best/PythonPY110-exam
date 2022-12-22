import random
from faker import Faker
from conf import MODEL
BOOKS_FILE = "books.txt"
pk = 1

def get_title():
    with open(BOOKS_FILE, encoding="utf-8") as f:
        data = f.readlines()
    return random.choice(data)

def get_year():
    return random.randint(1980, 2022)

def get_pages():
    return random.randint(1, 462)

def get_isbn13():
    fake = Faker()
    return fake.isbn13()

def get_rating():
    return round(random.random(), 5)

def get_price():
    i = random.randint(1, 5)
    return round(random.random(), i)

def get_author():
    fake = Faker()
    return fake.name()

def count(start_number: float = 1, step: float = 1):
    while True:
        yield start_number
        start_number += step

if __name__ == '__main__':
    fields = {
        "title": get_title(),
        "year": get_year(),
        "pages": get_pages(),
        "isbn13": get_isbn13,
        "rating": get_rating,
        "price": get_price,
        "author": get_author
    }

print(fields)


