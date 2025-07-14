from model import Player, Team, Match

man_utd_players = [
    Player("Andre Onana", "Goalkeeper", 82),
    Player("Harry Maguire", "Defender", 80),
    Player("Bruno Fernandes", "Midfielder", 88),
    Player("Marcus Rashford", "Forward", 85),
    # add more players as needed
]

# Arsenal players
arsenal_players = [
    Player("David Raya", "Goalkeeper", 83),
    Player("Gabriel Magalhaes", "Defender", 82),
    Player("Martin Odegaard", "Midfielder", 84),
    Player("Bukayo Saka", "Forward", 86),
    # add more players as needed
]

united = Team('Manchester United', man_utd_players)
arsenal =Team('Arsenal', arsenal_players)

gw1 = Match(united,arsenal)

Match.sim(gw1)