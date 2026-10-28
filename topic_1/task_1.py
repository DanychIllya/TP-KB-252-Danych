STRING_LENGTH = 10
 
 
def reverse_string(text):

    if len(text) != STRING_LENGTH:
        raise ValueError(f"Довжина рядка має бути {STRING_LENGTH} символів, а не {len(text)}.")
 
    result = ""
    for i in range(STRING_LENGTH - 1, -1, -1):
        result += text[i]
    return result
 
 
if __name__ == "__main__":
    user_text = input(f"Введіть рядок довжиною {STRING_LENGTH} символів: ")
    try:
        print("Результат:", reverse_string(user_text))
    except ValueError as error:
        print("Помилка:", error)
 