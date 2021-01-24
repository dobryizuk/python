from faker import Faker

faker = Faker()


def random_word():
    return faker.word()


def random_int():
    return faker.pyint()
