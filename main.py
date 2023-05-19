from conf import model
import faker
import random
import json

titles_file = 'books.txt'  # заголовки книг

def load_titles() -> str:
    '''
    Функция выбирает случайное название книги из файла books.txt
    :return: название книги
    '''
    with open(titles_file, 'r', encoding='utf-8') as f:
        return random.choice([line.strip() for line in f.readlines()])

def generate_publish_year() -> int:
    '''
    Функция генерации года
    :return: год от 1900, до 2023
    '''
    return random.randint(1900, 2023)

def generate_page_count() -> int:
    '''
    Функция генерации числа страниц
    :return: страницы от 50 до 1000
    '''
    return random.randint(50, 1000)

def generate_isbn() -> str :
    '''
    Функция генерации isbn, которая принимает экземпляр класса faker
    :return: isbn
    '''
    fake_ = faker.Faker()
    isbn = fake_.isbn13()
    return isbn

def generate_rating() -> float:
    '''
    Функция генерации рейтинга книги в промежутке от 1 до 5, с округлением до 2-х знаков после запятой
    :return: число float
    '''
    return round(random.uniform(0, 5), 2)

def generate_price() -> float:
    '''
    Функия генерации цены книги в промежутке от 300 до 3000, с округлением до 2-х знаков после запятой
    :return: число float
    '''
    return round(random.uniform(300, 3000), 2)

def generate_authors():
    '''
    Функция генерации 3-х авторов
    :return:
    '''
    fake_authors = faker.Faker('ru_RU')
    fake_authors_list = [fake_authors.name() for _ in range(3)]
    return fake_authors_list

def generator(count=1):
    '''
    Функция генерации словарей
    '''

    while True:
        dict_ = {"model": model,
                 "pk": count,
                 "fields": {
                     "title": load_titles(),
                     "year": generate_publish_year(),
                     "pages": generate_page_count(),
                     "isbn13": generate_isbn(),
                     "rating": generate_rating(),
                     "price": generate_price(),
                     "author": generate_authors()
                 }
                 }

        yield dict_
        count += 1

def main():
    '''
    Функция запуска генератора
    '''
    generator_ = generator()
    list_ = [next(generator_) for _ in range(100)]

    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(list_, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()