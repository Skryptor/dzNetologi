class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['Введение в программирование']
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades_Fstudent:
                lecturer.grades_Fstudent[course] += [grade]
            else:
                lecturer.grades_Fstudent[course] = [grade]
        else:
            return 'Ошибка'

    def calculate_grades(self):
        all_grades = 0
        i = 0
        for grades in self.grades.values():
            all_grades += sum(grades)
            i += len(grades)
        Averaga = all_grades / i
        return round(Averaga, 1)
    
    def __str__(self):
        return (F'Студенты \n'
                F'Имя: {self.name}'
                F'\nФамилия: {self.surname}'
                F'\nСредняя оценка за домашние задания: {self.calculate_grades()} '
                F'\nКурсы в процессе изучения: {' '.join(self.courses_in_progress)} '
                F'\nЗавершенные курсы: {' '.join(self.finished_courses)}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name,surname)
        self.grades_Fstudent = {}

    def calculate_grades(self):
        all_grades = 0
        i = 0
        for grades in self.grades_Fstudent.values():
            all_grades += sum(grades)
            i += len(grades)
        Averaga = all_grades / i
        return round(Averaga, 1)

    def __str__(self):
        return (F'Лекторы \nИмя: {self.name}\nФамилия: {self.surname} '
                F'\nСредняя оценка за лекции: {self.calculate_grades()} ')

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_Fstudent = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return F'Эксперты \nИмя: {self.name}\nФамилия: {self.surname}'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_lecturer = Lecturer('Ivan', 'Petrov')
cool_lecturer.courses_attached.append('Python')

best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 9)



print(cool_reviewer)

print(cool_lecturer)

print(best_student)
