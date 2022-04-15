import random


def calculate_total_cost(players, ids):
    cost = 0
    for i in ids:
        cost += players[i]['cost']
    return cost


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
    population = []
    for i in ids:
        population.append(players[i])
    return population


def generate_initial_populations(players, size, max_cost, players_number, team_size):
    initial = []
    for _ in range(size):
        population_ids = random.sample(range(0, players_number), team_size)
        cost = calculate_total_cost(players, population_ids)
        while cost > max_cost:
            most_expensive = find_max_cost(players, population_ids)
            possible_players = set(range(0, players_number)) - set(population_ids)
            new_idx = random.choice([*possible_players])
            population_ids[most_expensive] = new_idx
            cost = calculate_total_cost(players, population_ids)
        initial.append(get_population(players, population_ids))

    return initial
