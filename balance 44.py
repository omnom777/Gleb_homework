class Safe:
    def __init__(self, spisok, password):
        self.__spisok = spisok
        self.__password = password
    
    def change_password(self, password, new_password):
        if password == self.__password:
            self.__password = new_password
            return True
        else:
            return False
    
    def add_note(self, password, new_note):
        if password == self.__password:
            self.__spisok.append(new_note)
            return True
        else:
            return False
    
    def watch_note(self, password):
        if password == self.__password:
            return self.__spisok
            return True
    
    def delete_all_notes(self, password):
        if password == self.__password:
            self.__spisok = []
            return True


safe = Safe([], "1234")
while True:

    print("Выберите действие: 1.Изменить пароль 2.добавить заметку 3.просмотреть заметки 4.удалить все заметки")
    option = int(input())
    if option == 1:
        print('Напишите текущий пароль и новый пароль')
        cur_pas = input()
        new_pas = input()
        result = safe.change_password(cur_pas, new_pas)
        if result == True:
            print("пароль изменен")
        else:
            print("пароль не изменен")
    
    if option == 2:
        print('Напишите текущий пароль и новую заметку')
        cur_pas = input()
        new_note = input()
        result = safe.add_note(cur_pas, new_note)
        if result == True:
            print("заметка сохранена")
        else:
            print("заметка не сохранена")
    
    if option == 3:
        print('Напишите текущий пароль')
        cur_pas = input()
        result = safe.watch_note(cur_pas, )
        if result != None:
            print(result)
        else:
            print("пароль не верен")
    


        


