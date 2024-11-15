class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades_Fstudent:
                lecturer.grades_Fstudent[course].append(grade)
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
        if i == 0:
            return 0
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
        if i == 0:
            return 0
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

class StudentVsLecturer:
    def __init__(self, student: Student, lecturer: Lecturer):
        self.student = student
        self.lecturer = lecturer

    def __eq__(self, vs):
        return self.student == vs.student and self.lecturer == vs.lecturer

    def __gt__(self, vs):
        return self.student > vs.student

    def __lt__(self, vs):
        return self.student < vs.student

    def vs(self):
        average_student = self.student.calculate_grades()
        average_lecturer = self.lecturer.calculate_grades()

        if average_student > average_lecturer:
            return 'Средняя оценка студентов выше, чем у лекторов!'
        elif average_student < average_lecturer:
            return 'Средняя оценка лекторов выше, чем у студентов!'
        else:
            return 'Все молодцы, оценки одинаковые, но Дима лучший молодец!'

    def __str__(self):
        return self.vs()

class All_Average_Grades:
    def __init__(self,students):
        self.students = students

    def all_grades_student(self):
        all_grades = 0
        i = 0
        for student in self.students:
            if isinstance(student, Student):
                for grades in student.grades.values():
                    all_grades += sum(grades)
                    i += len(grades)
            elif isinstance(student, Lecturer):
                for grades in student.grades_Fstudent.values():
                    all_grades += sum(grades)
                    i += len(grades)
        if i == 0:
            return 0
        Averaga = all_grades / i
        return round(Averaga, 1)

    def __str__(self):
        return f'Среднее значением по всем студентам: {self.all_grades_student()}'


best_student = Student('Ema', 'Stoun', 'Woman')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Ivan', 'Petrov')
cool_lecturer.courses_attached.append('Python')

best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 9)

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)

super_student = Student('Dmitryi', 'Skripnikov','SuperMan')
super_student.courses_in_progress += ['Python']
super_student.finished_courses += ['Введение в программирование']

super_reviewer = Reviewer('Спасибо', 'Большое')
super_reviewer.courses_attached.append('Python')

super_lecturer = Lecturer('Pavel', 'Molybog')
super_lecturer.courses_attached.append('Python')

super_student.rate_lecturer(super_lecturer, 'Python', 11)
super_student.rate_lecturer(super_lecturer, 'Python', 12)
super_student.rate_lecturer(super_lecturer, 'Python', 10)

super_reviewer.rate_hw(super_student,'Python', 12 )
super_reviewer.rate_hw(super_student,'Python', 11 )
super_reviewer.rate_hw(super_student,'Python', 10 )

Versus2 = StudentVsLecturer(super_student,super_lecturer)
Versus1 = StudentVsLecturer(best_student,cool_lecturer)

ALl_Grade_Student = All_Average_Grades([super_student,best_student])
ALl_Grade_Lecturer = All_Average_Grades([cool_lecturer,super_lecturer])

#print (cool_reviewer,cool_lecturer,
#        best_student,super_reviewer,
#        super_student,super_lecturer)

print (Versus2)
print (Versus1)
print (ALl_Grade_Student)
print (ALl_Grade_Lecturer)