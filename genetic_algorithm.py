from random import random, randint
import matplotlib.pyplot as plt

from team import Team


class GeneticAlgorithm:
    def __init__(self, population, budget):
        self.population = population
        self.budget = budget

    EPOCHS_NUM = 100
    POPULATION_LIMIT = 50
    MUTATION_INCREASE = 0.001

    CHILDREN_NUM = 20
    CHILDREN_INCREASE = 2

    MUTATION_ITERATIONS = 20
    MUTATION_RATE = 0.3

    CROSSOVER_ITERATIONS = 20

    NO_IMPROVES = 10

    def fitness(self, team):
        return self.population.fitness(team, self.budget)

    def get_random_genes(self):
        return self.population.get_random_team_genes()

    def calculate_team_cost(self, team):
        cost = 0
        for player_idx in team:
            cost += self.population.players[player_idx]["cost"]
        return cost

    def crossover_divide_into_two_parts(self, team1, team2):
        genes = self.get_random_genes().copy()
        new_team = Team(genes)
        team_size = team1.size
        idx = randint(0, team_size - 1)
        for i in range(idx):
            new_team.set_gene(i, team1.get_gene(i))
        for i in range(idx, team_size):
            new_team.set_gene(i, team2.get_gene(i))
        return new_team

    def crossover_pairwise_comparison(self, team1, team2):
        genes = self.get_random_genes().copy()
        new_team = Team(genes)
        team_size = team1.size
        for i in range(team_size):
            if self.population.player_fitness(team1.get_gene(i), i) > self.population.player_fitness(team2.get_gene(i), i):
                new_team.set_gene(i, team1.get_gene(i))
            else:
                new_team.set_gene(i, team2.get_gene(i))
        return new_team

    def mutate(self, genes):
        new_genes = genes.copy()
        for i in range(len(genes)):
            if GeneticAlgorithm.MUTATION_RATE < random():
                player_gene = self.population.generate_player(i)
                current_cost = self.calculate_team_cost(new_genes)
                current_gene_cost = self.population.players[i]["cost"]
                new_gene_cost = self.population.players[player_gene]["cost"]
                # warunek sprawdzający czy w wyniku mutacji nie przekroczymy budżetu
                if current_cost - current_gene_cost + new_gene_cost < self.budget:
                    new_genes[i] = player_gene

        return Team(new_genes)

    def mutate_genes_swap(self, genes):
        new_genes = genes.copy()
        idx1 = randint(0, len(new_genes) - 1)
        idx2 = randint(0, len(new_genes) - 1)
        while idx1 == idx2:
            idx2 = randint(0, len(new_genes) - 1)

        team = Team(new_genes)
        team.set_gene(idx1, genes[idx2])
        team.set_gene(idx2, genes[idx1])

        return team

    def generate_best_team_mutation(self, team):
        mutation_population = []
        stable_score = 0
        best_score = self.fitness(team)
        for i in range(self.MUTATION_ITERATIONS):
            improve = False
            if stable_score == self.NO_IMPROVES:
                stable_score = 0
                self.MUTATION_RATE += self.MUTATION_INCREASE
                self.CHILDREN_NUM += self.CHILDREN_INCREASE
            for j in range(self.CHILDREN_NUM):
                child = self.mutate_genes_swap(team.genes)
                child_score = self.fitness(child)
                if child_score >= best_score:
                    best_score = child_score
                    improve = True
                    mutation_population.append(child)  # add only children better than parent
            if not improve:
                stable_score += 1
        return mutation_population

    def generate_best_team_crossover(self, team1, team2):
        crossover_population = []
        no_improves = 0
        if self.fitness(team1) > self.fitness(team2):
            better_team = team1
            worse_team = team2
        else:
            better_team = team2
            worse_team = team1
        for i in range(self.CROSSOVER_ITERATIONS):
            improve = False
            if no_improves == self.NO_IMPROVES:
                no_improves = 0
                self.CHILDREN_NUM += self.CHILDREN_INCREASE
            for j in range(self.CHILDREN_NUM):
                child = self.crossover_pairwise_comparison(better_team, worse_team)
                if self.fitness(child) > self.fitness(better_team):
                    worse_team = better_team
                    better_team = child
                    improve = True
                    crossover_population.append(child)  # add only children better than their parents
                elif self.fitness(child) > self.fitness(worse_team):
                    worse_team = child
            if not improve:
                no_improves += 1

        return crossover_population

    def selection(self, population, previous_population):
        for genes in previous_population:
            population.append(Team(genes))
        sorted_population = sorted(population, key=lambda x: self.fitness(x), reverse=True)
        result = sorted_population if len(sorted_population) < self.POPULATION_LIMIT else sorted_population[:self.POPULATION_LIMIT]
        team_genes = []
        for team in result:
            team_genes.append(team.genes)
        return team_genes

    def generate_best_team(self):
        fitness_history = []
        for i in range(self.EPOCHS_NUM):
            epoch_population = []
            team1 = Team(self.get_random_genes())
            team2 = Team(self.get_random_genes())
            epoch_population.extend(self.generate_best_team_crossover(team1, team2))
            epoch_population.extend(self.generate_best_team_mutation(team1))
            new_population = self.selection(epoch_population, self.population.teams)
            self.population.teams = new_population
            best_fitness = self.fitness(Team(new_population[0]))
            fitness_history.append(best_fitness)
            if i % 5 == 0:
                print("GA iteration: {} fitness: {}".format(i, best_fitness))

        plt.plot(range(0, self.EPOCHS_NUM), fitness_history)
        plt.xlabel("iterations")
        plt.ylabel("fitness value")
        plt.title("Fitness")
        plt.savefig("ga_fitness.png")

        return self.population.teams[0]
