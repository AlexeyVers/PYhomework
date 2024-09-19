from threading import Thread
from time import sleep
from random import randint
import queue


class Table:
    def __init__(self, number, guest=None):
        self.number = str(number)
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = str(name)

    def run(self):
        sleep(randint(3, 10))


class Cafe():
    def __init__(self, *cafe):
        self.cafe = []
        for table in cafe:
            self.cafe.append(table)

        self.queue = queue.Queue()
        self.tables = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            number = 0
            for table in self.cafe:
                number += 1
                if not table.guest:
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    guest.start()
                    guest.join()
                    break
                elif number == len(self.cafe):
                    self.queue.put(guest)
                    print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty():
            for table in self.cafe:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла) и Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    table.guest.start()
                    table.guest.join()
                    print(f'{table.guest.name}, вышел из очереди и сел за стол {table.number}')



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
