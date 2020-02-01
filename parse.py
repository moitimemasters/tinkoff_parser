import requests

URL = "https://algocode.ru/standings_data/69/"
data = requests.get(URL).json()

contest_data, users_data = data["contests"], data["users"]
users = {}
# id : short, name, group
for i in users_data:
    users[i["id"]] = [i["group_short"], i["name"], i["group"]]

contests = {}

# id : title, date, problems, users
for i in contest_data:
    contests[i["id"]] = [i["title"], i["date"], i["problems"], i["users"]]
