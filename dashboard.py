
dashboard = ["View Squad", "View Fixtures", "League Table", "Play Next Game", "Save & Exit"]

def loopDashboard(user):
    while True:
        choice = getDashboard(user)
        if choice == 5:
            break

def getDashboard(user):
    print("\n")
    for i, opt in enumerate(dashboard, 1):
        print(f"{i}: {opt}")
    try:
        choice = int(input())
        if 1 <= choice <= len(dashboard):
            if choice == 1:
                viewSquad(user)
            elif choice == 2:
                viewFixtures(user.team)
            elif choice == 3:
                leagueTable(user.team.league)
            elif choice == 4:
                playNext(user)
            elif choice == 5:
                return handleQuit()
            return "continue"
        else:
            print("Enter a number within the range ")
            return "continue"
    except ValueError:
        print("Please enter a valid number ")
        return "continue"

def viewSquad(user):
    print(f"\n{user.team.name}'s Squad \n")
    for player in user.team.players:
        print(f"{player.position} - {player.name}")

def viewFixtures(team):
    print(f"{team.name}'s Fixtures \n")
    for fixture in team.schedule:
        print(f"Gameweek: {fixture['gameweek']}")
        print(f"{fixture['homeTeam'].name} vs {fixture['awayTeam'].name}\n")

def leagueTable(league):
    print(f"\n{league.name} Table\n")
    
    sorted_teams = sorted(league.teams, key=lambda t: t.points, reverse=True)
    
    for idx, team in enumerate(sorted_teams, 1):
        print(f"{idx}. {team.name} - {team.points} pts")
        

def playNext():
    print

def handleQuit():
    pass