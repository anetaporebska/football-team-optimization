import requests
from PIL import ImageDraw

from players.const.const import *


def save_country(country):
    url = URL_FLAGS % country
    response = requests.get(url)
    if response.status_code == 200:
        with open(COUNTRY_PATH, 'wb') as file:
            file.write(response.content)


def player_photo(path):
    url = path
    response = requests.get(url)
    if response.status_code == 200:
        with open(PLAYER_PHOTO, 'wb') as file:
            file.write(response.content)


def create_player(player, position):
    save_country(player['nationality'].lower())
    player_photo(player['url'])
    player_name = player['name']

    try:
        ImageCountry = Image.open(COUNTRY_PATH)
    except:
        ImageCountry = Image.open(POLAND)
    ImageCountry = ImageCountry.resize(COUNTRY_SIZE)
    ImageCountryCopy = ImageCountry.copy()
    ImageCard = Image.open(CARD)
    ImageCardCopy = ImageCard.copy()

    ImageCardCopy.paste(ImageCountryCopy, COUNTRY_PLACE)

    ImagePlayerPhoto = Image.open(PLAYER_PHOTO)
    ImagePlayerPhoto = ImagePlayerPhoto.resize(PLAYER_SIZE)
    ImagePlayerCopy = ImagePlayerPhoto.copy()
    ImageCardCopy.paste(ImagePlayerCopy, PLAYER_PLACE, ImagePlayerCopy)

    I1 = ImageDraw.Draw(ImageCardCopy)

    I1.text(NAME_LOCATION, player_name, FONT_COLOR, align='left', font=PLAYER_FONT, stroke_width=1)
    I1.text(POSITION_LOCATION, position.upper(), FONT_COLOR, align='left', font=POSITION_FONT, stroke_width=2)
    I1.text(RATING_LOCATION, player['rating'][position], FONT_COLOR, align='left', font=SCORE_FONT, stroke_width=3)

    ImageCardCopy.save(PLAYER_CARD + player_name.replace(' ', '') + PNG)
    ImageCardCopy.save(PLAYER_CARD_TEMPORARILY)
