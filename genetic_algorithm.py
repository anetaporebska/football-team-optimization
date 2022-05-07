from random import random, randint

from team import Team


class GeneticAlgorithm:
    def __init__(self, population):
        self.population = population

    EPOCHS_NUM = 500
    MUTATION_INCREASE = 0.001

    CHILDREN_NUM = 20
    CHILDREN_INCREASE = 2

    MUTATION_RATE = 0.1
    MUTATION_CHANGE_OVER_EPOCHS = 120

    NO_IMPROVES = 80

    def crossover(self, team1, team2):
        genes = self.population.get_random_team_genes()
        new_team = Team(genes)
        idx = randint(0, 10)
        for i in range(idx):
            new_team.set_gene(i, team1.get_gene(i))
        for i in range(idx, 11):
            new_team.set_gene(i, team2.get_gene(i))
        return new_team

    def mutate(self, team_size):
        genes = []
        for i in range(team_size):
            if GeneticAlgorithm.MUTATION_RATE > random():
                player_gene = self.population.generate_player(i, use_best=True)
                genes.append(player_gene)
            else:
                player_gene = self.population.generate_player(i)
                genes.append(player_gene)

        return Team(genes)

    def generate_best_team_mutation(self):
        genes = self.population.get_random_team_genes()
        team = Team(genes)
        stable_score = 0
        best_team = team
        best_score = self.population.fitness(team)
        for i in range(self.EPOCHS_NUM):
            improve = False
            if stable_score == self.NO_IMPROVES:
                stable_score = 0
                self.MUTATION_RATE += self.MUTATION_INCREASE
                self.CHILDREN_NUM += self.CHILDREN_INCREASE
            for j in range(self.CHILDREN_NUM):
                child = self.mutate(len(team.genes))
                child_score = self.population.fitness(child)
                if child_score >= best_score:
                    best_score = child_score
                    best_team = child
                    improve = True
            if not improve:
                stable_score += 1
        return best_team

    def generate_best_team_crossover(self):
        genes = self.population.get_random_team_genes()
        team1 = Team(genes)
        genes = self.population.get_random_team_genes()
        team2 = Team(genes)
        no_improves = 0

        if self.population.fitness(team1) > self.population.fitness(team2):
            better_team = team1
            worse_team = team2
        else:
            better_team = team2
            worse_team = team1
        for i in range(self.EPOCHS_NUM):
            improve = False
            if no_improves == self.NO_IMPROVES:
                no_improves = 0
                self.CHILDREN_NUM += self.CHILDREN_INCREASE
            for j in range(self.CHILDREN_NUM):
                child = self.crossover(better_team, worse_team)
                if self.population.fitness(child) > self.population.fitness(better_team):
                    worse_team = better_team
                    better_team = child
                    improve = True
                elif self.population.fitness(child) > self.population.fitness(worse_team):
                    worse_team = child
            if not improve:
                no_improves += 1

        return better_team
