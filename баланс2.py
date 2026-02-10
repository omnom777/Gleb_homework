#Задача: сделать терминальную копилку для ведения учета за деньгами
#Нужно создать класс Koplika с методами polozhit, snyat, postavit_tzel, hvatit_na_tzel.
#Методы делают соответственно: пополняют баланс, уменьшают баланс, ставят цель накоплений, проверяют хватает ли денег в копилке для цели.
#При запуске программа должна спрашивать у пользователя действие (одно из 4), и если пользователь напишет exit то программа должа завершиться. Начинаем с балансом 100.
class Koplika:
    def __init__(self, nachalniy_balans=100):
        self.balans = nachalniy_balans
        self.tzel = None
    def polozhit(self, summa):
        self.balance += summa
    def snyat(self, summa):
        if summa > self.balans:
            print("Ошибка")
            return        
        else:
            self.balance -= summa
    def postavit_tzel(self, summa):
            self.tzel = summa
    def hvatit_na_tzel(self):
        if self.balance >= self.tzel:
            print("хватает на цель")
while True:
    command = input()
    
