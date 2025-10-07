"""Вывод списка студентов группы с информацией о результатах экзаменов

- print_students: Вывод списка студентов группы с информацией об экзаменах.
- filter_students_by_avg: Фильтрация студентов по среднему баллу.
"""


groupmates = [
    {
        "name": "Никита",
        "surname": "Шулапов",
        "exams": ["КТП", "АиГ", "Философия"],
        "marks": [4, 5, 3]
    },
    {
        "name": "Максим",
        "surname": "Соловьев",
        "exams": ["Физика", "АиГ", "ОС"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Дмитрий",
        "surname": "Шагаров",
        "exams": ["КТП", "История", "ОС"],
        "marks": [5, 3, 5]
    },
    {
        "name": "Алексей",
        "surname": "Обласов",
        "exams": ["Физика", "История", "КТП"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Егор",
        "surname": "Алексанов",
        "exams": ["Электроника", "ИС", "Философия"],
        "marks": [4, 3, 4]
    },
    {
        "name": "Мокров",
        "surname": "Данила",
        "exams": ["СиАОД", "КТП", "АиГ"],
        "marks": [5, 3, 5]
    }
]


def print_students(students):
    print(
        u"Имя".ljust(20),
        u"Фамилия".ljust(20),
        u"Экзамены".ljust(35),
        u"Оценки".ljust(20),
        u"Средний балл".ljust(20),
    )
    for student in students:
        avg_mark = sum(student["marks"]) / len(student["marks"])
        print(
            student["name"].ljust(20),
            student["surname"].ljust(20),
            str(student["exams"]).ljust(35),
            str(student["marks"]).ljust(20),
            f"{avg_mark:.2f}".ljust(20),
        )


def filter_students(students, min_avg):
    return [
        student for student in students
        if sum(student["marks"]) / len(student["marks"]) >= min_avg
    ]


print_students(groupmates)
print("\n\n")
threshold = float(input("Минимальный ср. балл: "))
filtered = filter_students(groupmates, threshold)
print(f"\nСтуденты со ср. баллом >= {threshold}:")
print_students(filtered)
