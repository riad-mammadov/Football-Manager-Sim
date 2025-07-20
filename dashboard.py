from classes.league import Match
import time
import sys
dashboard = ["View Squad", "View Fixtures", "League Table", "Play Next Game", "Save & Exit"]

def loopDashboard(user):
    # Keeps dashboard active until quit option is selected
    while True:
        choice = getDashboard(user)
        if choice == 5:
            break

def getDashboard(user):
    # Main dashboard 
    print(f"\nGameweek {user.week}\n")
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
                sys.exit()
            return "continue"
        else:
            print("Enter a number within the range ")
            return "continue"
    except ValueError:
        print("Please enter a valid number ")
        return "continue"

def viewSquad(user):
    # View player squad
    print(f"\n{user.team.name}'s Squad \n")
    for player in user.team.players:
        print(f"{player.position} - {player.name}")

def viewFixtures(team):
    # Get league fixtures
    print(f"{team.name}'s Fixtures \n")
    for fixture in team.schedule:
        print(f"Gameweek: {fixture['gameweek']}")
        print(f"{fixture['homeTeam'].name} vs {fixture['awayTeam'].name}\n")

def leagueTable(league):
    # get league table sorted in desc order
    print(f"\n{league.name} Table\n")
    sorted_teams = sorted(league.teams, key=lambda t: t.points, reverse=True)
    for idx, team in enumerate(sorted_teams, 1):
        print(f"{idx}. {team.name} - {team.points} pts")
        

def playNext(user):
    # Gets fixture for current gameweek (per game = +1 to gameweek)
    gameweek = user.week
    schedule = user.team.schedule
    currGames = [fixture for fixture in schedule if fixture['gameweek'] == gameweek]

    for fixture in currGames:
        print(f"\n{fixture['homeTeam'].name} vs {fixture['awayTeam'].name} ({fixture['home_or_away']}) \n")
    
    # create a match object 'game' to simulate the game
    game = Match(fixture['homeTeam'], fixture['awayTeam'])

    # Get opposiiton team 
    if fixture['homeTeam'] == user.team.name:
        oppTeam = fixture['awayTeam']
    else:
        oppTeam = fixture['homeTeam']

   
    ## Sim managers game + all other games behind the scenes
    print("Simulating Match...")
    time.sleep(3)
    gameResult = game.sim()
    simRestOfGames(user, oppTeam)


    # Track game result / stats
    homeGoals = gameResult[0]['home']
    awayGoals = gameResult[1]['away']

    if homeGoals > awayGoals:
        fixture['homeTeam'].points += 3
    elif awayGoals > homeGoals:
        fixture['awayTeam'].points += 3
    else:
        fixture['awayTeam'].points += 1
        fixture['homeTeam'].points += 1

    # Combine both teams players to avoid redundant loops
    allPlayers = user.team.players + oppTeam.players

    goalScorers = ""
    # Update goal stat for each player object
    for playerName, stats in gameResult[2].items():
        name = playerName
        minutes = "' ".join(str(minute) for minute in stats["minutes"])
        goalScorers += f"{name} - {minutes}' \n"
        for player in allPlayers:
            if player.name == playerName:
                player.goals += stats['goals']
                break

    finalScore = f"{fixture['homeTeam'].name} {homeGoals} - {fixture['awayTeam'].name} {awayGoals}"
    print(finalScore + "\n")
    print(goalScorers)

def simRestOfGames(user, opponent):
    gameweek = user.week
    seen_fixtures = set()
    simulated_fixtures = []

    # gets the rest of the team fixtures
    for team in user.team.league.teams:
        # Skip user and opponent teams
        if team.name in [user.team.name, opponent.name]:
            continue

        for fixture in team.schedule:
            if fixture["gameweek"] != gameweek:
                continue

            # Convert to tuple as dicts arent hashable 
            teams_tuple = tuple(sorted([
                fixture["homeTeam"].name,
                fixture["awayTeam"].name
            ]))

            # track processed fixtures to avoid duplicate fixtures 
            if teams_tuple not in seen_fixtures:
                simulated_fixtures.append(fixture)
                seen_fixtures.add(teams_tuple)

            break

    for fixture in simulated_fixtures:
        game = Match(fixture["homeTeam"], fixture["awayTeam"])
        gameResult = game.sim()

         # Track game result / stats
        homeGoals = gameResult[0]['home']
        awayGoals = gameResult[1]['away']

        if homeGoals > awayGoals:
            fixture['homeTeam'].points += 3
        elif awayGoals > homeGoals:
            fixture['awayTeam'].points += 3
        else:
            fixture['awayTeam'].points += 1
            fixture['homeTeam'].points += 1
        
        allPlayers = fixture["homeTeam"].players + fixture["awayTeam"].players

        for playerName, stats in gameResult[2].items():
            for player in allPlayers:
                if player.name == playerName:
                    player.goals += stats['goals']
                    break

    user.week += 1

    