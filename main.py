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
    budget = 600000000
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

    def avg(x):
        return sum(x) / len(x)

    for player_swaps in (1, 2):
        for position_swaps in (1, 2):
            for epochs in (200, 500, 1000):
                fitnesses = [BeesAlgorithm(
                    players,
                    N,
                    integrity_factor,
                    budget,
                    player_swaps=player_swaps,
                    position_swaps=position_swaps,
                    epochs=epochs
                ).generate_best_team()[0] for _ in range(3)]

                print("XDDDDD", ','.join(str(x) for x in (avg(fitnesses), player_swaps, position_swaps, epochs)))
