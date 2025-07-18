from classes.league import Player, Team, Match, Manager, League
from setup import *
from dashboard import *

season = 0
gamesPlayed = 0

def startGame():
    name = input("Whats your name? ")
    print("\n")
    for i,team in enumerate(teams, 1):
        print(f"{i}: {team}")
    
    while True:
        try:
            choice = int(input("\nWhat number team would you like to manage? "))
            if 1 <= choice <= len(teams):
                selectedTeam = teams[choice-1]
                break
            else:
                print("Enter a number within the range ")

        except ValueError:
            print("Please enter a valid number ")
    
    return Manager(name, selectedTeam)

if season == 0 and gamesPlayed == 0:
    prem = League("Premier League", teams)
    for team in teams:
        team.league = prem
    prem.generateFixtures()
    prem.assignSchedule()
    user = startGame()
    print(f"\nWelcome to {user.team.name}, {user.name}! We are really excited to have you here and cant wait for you to get started!")
    loopDashboard(user)



# gw1 = Match(teams[4],teams[10])

# Match.sim(gw1)