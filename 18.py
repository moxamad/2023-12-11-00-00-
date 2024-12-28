from threading import Thread, Lock
from time import sleep
from random import randint


class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            a = randint(50, 500)
            self.balance += a
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f"Пополнение: {a}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(100):
            a = randint(50, 500)
            print(f'Запрос на {a}')
            if a <= self.balance:
                self.balance -= a
                print(f"Снятие: {a}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')