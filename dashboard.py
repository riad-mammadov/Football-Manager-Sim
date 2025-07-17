
dashboard = ["View Squad", "View Fixtures", "League Table", "Play Next Game", "Save & Exit"]

def getDashboard(user):
    for i, opt in enumerate(dashboard, 1):
        print(f"{i}: {opt}")

    while True:
        try:
            choice = int(input())
            if 1 <= choice <= len(dashboard):
                if choice == 1:
                    return viewSquad(user)
                elif choice == 2:
                    return viewFixtures(user.team)
                elif choice == 3:
                    return playNext(user)
                elif choice == 4:
                    return handleQuit
            else:
                print("Enter a number within the range ")
        except ValueError:
            print("Please enter a valid number ")

def viewSquad(user):
    print(f"{user.team.name}'s Squad \n\n")
    for player in user.team.players:
        print(f"{player.position} - {player.name}")

def viewFixtures(team):
    print(f"{team.name}'s Fixtures \n")
    for fixture in team.schedule:
        print(f"Gameweek: {fixture['gameweek']}")
        print(f"{fixture['homeTeam'].name} vs {fixture['awayTeam'].name}\n")

def playNext():
    pass

def handleQuit():
    pass