from classes.league import Player, Team, Match, Manager
from setup import *

season = 0
gamesPlayed = 0

# if season == 0 and gamesPlayed == 0:
#     name = input("Whats your name? ")

#     for i,team in enumerate(teams, 1):
#         print(f"{i}: {team}")
    
#     while True:
#         try:
#             choice = int(input("What number team would you like to manage? "))
#             if 1 <= choice <= len(teams):
#                 selectedTeam = teams[choice-1]
#                 break
#             else:
#                 print("Enter a number within the range ")
            
#         except ValueError:
#             print("Please enter a valid number ")


# user = Manager(name, selectedTeam)

# print(f"Welcome to {user.team.name}, {name}! We are really excited to have you here and cant wait for you to get started!")

for i, opt in enumerate(dashboard, 1):
    print(opt)


# gw1 = Match(teams[4],teams[10])

# Match.sim(gw1)