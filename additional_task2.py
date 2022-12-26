import random
BOOKS_FILE = "books.txt"

def get_title() -> str: #Генерирем название книги случайным образом
    with open(BOOKS_FILE, encoding="utf-8") as f:
        data = f.readlines()
    return random.choice(data)

def val_title(n):
    try:
        len(get_title()) > n  #
    except ValueError :  #
        print(get_title())

if __name__ == '__main__': #Запуск программы
    print(val_title(10))