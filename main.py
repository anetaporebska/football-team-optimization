#!/usr/bin/env python3

import sys

from bees_algorithm import BeesAlgorithm
from genetic_algorithm import GeneticAlgorithm
from initial_population import generate_initial_populations
from players.const.const import PLAYER_POSITION
from players.create_team import create_team
from players.lead_player import lead_n_players
from population import Population


def get_ratings_arr(player):
    ratings = []
    player_rating = player['rating']
    for i in player_rating:
        if i in ['cb', 'cm', 'st']:
            ratings.append(int(player_rating[i]))
        ratings.append(int(player_rating[i]))

    return ratings


if __name__ == '__main__':
    budget = 1200000000
    team_size = 11
    players_number = 5000
    integrity_factor = 0.5

    loaded_players = lead_n_players(players_number)

    # gk, rb, cbl, cbr, lb, rm, cml, cmr, lm, stl, str
    N = [
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    ]

    players = [
        {
            "cost": int(loaded_players[i]['value']),
            "ratings": get_ratings_arr(loaded_players[i]),
            "aux": [loaded_players[i]['club'], loaded_players[i]['nationality']]
        }
        for i in range(players_number)
    ]

    if len(sys.argv) > 1 and sys.argv[1] == "bees":
        algorithm = BeesAlgorithm(players, N, integrity_factor, budget)
    else:
        teams = generate_initial_populations(players, 10, budget, team_size)
        population = Population(players, teams, N, integrity_factor)

        algorithm = GeneticAlgorithm(population, budget)

    result_indexes = algorithm.generate_best_team()

    result = {}
    for i, idx in enumerate(result_indexes):
        result[PLAYER_POSITION[i]] = loaded_players[idx]

    print(result)
    create_team(result)
