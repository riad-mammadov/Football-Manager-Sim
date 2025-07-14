import random

class Player:
    def __init__(self,name,position,rating):
        self.name = name
        self.position = position
        self.rating = rating
        self.goals = 0

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
        
        average = {"home": totalRating1/len(self.team1.players), "away": totalRating2/len(self.team2.players)}

        home = average["home"]
        away = average["away"]

        homeProb = home / (home + away)       
        
        x = random.random()
        drawProb = 0.15

        if x < drawProb:
            print(f"{self.team1.name} draws against {self.team2.name}")
        elif x < drawProb + homeProb * (1 - drawProb):
            print(f"{self.team1.name} wins against {self.team2.name}")
        else:
            print(f"{self.team2.name} wins against {self.team1.name}")

        
        
    
                

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.points = 0
