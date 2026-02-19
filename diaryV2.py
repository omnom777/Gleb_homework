#метод исправления двойки
class Diary:
    def __init__(self, subjects=("","","","","")):
        
        self._subjects = []
        self._grades = []

    def add_grade(self, subject, grade):
        if not isinstance(subject, str):     #isinstance() - проверяет, принадлежит ли объект определённому классу или типу данных
            print("предмет должен быть строкой")
            return
        if not isinstance(grade, (int, float)): 
            print("оценка должна быть числом")
            return
        if grade < 2 or grade > 5:
            print("оценка должна быть от 2 до 5")
            return

        self._subjects.append(subject)
        self._grades.append(grade)

    def get_average(self, subject):
        vsego = 0
        count = 0
        for i in range(len(self._subjects)):
            if self._subjects[i] == subject:
                vsego += self._grades[i]
                count += 1     
        if count == 0:
            return 0.0
        return vsego / count
    
    def get_all_average(self):
        if not self._grades: 
            return 0.0
        return sum(self._grades) / len(self._grades)
    
    def get_bad_subjects(self):
        subjects_avg = {}
        
        for i in range(len(self._subjects)):
            subject = self._subjects[i]
            vsego = 0
            count = 0
            for k in range(len(self._subjects)):
                if self._subjects[k] == subject:
                    vsego += self._grades[k]
                    count += 1
            subjects_avg[subject] = vsego / count
        bad_subjects = []
        for subject in subjects_avg:
            if subjects_avg[subject] < 3.5:
                bad_subjects.append(subject)
        return bad_subjects
    
    def reset_diary(self):
        self._subjects = []
        self._grades = []
    def fix_last_2(self, subject, new_grade):
        if new_grade < 2 or new_grade > 5:
            print("оценка должна быть от 2 до 5")
            return False
        for i in range(len(self._subjects) - 1, -1, -1): #for i in range(start, stop, step)
            if self._subjects[i] == subject and self._grades[i] == 2:
                self._grades[i] = new_grade
                print(f"Исправлена на {new_grade}")
                return True


my_diary = Diary()
my_diary.add_grade("Биология", 5)
my_diary.add_grade("Биология", 4)
my_diary.add_grade("География", 3)
my_diary.add_grade("География", 2)
my_diary.add_grade("История", 5)
print(my_diary.get_average("Биология"))
print(my_diary.get_average("География"))
print(my_diary.get_all_average())
print(my_diary.get_bad_subjects())
my_diary.reset_diary()
print(my_diary.get_all_average())