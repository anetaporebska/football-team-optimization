from PIL import ImageFont

JSON_PATH = 'football.json'
CSV_PATH = 'players_fifa22.csv'
COUNTRY_PATH = "country.png"
PLAYER_PHOTO = "player.png"
CARD = "player_card.png"
ARIAL = "arial.ttf"
PITCH_PATH = 'pitch.png'
PLAYER_CARD = 'card_player.png'
POLAND = 'poland.png'
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

CONNECTION = {
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


