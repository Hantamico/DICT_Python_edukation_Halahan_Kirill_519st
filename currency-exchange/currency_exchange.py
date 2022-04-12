import requests
import json
from functools import lru_cache


def get_rate(code):
    print("Searching...")
    res = requests.get(f"http://www.floatrates.com/daily/{code}.json")
    if res.ok:
        result = res.json()
        d = result.get("usd").get("rate")
        e = result.get("eur").get("rate")
        return round(d, 2), round(e, 2)
    else:
        return


def step_3():
    code = input("> ").lower()
    results = get_rate(code)
    if not results:
        print(f'No results found for "{code}"')
        step_3()
        return

    dollar, euro = results
    print(f"""Dollar: {round(dollar, 2)}
Euro: {round(euro, 2)}""")
    step_3()


def correct_float_input(string):
    user_input = input(string)
    while True:
        try:
            float(user_input)
        except ValueError:
            if "," in user_input:
                user_input = user_input.replace(",", ".")
                continue
            print("Incorrect format")
            user_input = input(string)
            continue
        else:
            break
    return float(user_input)


step_3()


# coin = float(input("Please, enter the number of mycoins you have: >"))
# print("I will get", coin * 0.82, "ARS from the sale of", coin, "mycoins")
# print("I will get", coin * 0.17, "HNL from the sale of", coin, "mycoins")
# print("I will get", coin * 1.96, "AUD from the sale of", coin, "mycoins")
# print("I will get", coin * 0.208, "MAD from the sale of", coin, "mycoins")
