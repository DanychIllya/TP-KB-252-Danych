import random

CHOICES = ["stone", "scissor", "paper"]

WINS_AGAINST = {
    "stone": "scissor",
    "scissor": "paper",
    "paper": "stone",
}


def request_user_choice():
    while True:
        choice = input("Ваш вибір (stone, scissor, paper): ").strip().lower()
        if choice in CHOICES:
            return choice
        print("Некоректне значення. Введіть stone, scissor або paper.")


def determine_winner(user, computer):
    if user == computer:
        return "draw"
    if WINS_AGAINST[user] == computer:
        return "user"
    return "computer"


def main():
    user = request_user_choice()
    computer = random.choice(CHOICES)

    print(f"Ви обрали: {user}")
    print(f"Комп'ютер обрав: {computer}")

    winner = determine_winner(user, computer)
    if winner == "draw":
        print("Нічия!")
    elif winner == "user":
        print("Ви перемогли!")
    else:
        print("Комп'ютер переміг.")


main()
