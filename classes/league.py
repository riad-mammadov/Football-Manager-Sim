import random
class Manager:
    def __init__(self,name,team,week):
        self.name = name
        self.team = team
        self.week = week
        

class League:
    def __init__(self,name,teams):
        self.name = name
        self.teams = teams
    
    def generateFixtures(self):

        num_teams = len(self.teams)
        num_rounds = (num_teams - 1) * 2
        half = num_teams // 2
        schedule = []

        team_list = self.teams[:]

        # First half of the season
        for round in range(num_teams - 1):
            matchday = []
            for i in range(half):
                team1 = team_list[i]
                team2 = team_list[-(i + 1)]
                matchday.append((team1, team2))
            schedule.append(matchday)
            team_list = [team_list[0]] + [team_list[-1]] + team_list[1:-1]

        # reverse fixtures
        second_half = [[(away, home) for (home, away) in gw] for gw in schedule]
        schedule.extend(second_half)

        return schedule
    
    def assignSchedule(self):
        full_schedule = self.generateFixtures()

        for team in self.teams:
            team.schedule = []

        # Assigns matches to teams
        for round_number, matchday in enumerate(full_schedule, start=1):
            for home_team, away_team in matchday:
                home_team.schedule.append({
                    'gameweek': round_number,
                    'homeTeam': home_team,
                    'awayTeam': away_team,
                    'home_or_away': 'Home'
                })
                away_team.schedule.append({
                    'gameweek': round_number,
                    'homeTeam': home_team,
                    'awayTeam': away_team,
                    'home_or_away': 'Away'
                })


class Player:
    def __init__(self,name,position,rating):
        self.name = name
        self.position = position
        self.rating = rating
        self.goals = 0
    def __str__(self):
        return(self.name)

# Match class with a simulate method, takes in a match instance and outputs a result based on team rating and random probability
# ensuring that games arent completely one sided
class Match:
    def __init__(self,team1,team2):
        self.team1 = team1
        self.team2 = team2

    def sim(self):
        totalRating1 = 0
        totalRating2 = 0

        for player in self.team1.players:
            totalRating1 += player.rating
        for player in self.team2.players:
            totalRating2 += player.rating
        
        # stores average player rating for teams (can to be changed with transfers)
        average = {"home": totalRating1/len(self.team1.players), "away": totalRating2/len(self.team2.players)}

        home = average["home"]
        away = average["away"]

        # Each team will get chances depending on their team strength using the gauss formula
        # chances will be around the mean mark, with a wider range of 2 for unpredictability, max 1 to prevent chances falling below 1
        homeMean, awayMean = home / 20, away / 20
        homeChances = max(1, round(random.gauss(homeMean, 2)))
        # better the team - better the goal probability, best teams capped at a 0.5 goal probability
        homeGoalProb = min(0.5, max(0.1, home / 150))
        
        awayChances = max(1, round(random.gauss(awayMean, 2)))
        awayGoalProb = min(0.5, max(0.1, away / 150))


        homeGoals, awayGoals = 0, 0

        stats = {}

        # For each home chance they have, generates a random int 0-1 and checks if their goal probability is above the int
        # The higher the goal probability, the more chance of scoring a goal
        for _ in range(homeChances):
            if random.random() < homeGoalProb:
                homeGoals += 1
                self.team1.goals += 1
                minute = random.randint(1,90)
                scorer = getScorer(self.team1.players)

                if scorer not in stats:
                    stats[scorer] = {"goals": 0, "minutes": []}

                stats[scorer]["goals"] += 1
                stats[scorer]["minutes"].append(minute)
                


        for _ in range(awayChances):
            if random.random() < awayGoalProb:
                awayGoals += 1
                self.team2.goals += 1
                scorer = getScorer(self.team2.players)
                minute = random.randint(1,90)

                if scorer not in stats:
                    stats[scorer] = {"goals": 0, "minutes": []}

                stats[scorer]["goals"] += 1
                stats[scorer]["minutes"].append(minute)
        
        goalScorers = ""
        for scorer, data in stats.items():
            name = scorer
            minutes = "' ".join(str(minute) for minute in data["minutes"])
            goalScorers += f"{name} - {minutes}' \n"
        
        
        results = [{'home': homeGoals}, {'away':awayGoals}, stats]
        return results
                  

class Team:
    def __init__(self,name, players,schedule = None, league = None,):
        self.name = name
        self.players = players
        self.schedule = schedule if schedule is not None else []
        self.league = league if league is not None else ""
        self.points = 0
        self.goals = 0        

    def __str__(self):
        return(self.name)

## Gets the goalscorer for the match
def getScorer(players):
    x = random.randint(1, len(players)-1)
    return players[x].name

