import random


def calculate_total_cost(players, ids):
    return sum(players[i]['cost'] for i in ids)


def find_max_cost(players, ids):
    max_cost = -1
    idx = -1
    current_idx = 0
    for i in ids:
        if players[i]['cost'] > max_cost:
            max_cost = players[i]['cost']
            idx = current_idx
        current_idx += 1
    return idx


def get_population(players, ids):
    # zakładam, że kolejność graczy w liście determinuje ich pozycje na boisku
    return [players[i] for i in ids]


def generate_initial_populations(players, size, max_cost, team_size):
    initial = []
    players_number = len(players)
    for _ in range(size):
        population_ids = random.sample(range(0, players_number), team_size)
        cost = calculate_total_cost(players, population_ids)
        while cost > max_cost:
            most_expensive = find_max_cost(players, population_ids)
            possible_players = set(range(0, players_number)) - set(population_ids)
            new_idx = random.choice([*possible_players])
            population_ids[most_expensive] = new_idx
            cost = calculate_total_cost(players, population_ids)
        initial.append(population_ids)

    return initial
