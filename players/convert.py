import csv
import json
import unidecode

from players.const import JSON_PATH, CSV_PATH


def create_json(data):
    with open(JSON_PATH, 'a') as json_file:
        json_file.write(data)


def convert_file(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        players = []
        for row in reader:
            player = {
                        'name': unidecode.unidecode(row[1]),
                        'url': row[6],
                        'position': row[14].lower(),
                        'club': unidecode.unidecode(row[15]),
                        'nationality': unidecode.unidecode(row[7]),
                        'value': row[16],
                        'rating': {
                            'gk': row[89],
                            'rb': row[88],
                            'cb': row[87],
                            'lb': row[86],
                            'rm': row[82],
                            'cm': row[81],
                            'lm': row[80],
                            'st': row[73]
                        }
                }
            players.append(player)
        create_json(json.dumps(players, indent=4, separators=(',', ': ')))


convert_file(CSV_PATH)
