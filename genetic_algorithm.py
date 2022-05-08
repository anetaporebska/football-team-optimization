from random import random, randint

from team import Team


class GeneticAlgorithm:
    def __init__(self, population):
        self.population = population

    EPOCHS_NUM = 50
    MUTATION_INCREASE = 0.001

    CHILDREN_NUM = 20
    CHILDREN_INCREASE = 2

    MUTATION_RATE = 0.3
    MUTATION_CHANGE_OVER_EPOCHS = 120

    NO_IMPROVES = 80

    def fitness(self, team):
        return self.population.fitness(team)

    def get_random_genes(self):
        return self.population.get_random_team_genes()

    def crossover(self, team1, team2):
        genes = self.get_random_genes()
        new_team = Team(genes)
        team_size = team1.size
        idx = randint(0, team_size-1)
        for i in range(idx):
            new_team.set_gene(i, team1.get_gene(i))
        for i in range(idx, team_size):
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

#TODO: Wybierać najelpsze geny od rodziców
    def generate_best_team_mutation(self, team):
        stable_score = 0
        best_team = team
        best_score = self.fitness(team)
        for i in range(self.EPOCHS_NUM):
            improve = False
            if stable_score == self.NO_IMPROVES:
                stable_score = 0
                self.MUTATION_RATE += self.MUTATION_INCREASE
                self.CHILDREN_NUM += self.CHILDREN_INCREASE
            for j in range(self.CHILDREN_NUM):
                child = self.mutate(len(team.genes))
                child_score = self.fitness(child)
                if child_score >= best_score:
                    best_score = child_score
                    best_team = child
                    improve = True
            if not improve:
                stable_score += 1
        return best_team

    def generate_best_team_crossover(self, team1, team2):
        no_improves = 0
        if self.fitness(team1) > self.fitness(team2):
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
                if self.fitness(child) > self.fitness(better_team):
                    worse_team = better_team
                    better_team = child
                    improve = True
                elif self.fitness(child) > self.fitness(worse_team):
                    worse_team = child
            if not improve:
                no_improves += 1

        return better_team, worse_team

    def generate_best_team(self):
        genes = self.get_random_genes()
        team1 = Team(genes)
        genes = self.get_random_genes()
        team2 = Team(genes)
        for i in range(self.EPOCHS_NUM):
            child1, child2 = self.generate_best_team_crossover(team1, team2)
            team1 = self.generate_best_team_mutation(child1)
            team2 = self.generate_best_team_mutation(child2)

        return team1 if self.fitness(team1) > self.fitness(team2) else team2



