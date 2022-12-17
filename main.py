class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'

    def middle_grade(self):
        middle_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_middle = course_sum / len(course_grades)
            middle_sum += course_middle
        if middle_sum == 0:
            return f'Ошибка. Студент еще не получал оценки'
        else:
            return f'{middle_sum / len(self.grades.values()):.2f}'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n'
        res += f'Средняя оценка за домашние задания: {self.middle_grade()} \n'
        res += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
        res += f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, student):
        if not isinstance(student, Student):
            print(f'Такого студента нет')
            return
        return self.middle_grade() < student.middle_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rates = {}


class Lecturer(Mentor):
    def middle_rate(self):
        middle_sum = 0
        for course_grades in self.rates.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_middle = course_sum / len(course_grades)
            middle_sum += course_middle
        if middle_sum == 0:
            return f'Оценки нет'
        else:
            return f'{middle_sum / len(self.rates.values()):.2f}'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        res += f'Средняя оценка {self.middle_rate()}\n'
        return res

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print(f' Лектор не найден')
            return
        return self.middle_rate() < lecturer.middle_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return res


def grades_students(students_list, course):
    mid_sum_grades = 0
    lectors = 0
    for stud in students_list:
        if course in stud.grades.keys():
            stud_sum_grades = 0
            for grades in stud.grades[course]:
                stud_sum_grades += grades
            mid_stud_sum_grades = stud_sum_grades / len(stud.grades[course])
            mid_sum_grades += mid_stud_sum_grades
            lectors += 1
    if mid_sum_grades == 0:
        return f'Оценок нет'
    else:
        return f'{mid_sum_grades / lectors:.2f}'


def grades_lecturers(lecturer_list, course):
    mid_sum_rates = 0
    b = 0
    for lecturer in lecturer_list:
        if course in lecturer.rates.keys():
            lecturer_sum_rates = 0
            for rate in lecturer.rates[course]:
                lecturer_sum_rates += rate
            mid_lecturer_sum_rates = lecturer_sum_rates / len(lecturer.rates[course])
            mid_sum_rates += mid_lecturer_sum_rates
            b += 1
    if mid_sum_rates == 0:
        return f'Оценок  нет'
    else:
        return f'{mid_sum_rates / b:.2f}'


first_student = Student('Ivan', 'Ivanov', 'Male')
first_student.finished_courses = ['Основы программирования', 'Тайм-менеджмент']
first_student.courses_in_progress = ['Git']

second_student = Student('Petr', 'Petrov', 'Male')
second_student.finished_courses = ['Тайм-менеджмент', 'Git']
second_student.courses_in_progress = ['Python', 'Java']
students_list = [first_student, second_student]

first_lecturer = Lecturer('Sasha', 'Semenov')
first_lecturer.courses_attached = ['Git', 'Java']

second_lecturer = Lecturer('Alex', 'Petrov')
second_lecturer.courses_attached = ['Python']
lecturer_list = [first_lecturer, second_lecturer]

first_reviewer = Reviewer('Kris', 'Semenova')
first_reviewer.courses_attached = ['Тайм-менеджмент', 'Основы программирования', 'Java', 'Git']

second_reviewer = Reviewer('Anna', 'Petrovna')
second_reviewer.courses_attached = ['Git', 'Python', 'Основы программирования']

first_reviewer.rate_hw(first_student, 'Git', 9)
first_reviewer.rate_hw(first_student, 'Git', 7)
first_reviewer.rate_hw(first_student, 'Git', 10)
first_reviewer.rate_hw(first_student, 'Java', 5)
first_reviewer.rate_hw(first_student, 'Java', 8)
first_reviewer.rate_hw(first_student, 'Java', 9)
first_reviewer.rate_hw(first_student, 'Основы программирования', 9)
first_reviewer.rate_hw(first_student, 'Основы программирования', 9)
first_reviewer.rate_hw(first_student, 'Основы программирования', 9)
first_reviewer.rate_hw(first_student, 'Тайм-менеджмент', 10)
first_reviewer.rate_hw(first_student, 'Тайм-менеджмент', 9)
first_reviewer.rate_hw(first_student, 'Тайм-менеджмент', 4)

second_reviewer.rate_hw(second_student, 'Тайм-менеджмент', 7)
second_reviewer.rate_hw(second_student, 'Тайм-менеджмент', 5)
second_reviewer.rate_hw(second_student, 'Тайм-менеджмент', 1)
second_reviewer.rate_hw(second_student, 'Git', 8)
second_reviewer.rate_hw(second_student, 'Git', 1)
second_reviewer.rate_hw(second_student, 'Git', 7)
second_reviewer.rate_hw(second_student, 'Python', 8)
second_reviewer.rate_hw(second_student, 'Python', 10)
second_reviewer.rate_hw(second_student, 'Python', 5)
second_reviewer.rate_hw(second_student, 'Java', 7)
second_reviewer.rate_hw(second_student, 'Java', 4)
second_reviewer.rate_hw(second_student, 'Java', 10)

first_student.rate_lecturer(first_lecturer, 'Git', 10)
first_student.rate_lecturer(first_lecturer, 'Git', 5)
first_student.rate_lecturer(first_lecturer, 'Git', 9)
first_student.rate_lecturer(first_lecturer, 'Java', 6)
first_student.rate_lecturer(first_lecturer, 'Java', 7)
first_student.rate_lecturer(first_lecturer, 'Java', 8)

second_student.rate_lecturer(first_lecturer, 'Java', 10)
second_student.rate_lecturer(first_lecturer, 'Java', 9)
second_student.rate_lecturer(first_lecturer, 'Java', 10)
second_student.rate_lecturer(second_lecturer, 'Python', 10)
second_student.rate_lecturer(second_lecturer, 'Python', 2)
second_student.rate_lecturer(second_lecturer, 'Python', 8)

print(first_student)
print(second_student)

if first_student > second_student:
    print(f'{first_student.name} учится лучше {second_student.name}')
else:
    print(f'{second_student.name} учится лучше {first_student.name}')

print(first_reviewer)
print(second_reviewer)

print(first_lecturer)
print(second_lecturer)

if first_lecturer > second_lecturer:
    print(f'{first_lecturer.name} преподает лучше {second_lecturer.name}')
else:
    print(f'{second_lecturer.name} преподает лучше {first_lecturer.name}')

print(f'Средняя оценка студентов по курсу "Git": {grades_students(students_list, "Git")}')
print(f'Средняя оценка студентов по курсу "Java": {grades_students(students_list, "Java")}')
print(f'Средняя оценка студентов по курсу "Python": {grades_students(students_list, "Python")}')

print(f'Средняя оценка лекторов по курсу "Git": {grades_lecturers(lecturer_list, "Git")}')
print(f'Средняя оценка лекторов по курсу "Java": {grades_lecturers(lecturer_list, "Java")}')
print(f'Средняя оценка лекторов по курсу "Python": {grades_lecturers(lecturer_list, "Python")}')
