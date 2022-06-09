import math
from PIL import Image
from PIL import ImageDraw

from players.const import CONNECTION, PITCH_PATH, PLAYER_CARD, CARD_SIZE, SCORE_FONT, FONT_COLOR, PLAYER_FONT
from players.create_player_card import create_player

players_ = {'gk': {'name': 'S. Handanovic', 'url': 'https://cdn.sofifa.com/players/162/835/22_60.png', 'position': 'gk',
                   'club': 'Everton', 'nationality': 'Slovenia', 'value': '7500000',
                   'rating': {'gk': '86', 'rb': '32', 'cb': '32', 'lb': '32', 'rm': '34', 'cm': '37', 'lm': '34',
                              'st': '33'}},
            'cbl': {'name': 'Thiago Silva', 'url': 'https://cdn.sofifa.com/players/164/240/22_60.png', 'position': 'cb',
                    'club': 'Everton', 'nationality': 'Brazil', 'value': '9500000',
                    'rating': {'gk': '21', 'rb': '80', 'cb': '85', 'lb': '80', 'rm': '70', 'cm': '78', 'lm': '70',
                               'st': '68'}},
            'cbr':
                {'name': 'T. Alderweireld', 'url': 'https://cdn.sofifa.com/players/184/087/22_60.png', 'position': 'cb',
                 'club': 'Everton', 'nationality': 'Belgium', 'value': '0',
                 'rating': {'gk': '24', 'rb': '81', 'cb': '83', 'lb': '81', 'rm': '69', 'cm': '76', 'lm': '69',
                            'st': '68'}},

            'cml': {'name': 'Joao Moutinho', 'url': 'https://cdn.sofifa.com/players/162/347/22_60.png',
                    'position': 'cm',
                    'club': 'Everton', 'nationality': 'Portugal', 'value': '9500000',
                    'rating': {'gk': '23', 'rb': '75', 'cb': '73', 'lb': '75', 'rm': '78', 'cm': '80', 'lm': '78',
                               'st': '74'}},
            'lb': {'name': 'Nacho Monreal', 'url': 'https://cdn.sofifa.com/players/177/604/22_60.png', 'position': 'lb',
                   'club': 'Everton', 'nationality': 'Spain', 'value': '6500000',
                   'rating': {'gk': '16', 'rb': '79', 'cb': '79', 'lb': '79', 'rm': '74', 'cm': '76', 'lm': '74',
                              'st': '71'}},
            'stl': {'name': 'Y. El Arabi', 'url': 'https://cdn.sofifa.com/players/194/209/22_60.png', 'position': 'st',
                    'club': 'Everton', 'nationality': 'Morocco', 'value': '8500000',
                    'rating': {'gk': '19', 'rb': '58', 'cb': '54', 'lb': '58', 'rm': '77', 'cm': '73', 'lm': '77',
                               'st': '79'}},
            'str': {'name': 'O. Giroud', 'url': 'https://cdn.sofifa.com/players/178/509/22_60.png', 'position': 'st',
                    'club': 'Everton', 'nationality': 'France', 'value': '8500000',
                    'rating': {'gk': '20', 'rb': '54', 'cb': '59', 'lb': '54', 'rm': '72', 'cm': '72', 'lm': '72',
                               'st': '79'}},
            'rm': {'name': 'A. Candreva', 'url': 'https://cdn.sofifa.com/players/173/221/22_60.png', 'position': 'rm',
                   'club': 'Everton', 'nationality': 'Italy', 'value': '8000000',
                   'rating': {'gk': '19', 'rb': '72', 'cb': '65', 'lb': '72', 'rm': '79', 'cm': '79', 'lm': '79',
                              'st': '78'}},

            'cmr': {'name': 'Miguel Veloso', 'url': 'https://cdn.sofifa.com/players/178/007/22_60.png',
                    'position': 'cm',
                    'club': 'Hellas Verona', 'nationality': 'Portugal', 'value': '5500000',
                    'rating': {'gk': '21', 'rb': '72', 'cb': '72', 'lb': '72', 'rm': '75', 'cm': '78', 'lm': '75',
                               'st': '72'}},
            'rb': {'name': 'S. Coleman', 'url': 'https://cdn.sofifa.com/players/180/216/22_60.png', 'position': 'rb',
                   'club': 'Everton', 'nationality': 'Republic of Ireland', 'value': '9500000',
                   'rating': {'gk': '19', 'rb': '78', 'cb': '78', 'lb': '78', 'rm': '75', 'cm': '76', 'lm': '75',
                              'st': '72'}},
            'lm': {'name': 'S. Blanco', 'url': 'https://cdn.sofifa.com/players/190/577/22_60.png', 'position': 'lm',
                   'club': 'Everton', 'nationality': 'Argentina', 'value': '6500000',
                   'rating': {'gk': '19', 'rb': '58', 'cb': '51', 'lb': '58', 'rm': '77', 'cm': '73', 'lm': '77',
                              'st': '76'}}}


def chemistry(team):
    calculate_chemistry = {
        'gk': 0,
        'cbl': 0,
        'cbr': 0,
        'lb': 0,
        'rb': 0,
        'lm': 0,
        'rm': 0,
        'cml': 0,
        'cmr': 0,
        'stl': 0,
        'str': 0,
    }
    for player, _ in list(calculate_chemistry.items()):
        result = 0
        for connection in CONNECTION[player]:
            if team[player]['club'] == team[connection]['club']:
                result += 10
            elif team[player]['nationality'] == team[connection]['nationality']:
                result += 7
        calculate_chemistry[player] = math.ceil(result / len(CONNECTION[player]))
    result = 0
    for position, value in calculate_chemistry.items():
        result += value
    return calculate_chemistry, result


def draw_pitch(team, team_chemistry):
    ImagePitch = Image.open(PITCH_PATH)
    ImagePitchCopy = ImageDraw.Draw(ImagePitch)

    connection = [
        ('gk', 'cbl', [(ImagePitch.width / 2, 1350), (ImagePitch.width / 2 - 150, 1100)]),
        ('gk', 'cbr', [(ImagePitch.width / 2, 1350), (ImagePitch.width / 2 + 150, 1100)]),
        ('cbl', 'cbr', [(ImagePitch.width / 2 - 150, 1100), (ImagePitch.width / 2 + 150, 1100)]),
        ('lb', 'cbl', [(ImagePitch.width / 2 - 150, 1100), (ImagePitch.width / 2 - 400, 1100)]),
        ('rb', 'cbr', [(ImagePitch.width / 2 + 150, 1100), (ImagePitch.width / 2 + 400, 1100)]),
        ('cbr', 'cmr', [(ImagePitch.width / 2 + 150, 1100), (ImagePitch.width / 2 + 150, 700)]),
        ('cbl', 'cml', [(ImagePitch.width / 2 - 150, 1100), (ImagePitch.width / 2 - 150, 700)]),
        ('rb', 'rm', [(ImagePitch.width / 2 + 400, 1100), (ImagePitch.width / 2 + 400, 700)]),
        ('lb', 'lm', [(ImagePitch.width / 2 - 400, 1100), (ImagePitch.width / 2 - 400, 700)]),
        ('cml', 'cmr', [(ImagePitch.width / 2 - 150, 700), (ImagePitch.width / 2 + 150, 700)]),
        ('cml', 'lm', [(ImagePitch.width / 2 - 150, 700), (ImagePitch.width / 2 - 400, 700)]),
        ('cmr', 'rm', [(ImagePitch.width / 2 + 150, 700), (ImagePitch.width / 2 + 400, 700)]),
        ('cmr', 'str', [(ImagePitch.width / 2 + 150, 700), (ImagePitch.width / 2 + 150, 300)]),
        ('cml', 'stl', [(ImagePitch.width / 2 - 150, 700), (ImagePitch.width / 2 - 150, 300)]),
        ('rm', 'str', [(ImagePitch.width / 2 + 400, 700), (ImagePitch.width / 2 + 150, 300)]),
        ('lm', 'stl', [(ImagePitch.width / 2 - 400, 700), (ImagePitch.width / 2 - 150, 300)]),
        ('stl', 'str', [(ImagePitch.width / 2 - 150, 300), (ImagePitch.width / 2 + 150, 300)])
    ]
    for i in connection:
        if team[i[0]]['club'] == team[i[1]]['club']:
            ImagePitchCopy.line(i[2], fill="green", width=10)
        elif team[i[0]]['nationality'] == team[i[1]]['nationality']:
            ImagePitchCopy.line(i[2], fill="yellow", width=10)
        else:
            ImagePitchCopy.line(i[2], fill="red", width=10)

    position_pitch = {
        'gk': (405, 1220),
        'cbl': (250, 1000),
        'cbr': (555, 1000),
        'lb': (0, 1000),
        'rb': (800, 1000),
        'lm': (0, 600),
        'rm': (800, 600),
        'cml': (250, 600),
        'cmr': (555, 600),
        'stl': (250, 200),
        'str': (555, 200),
    }
    rating = 0
    chemistry_teams = 0
    for i in team:
        create_player(team[i], i[0:2])
        ImagePlayer = Image.open(PLAYER_CARD)
        ImagePlayer = ImagePlayer.resize(CARD_SIZE)
        ImagePitch.paste(ImagePlayer, position_pitch[i], ImagePlayer)
        rating += int(team[i]['rating'][i[0:2]])
        if team[i]['position'] == i[0:2]:
            chemistry_teams += 4
        else:
            chemistry_teams += 2

    chemistry_teams += int(math.ceil(team_chemistry[1]))
    chemistry_teams = 100 if chemistry_teams > 100 else chemistry_teams
    ImagePitchCopy.text((0, 0), 'RATING: ' + str(math.ceil(rating / 11)), FONT_COLOR, align='left', font=PLAYER_FONT,
                        stroke_width=3)
    ImagePitchCopy.text((0, 50), 'CHEMISTRY: ' + str(chemistry_teams), FONT_COLOR, align='left',
                        font=PLAYER_FONT,
                        stroke_width=3)
    ImagePitch.save('result.png')


def create_team(team):
    team_chemistry = chemistry(team)
    draw_pitch(team, team_chemistry)


create_team(players_)
