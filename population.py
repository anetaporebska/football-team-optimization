from random import randint


class Population:
    def __init__(self, players, teams):
        self.players = players
        self.teams = teams

# TODO: dla use_best uwzględniać aux
    def generate_player(self, position, use_best=False):
        players = self.players
        players_list = sorted(players, key=lambda x: x["ratings"][position], reverse=True)
        if use_best:
            player = players.index(players_list[0])
        else:
            player = randint(0, len(players_list) - 1)
        return player

    def get_random_team_genes(self):
        idx = randint(0, len(self.teams)-1)
        return self.teams[idx]

# TODO: uzględniać aux, liczyć koszta itp
    def fitness(self, team):
        fitness_score = 0
        idx = 0
        for i in team.genes:
            fitness_score += self.players[i]["ratings"][idx]
            idx += 1
        return fitness_score
