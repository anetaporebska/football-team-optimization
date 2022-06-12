import time
from PIL import ImageFont, Image

JSON_PATH = 'players/static/data/football.json'
CSV_PATH = 'players_fifa22.csv'
COUNTRY_PATH = "players/static/photo/country.png"
PLAYER_PHOTO = "players/static/photo/player.png"
CARD = "players/static/photo/player_card.png"
ARIAL = "players/static/font/arial.ttf"
PITCH_PATH = 'players/static/photo/pitch.png'
PLAYER_CARD = 'players/static/player_card/'
PLAYER_CARD_TEMPORARILY = 'players/static/photo/player.png'
POLAND = 'players/static/photo/poland.png'
RESULT_TEAM = 'players/static/result/resultTeam'
PNG = '.png'
URL_FLAGS = "https://countryflagsapi.com/png/%s"
RESULT_TEAM_PHOTO = RESULT_TEAM + str(time.time()) + PNG
SCORE_FONT = ImageFont.truetype(ARIAL, 150)
POSITION_FONT = ImageFont.truetype(ARIAL, 75)
PLAYER_FONT = ImageFont.truetype(ARIAL, 50)
FONT_COLOR = (0, 0, 0)
COUNTRY_SIZE = (150, 75)
COUNTRY_PLACE = (120, 350)
PLAYER_SIZE = (250, 250)
PLAYER_PLACE = (300, 175)
NAME_LOCATION = (100, 480)
POSITION_LOCATION = (125, 225)
RATING_LOCATION = (240, 560)
CARD_SIZE = (161, 225)
RATING_TEXT_POSITION = (0, 0)
CHEMISTRY_TEXT_POSITION = (0, 50)
TEXT_STROKE_WIDTH = 3
CHEMISTRY_ON_GOOD_POSITION = 4
OTHER_ON_OTHER_POSITION = 2

GK_POSITION = 1350
DEFENSE_POSITION = 1100
MIDFIELD_POSITION = 700
STRIKER_POSITION = 300
CENTER_PLAYERS_POSITION = 150
SIDE_PLAYERS_POSITION = 400

MAX_CHEMISTRY = 100
NUMBER_OF_PLAYER_IN_PITCH = 11
CONNECTION_WIDTH = 10
TEAM_CONNECTION = 'green'
NATIONALITY_CONNECTION = 'yellow'
NO_CONNECTION = 'red'

SIDE_WIDTH = Image.open(PITCH_PATH).width / 2

CONNECTION_BETWEEN_PLAYERS = [
    ('gk', 'cbl', [(SIDE_WIDTH, GK_POSITION), (SIDE_WIDTH - CENTER_PLAYERS_POSITION, DEFENSE_POSITION)]),
    ('gk', 'cbr', [(SIDE_WIDTH, GK_POSITION), (SIDE_WIDTH + CENTER_PLAYERS_POSITION, DEFENSE_POSITION)]),
    ('cbl', 'cbr', [(SIDE_WIDTH - CENTER_PLAYERS_POSITION, DEFENSE_POSITION),
                    (SIDE_WIDTH + CENTER_PLAYERS_POSITION, DEFENSE_POSITION)]),
    ('lb', 'cbl', [(SIDE_WIDTH - CENTER_PLAYERS_POSITION, DEFENSE_POSITION),
                   (SIDE_WIDTH - SIDE_PLAYERS_POSITION, DEFENSE_POSITION)]),
    ('rb', 'cbr', [(SIDE_WIDTH + CENTER_PLAYERS_POSITION, DEFENSE_POSITION),
                   (SIDE_WIDTH + SIDE_PLAYERS_POSITION, DEFENSE_POSITION)]),
    ('cbr', 'cmr', [(SIDE_WIDTH + CENTER_PLAYERS_POSITION, DEFENSE_POSITION),
                    (SIDE_WIDTH + CENTER_PLAYERS_POSITION, MIDFIELD_POSITION)]),
    ('cbl', 'cml', [(SIDE_WIDTH - CENTER_PLAYERS_POSITION, DEFENSE_POSITION),
                    (SIDE_WIDTH - CENTER_PLAYERS_POSITION, MIDFIELD_POSITION)]),
    ('rb', 'rm',
     [(SIDE_WIDTH + SIDE_PLAYERS_POSITION, DEFENSE_POSITION), (SIDE_WIDTH + SIDE_PLAYERS_POSITION, MIDFIELD_POSITION)]),
    ('lb', 'lm',
     [(SIDE_WIDTH - SIDE_PLAYERS_POSITION, DEFENSE_POSITION), (SIDE_WIDTH - SIDE_PLAYERS_POSITION, MIDFIELD_POSITION)]),
    ('cml', 'cmr', [(SIDE_WIDTH - CENTER_PLAYERS_POSITION, MIDFIELD_POSITION),
                    (SIDE_WIDTH + CENTER_PLAYERS_POSITION, MIDFIELD_POSITION)]),
    ('cml', 'lm', [(SIDE_WIDTH - CENTER_PLAYERS_POSITION, MIDFIELD_POSITION),
                   (SIDE_WIDTH - SIDE_PLAYERS_POSITION, MIDFIELD_POSITION)]),
    ('cmr', 'rm', [(SIDE_WIDTH + CENTER_PLAYERS_POSITION, MIDFIELD_POSITION),
                   (SIDE_WIDTH + SIDE_PLAYERS_POSITION, MIDFIELD_POSITION)]),
    ('cmr', 'str', [(SIDE_WIDTH + CENTER_PLAYERS_POSITION, MIDFIELD_POSITION),
                    (SIDE_WIDTH + CENTER_PLAYERS_POSITION, STRIKER_POSITION)]),
    ('cml', 'stl', [(SIDE_WIDTH - CENTER_PLAYERS_POSITION, MIDFIELD_POSITION),
                    (SIDE_WIDTH - CENTER_PLAYERS_POSITION, STRIKER_POSITION)]),
    ('rm', 'str', [(SIDE_WIDTH + SIDE_PLAYERS_POSITION, MIDFIELD_POSITION),
                   (SIDE_WIDTH + CENTER_PLAYERS_POSITION, STRIKER_POSITION)]),
    ('lm', 'stl', [(SIDE_WIDTH - SIDE_PLAYERS_POSITION, MIDFIELD_POSITION),
                   (SIDE_WIDTH - CENTER_PLAYERS_POSITION, STRIKER_POSITION)]),
    ('stl', 'str', [(SIDE_WIDTH - CENTER_PLAYERS_POSITION, STRIKER_POSITION),
                    (SIDE_WIDTH + CENTER_PLAYERS_POSITION, STRIKER_POSITION)])
]

PLAYER_POSITION = ['gk', 'rb', 'cbl', 'cbr', 'lb', 'rm', 'cml', 'cmr', 'lm', 'stl', 'str']

CONNECTION_ON_PITCH = {
    'gk': ['cbl', 'cbr'],
    'cbl': ['cbr', 'gk', 'cml', 'lb'],
    'cbr': ['cbl', 'gk', 'cmr', 'rb'],
    'lb': ['cbl', 'lm'],
    'rb': ['cbr', 'rm'],
    'lm': ['lb', 'stl', 'cml'],
    'rm': ['rb', 'str', 'cmr'],
    'cml': ['cmr', 'cbl', 'lm', 'stl'],
    'cmr': ['cml', 'cbr', 'rm', 'str'],
    'stl': ['str', 'lm', 'cml'],
    'str': ['stl', 'rm', 'cmr'],
}

POSITION_ON_PITCH = {
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

CALCULATE_CHEMISTRY = {
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

testing_data_1 = {
    'gk': {'name': 'S. Handanovic', 'url': 'https://cdn.sofifa.com/players/162/835/22_60.png', 'position': 'gk',
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

testing_data_2 = {
    'gk': {'name': 'S. Handanovic', 'url': 'https://cdn.sofifa.com/players/162/835/22_60.png', 'position': 'gk',
           'club': 'Inter', 'nationality': 'Slovenia', 'value': '7500000',
           'rating': {'gk': '86', 'rb': '32', 'cb': '32', 'lb': '32', 'rm': '34', 'cm': '37', 'lm': '34',
                      'st': '33'}},
    'cbl': {'name': 'Thiago Silva', 'url': 'https://cdn.sofifa.com/players/164/240/22_60.png', 'position': 'cb',
            'club': 'Chelsea', 'nationality': 'Brazil', 'value': '9500000',
            'rating': {'gk': '21', 'rb': '80', 'cb': '85', 'lb': '80', 'rm': '70', 'cm': '78', 'lm': '70',
                       'st': '68'}},
    'cbr':
        {'name': 'T. Alderweireld', 'url': 'https://cdn.sofifa.com/players/184/087/22_60.png', 'position': 'cb',
         'club': 'Free agent', 'nationality': 'Belgium', 'value': '0',
         'rating': {'gk': '24', 'rb': '81', 'cb': '83', 'lb': '81', 'rm': '69', 'cm': '76', 'lm': '69',
                    'st': '68'}},

    'cml': {'name': 'Joao Moutinho', 'url': 'https://cdn.sofifa.com/players/162/347/22_60.png',
            'position': 'cm',
            'club': 'Wolverhampton Wanderers', 'nationality': 'Portugal', 'value': '9500000',
            'rating': {'gk': '23', 'rb': '75', 'cb': '73', 'lb': '75', 'rm': '78', 'cm': '80', 'lm': '78',
                       'st': '74'}},
    'lb': {'name': 'Nacho Monreal', 'url': 'https://cdn.sofifa.com/players/177/604/22_60.png', 'position': 'lb',
           'club': 'Real Sociedad', 'nationality': 'Spain', 'value': '6500000',
           'rating': {'gk': '16', 'rb': '79', 'cb': '79', 'lb': '79', 'rm': '74', 'cm': '76', 'lm': '74',
                      'st': '71'}},
    'stl': {'name': 'Y. El Arabi', 'url': 'https://cdn.sofifa.com/players/194/209/22_60.png', 'position': 'st',
            'club': 'Olympiacos CFP', 'nationality': 'Morocco', 'value': '8500000',
            'rating': {'gk': '19', 'rb': '58', 'cb': '54', 'lb': '58', 'rm': '77', 'cm': '73', 'lm': '77',
                       'st': '79'}},
    'str': {'name': 'O. Giroud', 'url': 'https://cdn.sofifa.com/players/178/509/22_60.png', 'position': 'st',
            'club': 'AC Milan', 'nationality': 'France', 'value': '8500000',
            'rating': {'gk': '20', 'rb': '54', 'cb': '59', 'lb': '54', 'rm': '72', 'cm': '72', 'lm': '72',
                       'st': '79'}},
    'rm': {'name': 'A. Candreva', 'url': 'https://cdn.sofifa.com/players/173/221/22_60.png', 'position': 'rm',
           'club': 'U.C. Sampdoria', 'nationality': 'Italy', 'value': '8000000',
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
           'club': 'Portland Timbers', 'nationality': 'Argentina', 'value': '6500000',
           'rating': {'gk': '19', 'rb': '58', 'cb': '51', 'lb': '58', 'rm': '77', 'cm': '73', 'lm': '77',
                      'st': '76'}}}

testing_data_3 = {
    'gk': {'name': 'L. Fabianski', 'url': 'https://cdn.sofifa.com/players/164/835/22_60.png', 'position': 'gk',
           'club': 'West Ham United', 'nationality': 'Poland', 'value': '3400000',
           'rating': {'gk': '82', 'rb': '27', 'cb': '29', 'lb': '27', 'rm': '31', 'cm': '31', 'lm': '31', 'st': '31'}},
    'cbl': {'name': 'Jose Fonte', 'url': 'https://cdn.sofifa.com/players/171/791/22_60.png', 'position': 'cb',
            'club': 'LOSC Lille', 'nationality': 'Portugal', 'value': '4600000',
            'rating': {'gk': '20', 'rb': '72', 'cb': '81', 'lb': '72', 'rm': '61', 'cm': '70', 'lm': '61', 'st': '62'}},
    'cbr':
        {'name': 'T. Alderweireld', 'url': 'https://cdn.sofifa.com/players/184/087/22_60.png', 'position': 'cb',
         'club': 'Free agent', 'nationality': 'Belgium', 'value': '0',
         'rating': {'gk': '24', 'rb': '81', 'cb': '83', 'lb': '81', 'rm': '69', 'cm': '76', 'lm': '69',
                    'st': '68'}},
    'cml': {'name': 'J. Sosa', 'url': 'https://cdn.sofifa.com/players/143/121/22_60.png', 'position': 'cm',
            'club': 'Fenerbahce SK', 'nationality': 'Argentina', 'value': '2400000',
            'rating': {'gk': '19', 'rb': '70', 'cb': '67', 'lb': '70', 'rm': '76', 'cm': '76', 'lm': '76', 'st': '71'}},
    'lb': {'name': 'A. Kolarov', 'url': 'https://cdn.sofifa.com/players/185/103/22_60.png', 'position': 'lb',
           'club': 'Inter', 'nationality': 'Serbia', 'value': '4300000',
           'rating': {'gk': '23', 'rb': '78', 'cb': '78', 'lb': '78', 'rm': '76', 'cm': '78', 'lm': '76', 'st': '76'}},
    'stl': {'name': 'A. Dzyuba', 'url': 'https://cdn.sofifa.com/players/187/607/22_60.png', 'position': 'st',
            'club': 'Free agent', 'nationality': 'Russia', 'value': '0',
            'rating': {'gk': '20', 'rb': '52', 'cb': '52', 'lb': '52', 'rm': '75', 'cm': '71', 'lm': '75', 'st': '78'}},
    'str': {'name': 'Soldado', 'url': 'https://cdn.sofifa.com/players/146/758/22_60.png', 'position': 'st',
            'club': 'Levante Union Deportiva', 'nationality': 'Spain', 'value': '3600000',
            'rating': {'gk': '21', 'rb': '58', 'cb': '60', 'lb': '58', 'rm': '75', 'cm': '73', 'lm': '75', 'st': '77'}},
    'rm': {'name': 'R. Sambueza', 'url': 'https://cdn.sofifa.com/players/152/916/22_60.png', 'position': 'rm',
           'club': 'Deportivo Toluca', 'nationality': 'Argentina', 'value': '3400000',
           'rating': {'gk': '19', 'rb': '63', 'cb': '60', 'lb': '63', 'rm': '77', 'cm': '77', 'lm': '77', 'st': '74'}},
    'cmr': {'name': 'L. Montes', 'url': 'https://cdn.sofifa.com/players/184/703/22_60.png', 'position': 'cm',
            'club': 'Club Leon', 'nationality': 'Mexico', 'value': '4200000',
            'rating': {'gk': '19', 'rb': '67', 'cb': '64', 'lb': '67', 'rm': '77', 'cm': '77', 'lm': '77', 'st': '73'}},
    'rb': {'name': 'L. De Silvestri', 'url': 'https://cdn.sofifa.com/players/170/320/22_60.png', 'position': 'rb',
           'club': 'Bologna', 'nationality': 'Italy', 'value': '3900000',
           'rating': {'gk': '22', 'rb': '76', 'cb': '76', 'lb': '76', 'rm': '75', 'cm': '74', 'lm': '75', 'st': '74'}},
    'lm': {'name': 'M. Gradel', 'url': 'https://cdn.sofifa.com/players/182/945/22_60.png', 'position': 'lm',
           'club': 'Demir Grup Sivasspor', 'nationality': "Cote d'Ivoire", 'value': '4700000',
           'rating': {'gk': '20', 'rb': '60', 'cb': '54', 'lb': '60', 'rm': '76', 'cm': '74', 'lm': '76', 'st': '76'}}}

testing_data_4 = {
    'gk': {'name': 'M. Neuer', 'url': 'https://cdn.sofifa.com/players/167/495/22_60.png', 'position': 'gk',
           'club': 'FC Bayern Munchen', 'nationality': 'Germany', 'value': '13500000',
           'rating': {'gk': '90', 'rb': '38', 'cb': '37', 'lb': '38', 'rm': '47', 'cm': '53', 'lm': '47', 'st': '43'}},
    'cbr': {'name': 'M. Hummels', 'url': 'https://cdn.sofifa.com/players/178/603/22_60.png', 'position': 'cb',
            'club': 'Borussia Dortmund', 'nationality': 'Germany', 'value': '44000000',
            'rating': {'gk': '20', 'rb': '83', 'cb': '86', 'lb': '83', 'rm': '74', 'cm': '81', 'lm': '74', 'st': '73'}},
    'cbl':
        {'name': 'Sergio Ramos', 'url': 'https://cdn.sofifa.com/players/155/862/22_60.png', 'position': 'cb',
         'club': 'Paris Saint-Germain', 'nationality': 'Spain', 'value': '24000000',
         'rating': {'gk': '21', 'rb': '86', 'cb': '88', 'lb': '86', 'rm': '77', 'cm': '82', 'lm': '77', 'st': '79'}},
    'cml': {'name': 'G. Wijnaldum', 'url': 'https://cdn.sofifa.com/players/181/291/22_60.png', 'position': 'cm',
            'club': 'Paris Saint-Germain', 'nationality': 'Netherlands', 'value': '40500000',
            'rating': {'gk': '22', 'rb': '83', 'cb': '82', 'lb': '83', 'rm': '84', 'cm': '84', 'lm': '84', 'st': '83'}},
    'lb': {'name': 'Jordi Alba', 'url': 'https://cdn.sofifa.com/players/189/332/22_60.png', 'position': 'lb',
           'club': 'FC Barcelona', 'nationality': 'Spain', 'value': '47000000',
           'rating': {'gk': '22', 'rb': '85', 'cb': '79', 'lb': '85', 'rm': '86', 'cm': '84', 'lm': '86', 'st': '79'}},
    'str': {'name': 'Cristiano Ronaldo', 'url': 'https://cdn.sofifa.com/players/020/801/22_60.png', 'position': 'st',
            'club': 'Manchester United', 'nationality': 'Portugal', 'value': '45000000',
            'rating': {'gk': '23', 'rb': '63', 'cb': '56', 'lb': '63', 'rm': '89', 'cm': '81', 'lm': '89', 'st': '91'}},
    'stl': {'name': 'L. Suarez', 'url': 'https://cdn.sofifa.com/players/176/580/22_60.png', 'position': 'st',
            'club': 'Atletico de Madrid', 'nationality': 'Uruguay', 'value': '44500000',
            'rating': {'gk': '40', 'rb': '66', 'cb': '64', 'lb': '66', 'rm': '86', 'cm': '83', 'lm': '86', 'st': '88'}},
    'rm': {'name': 'Ronaldo Cabrais', 'url': 'https://cdn.sofifa.com/players/230/481/22_60.png', 'position': 'rm',
           'club': 'Gremio', 'nationality': 'Brazil', 'value': '35500000',
           'rating': {'gk': '23', 'rb': '63', 'cb': '53', 'lb': '63', 'rm': '83', 'cm': '80', 'lm': '83', 'st': '81'}},
    'cmr': {'name': 'L. Modric', 'url': 'https://cdn.sofifa.com/players/177/003/22_60.png', 'position': 'cm',
            'club': 'Real Madrid CF', 'nationality': 'Croatia', 'value': '32000000',
            'rating': {'gk': '22', 'rb': '81', 'cb': '75', 'lb': '81', 'rm': '87', 'cm': '87', 'lm': '87', 'st': '79'}},
    'rb': {'name': 'K. Walker', 'url': 'https://cdn.sofifa.com/players/188/377/22_60.png', 'position': 'rb',
           'club': 'Manchester City', 'nationality': 'England', 'value': '39000000',
           'rating': {'gk': '22', 'rb': '85', 'cb': '84', 'lb': '85', 'rm': '81', 'cm': '80', 'lm': '81', 'st': '77'}},
    'lm': {'name': 'Y. Carrasco', 'url': 'https://cdn.sofifa.com/players/208/418/22_60.png', 'position': 'lm',
           'club': 'Atletico de Madrid', 'nationality': 'Belgium', 'value': '45000000',
           'rating': {'gk': '21', 'rb': '66', 'cb': '57', 'lb': '66', 'rm': '84', 'cm': '79', 'lm': '84', 'st': '82'}}}
