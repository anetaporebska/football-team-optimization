import random

if __name__ == '__main__':

    budget = 600
    team_size = 11
    players_number = 100

    N = [[random.randint(0, 1) for _ in range(team_size)] for _ in range(team_size)]
    cost = [random.randint(0, 100) for _ in range(players_number)]
    ratings = [[random.randint(0, 10) for _ in range(team_size)] for _ in range(players_number)]
    aux = [random.randint(0, 10) for _ in range(players_number)]

    players = [dict()] * players_number
    for i in range(players_number):
        players[i] = {
            "cost": cost[i],
            "ratings": ratings[i],
            "aux": aux[i]
        }
