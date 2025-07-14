import random

class Player:
    def __init__(self,name,position,rating):
        self.name = name
        self.position = position
        self.rating = rating
        self.goals = 0

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

        homeProb = home / (home + away)       
        awayProb = away / (away + home)

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
        for _ in range(homeChances):
            if random.random() < homeGoalProb:
                homeGoals += 1
                scorer = getScorer(self.team1.players)
                stats[scorer] = stats.get(scorer, 0) + 1
                print(f"The goalscorers for the home team were: {list(stats.keys())}")

        print(f"{self.team1.name} : {homeChances}, {self.team2.name} : {awayChances}")
        
        
    
                

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.points = 0
        self.goals = 0

def getScorer(players):
    ## gets a player in team that scored exluding goalkeepers (first entry)
    x = random.randint(1, len(players)-1)
    return players[x].name
