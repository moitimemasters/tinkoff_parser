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


# id, user_id -> returns list of problems, solved in given contest
def parse_contest(id, user_id):
    contest = contests[id][3]
    user = contest[user_id]
    result = []
    problem_number = 0
    for i in user:
        if i["verdict"] == "OK":
            result += [(problem_number, i["time"])]
        problem_number += 1
    return result
