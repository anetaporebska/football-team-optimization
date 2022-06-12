import math
from random import randint
from players.const.const import *
import numpy as np

from players.create_team import chemistry_score


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
        players_comp = [self.players_comp(self.players[team.genes[i]], self.players[team.genes[k]]) for k in
                        range(len(team.genes))]
        normalization = 0
        for j in range(len(team.genes)):
            normalization += self.N[i][j]
        if normalization == 0:
            return 0
        return np.sum(np.array(self.N) @ np.array(players_comp).T) / normalization

    def players_comp(self, player1, player2):
        compatible_attrs = [attr1 == attr2 for attr1, attr2 in zip(player1["aux"], player2["aux"])]
        return sum(compatible_attrs) / len(compatible_attrs)

    # TODO: uzględniać aux

    def fitness(self, team, budget):
        cost = 0
        rating = 0
        result = {}
        for i, idx in enumerate(team.genes):
            result[PLAYER_POSITION[i]] = self.players[idx]
            rating += int(self.players[idx]["ratings"][i])
            cost += self.players[idx]["cost"]
        fitness_chemistry = chemistry_score(result)
        fitness_chemistry = MAX_CHEMISTRY if fitness_chemistry > MAX_CHEMISTRY else fitness_chemistry
        fitness_score = math.ceil(rating / NUMBER_OF_PLAYER_IN_PITCH) + fitness_chemistry

        return 0 if cost > budget or len(set(team.genes)) != 11 else fitness_score

    def player_fitness(self, player_idx, position):
        return self.players[player_idx]["ratings"][position]
