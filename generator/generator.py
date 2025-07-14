import random

from data.data import Person
from faker import Faker

faker_en = Faker('En')

def generated_person():
    return Person(
    first_name=faker_en.firsn_name(),
    last_name=faker_en.last_name(),
    email=faker_en.email(),
    current_address=faker_en.address(),
    mobile=faker_en.msidsn(),
    subject='English'
    )

def generate_file():
    path = rf'/Users/oleksiybeseda/PycharmProjects/PythonAQATestProject/.venv311/test{random.randint(10, 100)}.txt'
    file = open(path, 'w')
    file.write(f'Helloworld{random.randint(23, 100)}')
    file.close()
    return path