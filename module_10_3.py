from threading import Thread, Lock
from random import randrange
from time import sleep

class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = int()
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            amount = randrange(50, 500)
            if self.lock.acquire() and self.balance >= 500:
                print(2)
                self.lock.release()
            self.balance =+ amount
            print(f'Пополнение на {amount}, текущий баланс {self.balance}')

    def take(self):
        for _ in range(100):
            amount = randrange(50, 500)
            print(f'Запрос на {amount}, баланс {self.balance}')
            if self.balance >= amount:
                self.balance = self.balance - amount
                print(f'Списали {amount}, баланс {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
