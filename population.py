from random import random


class Population:
    def __init__(self, players, teams):
        self.players = players
        self.teams = teams

    def generate_player(self, position, use_best=False):
        players = self.players
        players_list = sorted(players, key=lambda x: x["ratings"][position], reverse=True)
        if use_best:
            player = players.index(players_list[0])
        else:
            player = get_random(len(players_list))
        return player

    def get_random_team_genes(self):
        idx = get_random(len(self.teams))
        return self.teams[idx]

    def fitness(self, team):
        fitness_score = 0
        idx = 0
        for i in team.genes:
            fitness_score += self.players[i]["ratings"][idx]
            idx += 1
        return fitness_score


"""
Ma jakis problem o randinta,
Na razie zostawie tak, żeby tylko zobaczyć czy działa 
"""
def get_random(n):
    return int(random()*n)

