import json
from players.const.const import JSON_PATH


def lead_n_players(number):
    result = []
    with open(JSON_PATH, 'r') as json_file:
        data = json.load(json_file)
        for n, player in enumerate(data):
            if number == n:
                break
            result.append(player)
    return result


def lead_n_players_with_price(number, price):
    result = []
    with open(JSON_PATH, 'r') as json_file:
        data = json.load(json_file)
        n = 0
        for player in data:
            if number == n:
                break
            if int(player['value']) < price:
                result.append(player)
                n += 1
    return result


def lead_n_players_in_every_position(number):
    result = []
    players = {
        'gk': number,
        'rb': number,
        'cb': number * 2,
        'lb': number,
        'rm': number,
        'cm': number * 2,
        'lm': number,
        'st': number * 2
    }
    with open(JSON_PATH, 'r') as json_file:
        data = json.load(json_file)
        for n, player in enumerate(data):
            if len(players) == 0:
                break
            if player['position'] in players:
                players[player['position']] -= 1
                if players[player['position']] == 0:
                    players.pop(player['position'])
                result.append(player)
    return result


def lead_n_players_in_every_position_with_price(number, price):
    result = []
    players = {
        'gk': number,
        'rb': number,
        'cb': number * 2,
        'lb': number,
        'rm': number,
        'cm': number * 2,
        'lm': number,
        'st': number * 2
    }
    with open(JSON_PATH, 'r') as json_file:
        data = json.load(json_file)
        for n, player in enumerate(data):
            if int(player['value']) < price:
                if len(players) == 0:
                    break
                if player['position'] in players:
                    players[player['position']] -= 1
                    if players[player['position']] == 0:
                        players.pop(player['position'])
                    result.append(player)
    return result


print(lead_n_players(5))
print(lead_n_players_in_every_position_with_price(1, 50000000))
