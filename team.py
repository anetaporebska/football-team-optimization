class Team:
    def __init__(self, genes):
        self.genes = []
        self.genes = genes

    def get_gene(self, idx):
        return self.genes[idx]

    def set_gene(self, idx, value):
        self.genes[idx] = value

    def get_fitness_score(self):
        return self.fitness()

