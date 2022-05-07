import random

from genetic_algorithm import GeneticAlgorithm
from initial_population import generate_initial_populations
from population import Population

if __name__ == '__main__':
    budget = 600
    team_size = 11
    players_number = 100

    N = [[random.randint(0, 1) for _ in range(team_size)] for _ in range(team_size)]
    cost = [random.randint(0, 100) for _ in range(players_number)]
    ratings = [[random.randint(0, 10) for _ in range(team_size)] for _ in range(players_number)]
    aux = [random.randint(0, 10) for _ in range(players_number)]

    players = [{"cost": cost[i], "ratings": ratings[i], "aux": aux[i]} for i in range(players_number)]

    teams = generate_initial_populations(players, 10, budget, players_number, team_size)

    population = Population(players, teams)
    genetic_algorithm = GeneticAlgorithm(population)
    genetic_algorithm.generate_best_team_crossover()
