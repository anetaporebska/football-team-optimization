import random

from genetic_algorithm import GeneticAlgorithm
from initial_population import generate_initial_populations
from population import Population

if __name__ == '__main__':
    budget = 600
    team_size = 11
    players_number = 500
    max_cost = 100
    integrity_factor = 0.7

    N = [[random.randint(0, 1) for _ in range(team_size)] for _ in range(team_size)]
    cost = [random.randint(0, max_cost) for _ in range(players_number)]
    ratings = [[random.randint(0, 10) * cost[x] / max_cost for _ in range(team_size)] for x in range(players_number)]
    aux = [random.randint(0, 10) for _ in range(players_number)]

    players = [{"cost": cost[i], "ratings": ratings[i], "aux": aux[i]} for i in range(players_number)]

    teams = generate_initial_populations(players, 10, budget, team_size)

    population = Population(players, teams, N, integrity_factor)
    genetic_algorithm = GeneticAlgorithm(population, budget)
    result = genetic_algorithm.generate_best_team()
    print(result)
