import pytest

from lab_02 import (
    load_students, save_students,
    findInsertPosition, findElementPosition,
    insertStudent, deleteStudent, updateStudent, formatStudent,
    addNewElement, deleteElement, updateElement, main,
)


def make_student(name, phone="1", email="e", group="g"):
    return {"name": name, "phone": phone, "email": email, "group": group}


def make_list():
    return [make_student("Bob"), make_student("Emma"), make_student("Jon"), make_student("Zak")]


def names(students):
    return [item["name"] for item in students]


def fake_input(monkeypatch, answers):
    """Підміняє input() заздалегідь заданими відповідями."""
    iterator = iter(answers)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(iterator))


# ---------- findInsertPosition ----------

def test_find_insert_position_beginning():
    assert findInsertPosition("Anna", make_list()) == 0


def test_find_insert_position_middle():
    assert findInsertPosition("Ivan", make_list()) == 2


def test_find_insert_position_end():
    assert findInsertPosition("Zoe", make_list()) == 4


def test_find_insert_position_empty_list():
    assert findInsertPosition("Anna", []) == 0


def test_find_insert_position_ignores_case():
    assert findInsertPosition("ivan", make_list()) == 2


# ---------- findElementPosition ----------

def test_find_element_position_found():
    assert findElementPosition("Jon", make_list()) == 2


def test_find_element_position_ignores_case():
    assert findElementPosition("jon", make_list()) == 2


def test_find_element_position_not_found():
    assert findElementPosition("Nobody", make_list()) == -1


# ---------- insertStudent / deleteStudent ----------

def test_insert_student_keeps_sorted():
    students = make_list()
    position = insertStudent(students, make_student("Ivan"))
    assert position == 2
    assert names(students) == ["Bob", "Emma", "Ivan", "Jon", "Zak"]


def test_delete_student_existing():
    students = make_list()
    assert deleteStudent(students, "Emma") is True
    assert names(students) == ["Bob", "Jon", "Zak"]


def test_delete_student_missing():
    students = make_list()
    assert deleteStudent(students, "Nobody") is False
    assert len(students) == 4


# ---------- updateStudent ----------

def test_update_student_changes_phone_only():
    students = make_list()
    assert updateStudent(students, "Jon", {"phone": "999"}) is True
    jon = students[findElementPosition("Jon", students)]
    assert jon["phone"] == "999"
    assert jon["email"] == "e"


def test_update_student_empty_values_keep_old():
    students = make_list()
    updateStudent(students, "Jon", {"name": "", "phone": "", "email": "", "group": ""})
    assert students == make_list()


def test_update_student_rename_keeps_sorted():
    students = make_list()
    updateStudent(students, "Zak", {"name": "Alex"})
    assert names(students) == ["Alex", "Bob", "Emma", "Jon"]


def test_update_student_missing():
    students = make_list()
    assert updateStudent(students, "Nobody", {"phone": "1"}) is False
    assert students == make_list()


# ---------- formatStudent ----------

def test_format_student():
    text = formatStudent({"name": "Bob", "phone": "1", "email": "b@x", "group": "KB"})
    assert text == "Student name is Bob,  Phone is 1,  Email is b@x,  Group is KB"


# ---------- Робота з CSV ----------

def test_load_students_sorted_with_all_fields(tmp_path):
    file = tmp_path / "in.csv"
    file.write_text("Name,Phone,Email,Group\nZak,3,z@x,KB-2\nBob,1,b@x,KB-1\n", encoding="utf-8")
    students = load_students(str(file))
    assert students == [
        {"name": "Bob", "phone": "1", "email": "b@x", "group": "KB-1"},
        {"name": "Zak", "phone": "3", "email": "z@x", "group": "KB-2"},
    ]


def test_load_students_missing_columns_are_empty(tmp_path):
    file = tmp_path / "in.csv"
    file.write_text("Name,Phone\nBob,1112233\n", encoding="utf-8")
    assert load_students(str(file)) == [
        {"name": "Bob", "phone": "1112233", "email": "", "group": ""}
    ]


def test_load_students_header_case_insensitive(tmp_path):
    file = tmp_path / "in.csv"
    file.write_text("NAME,phone,Email,GROUP\nBob,1,b@x,KB\n", encoding="utf-8")
    assert load_students(str(file))[0]["email"] == "b@x"


def test_load_students_skips_rows_without_name(tmp_path):
    file = tmp_path / "in.csv"
    file.write_text("Name,Phone\n,111\nBob,222\n", encoding="utf-8")
    assert names(load_students(str(file))) == ["Bob"]


def test_load_students_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_students(str(tmp_path / "missing.csv"))


def test_save_students_writes_header_and_rows(tmp_path):
    file = tmp_path / "out.csv"
    save_students(str(file), [make_student("Bob", "1", "b@x", "KB")])
    lines = file.read_text(encoding="utf-8").splitlines()
    assert lines == ["Name,Phone,Email,Group", "Bob,1,b@x,KB"]


def test_save_and_load_roundtrip(tmp_path):
    file = tmp_path / "out.csv"
    students = [make_student("Bob", "1", "b@x", "KB"), make_student("Zak", "2", "z@x", "KB")]
    save_students(str(file), students)
    assert load_students(str(file)) == students


# ---------- Функції з введенням (input підміняється) ----------

def test_add_new_element(monkeypatch):
    students = make_list()
    fake_input(monkeypatch, ["Ivan", "123", "ivan@x", "KB-1"])
    addNewElement(students)
    assert names(students) == ["Bob", "Emma", "Ivan", "Jon", "Zak"]
    assert students[2] == {"name": "Ivan", "phone": "123", "email": "ivan@x", "group": "KB-1"}


def test_add_new_element_rejects_empty_name(monkeypatch):
    students = []
    fake_input(monkeypatch, ["", "   ", "Ivan", "1", "e", "g"])
    addNewElement(students)
    assert names(students) == ["Ivan"]


def test_delete_element(monkeypatch, capsys):
    students = make_list()
    fake_input(monkeypatch, ["Emma"])
    deleteElement(students)
    assert names(students) == ["Bob", "Jon", "Zak"]
    assert "deleted" in capsys.readouterr().out


def test_delete_element_not_found(monkeypatch, capsys):
    students = make_list()
    fake_input(monkeypatch, ["Nobody"])
    deleteElement(students)
    assert len(students) == 4
    assert "not found" in capsys.readouterr().out


def test_update_element(monkeypatch):
    students = make_list()
    fake_input(monkeypatch, ["Zak", "Alex", "", "new@x", ""])
    updateElement(students)
    assert names(students) == ["Alex", "Bob", "Emma", "Jon"]
    assert students[0] == {"name": "Alex", "phone": "1", "email": "new@x", "group": "g"}


def test_update_element_not_found(monkeypatch, capsys):
    students = make_list()
    fake_input(monkeypatch, ["Nobody"])
    updateElement(students)
    assert students == make_list()
    assert "not found" in capsys.readouterr().out


# ---------- main ----------

def test_main_without_arguments(capsys):
    assert main(["lab_02.py"]) == 1
    assert "Usage" in capsys.readouterr().out


def test_main_file_not_found(tmp_path, capsys):
    assert main(["lab_02.py", str(tmp_path / "missing.csv")]) == 1
    assert "File not found" in capsys.readouterr().out


def test_main_saves_before_exit(tmp_path, monkeypatch):
    file = tmp_path / "book.csv"
    file.write_text("Name,Phone,Email,Group\nZak,3,z@x,KB\nBob,1,b@x,KB\n", encoding="utf-8")
    fake_input(monkeypatch, ["C", "Anna", "2", "a@x", "KB", "D", "Zak", "X"])
    assert main(["lab_02.py", str(file)]) == 0
    assert names(load_students(str(file))) == ["Anna", "Bob"]


def test_main_saves_to_second_file(tmp_path, monkeypatch):
    source = tmp_path / "in.csv"
    target = tmp_path / "out.csv"
    source.write_text("Name,Phone,Email,Group\nBob,1,b@x,KB\n", encoding="utf-8")
    fake_input(monkeypatch, ["X"])
    main(["lab_02.py", str(source), str(target)])
    assert names(load_students(str(target))) == ["Bob"]


def test_main_wrong_choice(tmp_path, monkeypatch, capsys):
    file = tmp_path / "book.csv"
    file.write_text("Name,Phone,Email,Group\nBob,1,b@x,KB\n", encoding="utf-8")
    fake_input(monkeypatch, ["?", "X"])
    main(["lab_02.py", str(file)])
    assert "Wrong chouse" in capsys.readouterr().out
