class Team:
    def __init__(self, genes, size=11):
        self.genes = genes
        self.size = size

    def get_gene(self, idx):
        return self.genes[idx]

    def set_gene(self, idx, value):
        self.genes[idx] = value
