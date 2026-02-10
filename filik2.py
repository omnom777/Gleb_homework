# Реализовать класс Game и Player
# В цикле while true ожидать сначала номер игрока, потом действие игрока: move_up, move_down, move_left, move_right.
# При получении команды меняем координаты x и y игрока соответственно при помощи одного из 4 методов.
# Game хранит словарь айди-игрок и вызывает действие у каждого из них при получении номера игрока
# Junior — с окладом 10 тугриков в час;
# Middle — с окладом 15 тугриков в час;
# Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за каждое новое повышение.
class Programmer:
    def __init__(self, name, grade="Junior"):
        self.name = name
        self.grade = grade
        self.time = 0
        if self.grade == "Junior":
            self.rate = 10
        elif self.grade == "Middle":
            self.rate = 15
        elif self.grade == "Senior":
            self.rate = 20

    def info(self):
        return f"{self.name}, {self.time}, {self.rate * self.time}"

    def grade_up(self):
        if self.grade == "Junior":
            self.grade = "Middle"
            self.rate = 15
        elif self.grade == "Middle":
            self.grade = "Senior"
            self.rate = 20
        elif self.grade == "Senior":
            self.rate += 1

    def work(self, time):
        self.time += time



programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.grade_up()
programmer.work(500)
print(programmer.info())
programmer.grade_up()
programmer.work(250)
print(programmer.info())
programmer.grade_up()
programmer.work(250)
print(programmer.info())
  
        




        

    

