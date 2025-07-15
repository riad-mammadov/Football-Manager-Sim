from classes.league import *

import json

with open("teams.json", "r") as file:
    team_data = json.load(file)

teams = []
for t in team_data:
    players = [Player(p["name"], p["position"], p["rating"]) for p in t["players"]]
    team = Team(t["name"], players)
    teams.append(team)




