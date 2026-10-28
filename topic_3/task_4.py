from bisect import bisect_left


def find_insert_position(sorted_list, value):
    """Повертає індекс, на який потрібно вставити value,
    щоб список залишився відсортованим за зростанням.
    Якщо такі значення вже є, повертається позиція перед ними."""
    left = 0
    right = len(sorted_list)

    while left < right:
        middle = (left + right) // 2
        if sorted_list[middle] < value:
            left = middle + 1
        else:
            right = middle

    return left

def main():
    numbers = [1, 3, 5, 7, 9]
    print("Відсортований список:", numbers)

    tests = [0, 1, 4, 7, 8, 10]
    for value in tests:
        position = find_insert_position(numbers, value)
        assert position == bisect_left(numbers, value)
        result = numbers.copy()
        result.insert(position, value)
        print(f"Значення {value}: позиція {position}, список після вставки {result}")

    assert find_insert_position([], 5) == 0
    assert find_insert_position([2, 2, 2], 2) == 0
    assert find_insert_position([2, 2, 2], 3) == 3
    print("Усі перевірки пройдено.")

main()
