from random import randint
import numpy as np


class Population:
    def __init__(self, players, teams, N, integrity_factor):
        self.players = players
        self.teams = teams
        self.N = N
        self.integrity_factor = integrity_factor

    def generate_player(self, position, use_best=False):
        players = self.players
        players_list = sorted(players, key=lambda x: x["ratings"][position], reverse=True)
        #
        player = randint(0, len(players_list) - 1)
        return player

    def get_random_team_genes(self):
        idx = randint(0, len(self.teams) - 1)
        return self.teams[idx]

    def comp(self, team, i):
        players_comp = [self.players_comp(self.players[team.genes[i]], self.players[team.genes[k]]) for k in range(len(team.genes))]
        normalization = 0
        for j in range(len(team.genes)):
            normalization += self.N[i][j]
        if normalization == 0:
            return 0
        return np.sum(np.array(self.N) @ np.array(players_comp).T) / normalization

    def players_comp(self, player1, player2):
        return 1 if player1["aux"] == player2["aux"] else 0  # TODO narodowość, liga itp

    # TODO: uzględniać aux
    def fitness(self, team, budget):
        fitness_score = 0
        cost = 0
        idx = 0
        for i in team.genes:
            fitness_score += self.players[i]["ratings"][idx] * (1 + self.integrity_factor * self.comp(team, idx))
            cost += self.players[i]["cost"]
            idx += 1
        return 0 if cost > budget or len(set(team.genes)) != 11 else fitness_score

    def player_fitness(self, player_idx, position):
        return self.players[player_idx]["ratings"][position]