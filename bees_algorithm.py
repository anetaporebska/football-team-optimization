from random import random, randint
import matplotlib.pyplot as plt

from team import Team
from population import Population
from initial_population import generate_initial_populations


class BeesAlgorithm:
    def __init__(
        self,
        players,
        N,
        integrity_factor,
        budget,
        epochs=100,
        mutation_rate=0.3,
        population_size=50,
        elite_bees=5,
        good_bees=10,
        elite_size=10,
        good_size=5
    ):
        assert elite_bees < good_bees
        assert elite_bees + good_bees < population_size
        assert elite_size > good_size

        self.players = players
        self.N = N
        self.integrity_factor = integrity_factor
        self.budget = budget
        self.epochs = epochs
        self.mutation_rate = mutation_rate
        self.population_size = population_size
        self.elite_bees = elite_bees
        self.good_bees = good_bees
        self.elite_size = elite_size
        self.good_size = good_size

        initial_teams = generate_initial_populations(players, population_size, budget, len(N))
        self.population = Population(players, initial_teams, N, integrity_factor)

    def fitness(self, team: Team):
        return self.population.fitness(team, self.budget)

    def pick_random_team(self):
        return generate_initial_populations(self.players, 1, self.budget, len(self.N))[0]

    def calculate_team_cost(self, team):
        return sum(self.population.players[player_idx]["cost"] for player_idx in team)

    def search_neighborhood(self, team, site_size):
        return team

    def sort_population(self):
        self.population.teams.sort(key=lambda team: self.fitness(Team(team)), reverse=True)

    def generate_best_team(self):
        fitness_history = []

        self.sort_population()

        for i in range(self.epochs):
            for bee in range(0, self.elite_bees):
                self.population.teams[bee] = self.search_neighborhood(self.population.teams[bee], self.elite_size)

            for bee in range(self.elite_bees, self.elite_bees + self.good_bees):
                self.population.teams[bee] = self.search_neighborhood(self.population.teams[bee], self.good_size)

            for bee in range(self.elite_bees + self.good_bees, self.population_size):
                self.population.teams[bee] = self.pick_random_team()

            self.sort_population()
            best_fitness = self.fitness(Team(self.population.teams[0]))
            fitness_history.append(best_fitness)

            if i % 5 == 0:
                print(f"Bees iteration: {i} fitness: {best_fitness}")

        plt.plot(range(0, self.epochs), fitness_history)
        plt.xlabel("iterations")
        plt.ylabel("fitness value")
        plt.title("Fitness")
        plt.savefig("bees_fitness.png")

        return self.population.teams[0]
