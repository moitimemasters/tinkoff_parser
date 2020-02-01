import requests

URL = "https://algocode.ru/standings_data/69/"
data = requests.get(URL).json()

contest_data, users_data = data["contests"], data["users"]
users = {}
