def show(title, *lists):
    """Виводить назву тесту та стан списків."""
    print(f"\n--- {title} ---")
    for name, value in lists:
        print(f"{name} = {value}")


def test_append():
    numbers = [1, 2, 3]
    show("append(): до", ("numbers", numbers))
    numbers.append(4)
    show("append(4): після", ("numbers", numbers))
    assert numbers == [1, 2, 3, 4]


def test_extend():
    numbers = [1, 2, 3]
    more = [4, 5]
    show("extend(): до", ("numbers", numbers), ("more", more))
    numbers.extend(more)
    show("extend(more): після", ("numbers", numbers))
    assert numbers == [1, 2, 3, 4, 5]


def test_insert():
    numbers = [1, 2, 4]
    show("insert(): до", ("numbers", numbers))
    numbers.insert(2, 3)
    show("insert(2, 3): після", ("numbers", numbers))
    assert numbers == [1, 2, 3, 4]


def test_remove():
    numbers = [1, 2, 3, 2, 4]
    show("remove(): до", ("numbers", numbers))
    numbers.remove(2)
    show("remove(2): після", ("numbers", numbers))
    assert numbers == [1, 3, 2, 4]


def test_clear():
    numbers = [1, 2, 3]
    show("clear(): до", ("numbers", numbers))
    numbers.clear()
    show("clear(): після", ("numbers", numbers))
    assert numbers == []


def test_sort():
    numbers = [5, 2, 9, 1, 7]
    show("sort(): до", ("numbers", numbers))
    numbers.sort()
    show("sort(): після", ("numbers", numbers))
    assert numbers == [1, 2, 5, 7, 9]
    numbers.sort(reverse=True)
    show("sort(reverse=True): після", ("numbers", numbers))
    assert numbers == [9, 7, 5, 2, 1]


def test_reverse():
    numbers = [1, 2, 3, 4]
    show("reverse(): до", ("numbers", numbers))
    numbers.reverse()
    show("reverse(): після", ("numbers", numbers))
    assert numbers == [4, 3, 2, 1]


def test_copy():
    original = [1, 2, 3]
    duplicate = original.copy()
    alias = original
    original.append(4)
    show(
        "copy(): після original.append(4)",
        ("original", original),
        ("duplicate", duplicate),
        ("alias", alias),
    )
    assert duplicate == [1, 2, 3]
    assert alias == [1, 2, 3, 4]


def main():
    test_append()
    test_extend()
    test_insert()
    test_remove()
    test_clear()
    test_sort()
    test_reverse()
    test_copy()
    print("\nУсі тести методів списків пройдено.")


main()
