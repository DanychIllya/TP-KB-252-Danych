students = [
    {"name": "Олена", "grade": 88},
    {"name": "Андрій", "grade": 95},
    {"name": "Максим", "grade": 72},
    {"name": "Софія", "grade": 95},
    {"name": "Богдан", "grade": 60},
]


def show(title, data):
    print(f"\n{title}")
    for item in data:
        print(f"  {item['name']:<8} {item['grade']}")


def main():
    show("Початковий (не відсортований) список:", students)

    by_name = sorted(students, key=lambda item: item["name"])
    show("Сортування за іменем (за зростанням):", by_name)

    by_grade = sorted(students, key=lambda item: item["grade"])
    show("Сортування за оцінкою (за зростанням):", by_grade)

    by_grade_desc = sorted(students, key=lambda item: item["grade"], reverse=True)
    show("Сортування за оцінкою (за спаданням):", by_grade_desc)

    assert students[0]["name"] == "Олена"
    assert [s["name"] for s in by_name] == ["Андрій", "Богдан", "Максим", "Олена", "Софія"]
    assert [s["grade"] for s in by_grade] == [60, 72, 88, 95, 95]


main()
