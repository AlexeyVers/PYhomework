from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        read_ = open(file_name, 'w', encoding='utf-8')
        read_.write(str(data_set))
        read_.close()
    return write_everything

write = get_advanced_writer('test.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
