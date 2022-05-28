from random import random, randint
import matplotlib.pyplot as plt

from team import Team
from population import Population


class BeesAlgorithm:
    def __init__(
        self,
        population: Population,
        budget,
        epochs=100,
        mutation_rate=0.3,
        population_size=50,
        elite_bees=5,
        good_bees=10,
        elite_size=10,
        good_size=5
    ):
        self.population = population
        self.budget = budget
        self.epochs = epochs
        self.mutation_rate = mutation_rate
        self.population_size = population_size
        self.elite_bees = elite_bees
        self.good_bees = good_bees
        self.elite_size = elite_size
        self.good_size = good_size

        assert elite_bees < good_bees
        assert elite_bees + good_bees < population_size
        assert elite_size > good_size

    def fitness(self, team: Team):
        return self.population.fitness(team, self.budget)

    def get_random_genes(self):
        return self.population.get_random_team_genes()

    def calculate_team_cost(self, team):
        return sum(self.population.players[player_idx]["cost"] for player_idx in team)

    def mutate(self, genes):
        new_genes = genes.copy()
        for i in range(len(genes)):
            if self.mutation_rate > random():
                player_gene = self.population.generate_player(i)
                current_cost = self.calculate_team_cost(new_genes)
                current_gene_cost = self.population.players[i]["cost"]
                new_gene_cost = self.population.players[player_gene]["cost"]
                # warunek sprawdzający czy w wyniku mutacji nie przekroczymy budżetu
                if current_cost - current_gene_cost + new_gene_cost < self.budget:
                    new_genes[i] = player_gene

        return Team(new_genes)

    def select_neighbour(population: Population, site_size):
        pass

    def init_populations(self):
        return [self.get_random_genes() for _ in range(self.population_size)]

    def generate_best_team(self):
        # TODO: population vs team? How do I make an artificially big population?
        # TODO: move improvements from this algorithm to generic_algorithm.py too
        fitness_history = []
        populations = self.init_populations()
        populations.sort(key=lambda pop: self.fitness(Team(pop)), reverse=True)
        for i in range(self.epochs):
            for i in range(0, self.elite_bees):
                populations[i] = self.select_neighbour(populations[i], self.elite_size)

            for i in range(self.elite_bees, self.elite_bees + self.good_bees):
                populations[i] = self.select_neighbour(populations[i], self.good_size)

            for i in range(self.elite_bees + self.good_bees, self.population_size):
                populations[i] = self.get_random_genes()

            populations.sort(key=self.fitness, reverse=True)
            best_fitness = self.fitness(populations[0])

            if i % 5 == 0:
                print(f"Bees iteration: {i} fitness: {best_fitness}")
                fitness_history.append(best_fitness)

        plt.plot(range(0, self.epochs), fitness_history)
        plt.xlabel("iterations")
        plt.ylabel("fitness value")
        plt.title("Fitness")
        plt.savefig("bees_fitness.png")

        return self.population.teams[0]
