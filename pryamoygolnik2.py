# Разработайте класс Rectangle.

# При инициализации класс принимает два кортежа рациональных координат противоположных углов прямоугольника (со сторонами параллельными осям координат).

# Класс должен реализовывать методы:

# perimeter — возвращает периметр прямоугольника;
# area — возвращает площадь прямоугольника.
# Все результаты вычислений нужно округлить до сотых.

class Rectangle:
    def __init__(self, corner1, corner2):
        self.x1,self.y1 = corner1
        self.x2, self.y2 = corner2
        self.left = min(self.x1, self.x2)
        self.right = max(self.x1, self.x2)
        self.down = min(self.y1, self.y2)
        self.top = max(self.y1, self.y2)
    
    def perimeter(self):
        shirina = self.right - self.left
        height = self.top - self.down
        zn_perimeter = 2 * (shirina + height)
        return round(zn_perimeter, 2)  #раунд чтоб округлить, а 2 - кол-во знаков после запятой
    
    def area(self):
        shirina = self.right - self.left
        height = self.top - self.down
        zn_area = shirina * height
        return round(zn_area, 2)
# Расширим функционал класса написанного вами в предыдущей задаче.

# Реализуйте методы:

# get_pos() — возвращает координаты верхнего левого угла в виде кортежа;
# get_size() — возвращает размеры в виде кортежа;
# move(dx, dy) — изменяет положение на заданные значения;
# resize(width, height) — изменяет размер (положение верхнего левого угла остаётся неизменным).

    def get_pos(self):
        return (self.left, self.top)
    
    def get_size(self):
        shirina = self.right - self.left
        height = self.top - self.down
        return (shirina, height)
    
    def move(self, dx, dy):
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy
        self.left += dx
        self.right += dx
        self.down += dy
        self.top += dy
    def resize(self, width, height):    
        c_left = self.left
        c_top = self.top
        self.right = c_left + width
        self.down = c_top - height
        self.x1 = self.left
        self.y1 = self.top
        self.x2 = self.right
        self.y2 = self.down
# Необходимо ещё немного доработать предыдущую задачу.

# Разработайте методы:

# turn() — поворачивает прямоугольник на 90° по часовой стрелке вокруг его центра;
# scale(factor) — изменяет размер в указанное количество раз, тоже относительно центра.
# Все вычисления производить с округлением до сотых.

    def turn(self):
        center_x = (left + right) / 2
        center_y = (down + top) / 2
        


rectangle1 = Rectangle(( 2, 0 ), ( 1, 0 ))
print(rectangle1.perimeter()) 
print(rectangle1.area())
print(rectangle1.get_pos())
print(rectangle1.get_size()) 
print(rectangle1.move(44, 67))   
print(rectangle1.resize())
print(rectangle1.turn())



