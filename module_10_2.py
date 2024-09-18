from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)

    def run(self):
        count_enemy = 100
        i = 0
        print(f'{self.name}, на нас напали')
        while count_enemy > 0:
            sleep(1)
            i += 1
            count_enemy = count_enemy - self.power
            print(f'{self.name}, сражается {i} дней, но ещё осталось {count_enemy} воинов\n')
        print(f'{self.name}, одержал победу спустя {i} дней')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
