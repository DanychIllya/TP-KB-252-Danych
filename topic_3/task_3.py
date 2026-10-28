def show(title, data):
    print(f"{title}: {data}")


def test_update():
    student = {"name": "Іван", "age": 19}
    show("update(): до", student)
    student.update({"age": 20, "group": "ІП-21"})
    show("update(): після", student)
    assert student == {"name": "Іван", "age": 20, "group": "ІП-21"}


def test_del():
    student = {"name": "Іван", "age": 19, "group": "ІП-21"}
    show("del: до", student)
    del student["group"]
    show("del student['group']: після", student)
    assert "group" not in student


def test_clear():
    student = {"name": "Іван", "age": 19}
    show("clear(): до", student)
    student.clear()
    show("clear(): після", student)
    assert student == {}


def test_keys():
    student = {"name": "Іван", "age": 19}
    keys = student.keys()
    show("keys()", keys)
    assert list(keys) == ["name", "age"]


def test_values():
    student = {"name": "Іван", "age": 19}
    values = student.values()
    show("values()", values)
    assert list(values) == ["Іван", 19]


def test_items():
    student = {"name": "Іван", "age": 19}
    items = student.items()
    show("items()", items)
    for key, value in items:
        print(f"  {key} -> {value}")
    assert list(items) == [("name", "Іван"), ("age", 19)]


def main():
    test_update()
    test_del()
    test_clear()
    test_keys()
    test_values()
    test_items()
    print("Усі тести методів словників пройдено.")


main()
