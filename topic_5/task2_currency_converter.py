import requests

NBU_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={code}&json"
CURRENCIES = ["EUR", "USD", "PLN"]


def get_rate(code):
    response = requests.get(NBU_URL.format(code=code), timeout=10)
    response.raise_for_status()
    data = response.json()
    return data[0]["rate"]


def request_currency():
    while True:
        code = input(f"Тип валюти ({', '.join(CURRENCIES)}): ").strip().upper()
        if code in CURRENCIES:
            return code
        print("Непідтримувана валюта.")


def request_amount():
    while True:
        try:
            amount = float(input("Кількість: ").replace(",", "."))
            if amount < 0:
                print("Кількість не може бути від'ємною.")
                continue
            return amount
        except ValueError:
            print("Потрібно ввести число.")


def main():
    code = request_currency()
    amount = request_amount()

    try:
        rate = get_rate(code)
    except requests.exceptions.RequestException as error:
        print(f"Не вдалося отримати курс від НБУ: {error}")
        return
    except (ValueError, IndexError, KeyError):
        print("НБУ повернув відповідь у неочікуваному форматі.")
        return

    result = amount * rate
    print(f"Курс НБУ: 1 {code} = {rate} UAH")
    print(f"{amount} {code} = {result:.2f} UAH")


main()
