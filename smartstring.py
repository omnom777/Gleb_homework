# Создайте класс SmartString, который ведёт себя как строка, но:
# len() возвращает не длину строки, а количество уникальных символов в ней
# При преобразовании в строку str() выводит исходную строку, а рядом в скобках — длину и количество уникальных символов
# Поддерживает сложение с другой строкой или SmartString, при этом новое значение тоже должно быть SmartString

class SmartString:
    def __init__(self, stroka):
        self.stroka = stroka
    def __len__(self):
        return len(set(self.stroka))  #колво элементов в мнве
    def __str__(self):
        length = len(self.stroka)
        unic_simbols = len(set(self.stroka))
        return f"{self.stroka} ({length}, {unic_simbols})" 
    def __add__(self, other):
        if isinstance(other, SmartString):
            other_str = other.stroka
        else:
            other_str = str(other)
        return SmartString(self.stroka + other_str)


s = SmartString("abccc")
print(len(s))
s2 = s + "dddfg"
print(str(s2))
print(str(s2 + "!!!"))
