def demo_value_error():
    return int("abc")


def demo_type_error():
    return "5" + 5


def demo_zero_division_error():
    return 10 / 0


def demo_index_error():
    numbers = [1, 2, 3]
    return numbers[10]


def demo_key_error():
    student = {"name": "Іван"}
    return student["age"]


def demo_name_error():
    return undefined_variable


def demo_attribute_error():
    return "text".append("a")


def demo_file_not_found_error():
    with open("file_that_does_not_exist.txt") as file:
        return file.read()


def demo_overflow_error():
    return 2.0 ** 10000


DEMOS = [
    demo_value_error,
    demo_type_error,
    demo_zero_division_error,
    demo_index_error,
    demo_key_error,
    demo_name_error,
    demo_attribute_error,
    demo_file_not_found_error,
    demo_overflow_error,
]


def main():
    for demo in DEMOS:
        try:
            demo()
        except Exception as error:
            print(f"{type(error).__name__:22} -> {error}")

main()