import math

from PIL import ImageDraw

from players.const.const import *
from players.create_player_card import create_player


def chemistry_score(team):
    for player, _ in list(CALCULATE_CHEMISTRY.items()):
        result = 0
        for connection in CONNECTION_ON_PITCH[player]:
            if team[player]['aux'][0] == team[connection]['aux'][0]:
                result += 10
            elif team[player]['aux'][1] == team[connection]['aux'][1]:
                result += 7
        CALCULATE_CHEMISTRY[player] = math.ceil(result / len(CONNECTION_ON_PITCH[player]))
    result = 0
    for index, player in enumerate(team):
        if team[player]['ratings'][index] == max(team[player]['ratings']):
            CALCULATE_CHEMISTRY[PLAYER_POSITION[index]] += CHEMISTRY_ON_GOOD_POSITION
        else:
            CALCULATE_CHEMISTRY[PLAYER_POSITION[index]] += OTHER_ON_OTHER_POSITION

    for position, value in CALCULATE_CHEMISTRY.items():
        result += value if value < 10 else 10

    return result


def chemistry(team):
    for player, _ in list(CALCULATE_CHEMISTRY.items()):
        result = 0
        for connection in CONNECTION_ON_PITCH[player]:
            if team[player]['club'] == team[connection]['club']:
                result += 10
            elif team[player]['nationality'] == team[connection]['nationality']:
                result += 7
        CALCULATE_CHEMISTRY[player] = math.ceil(result / len(CONNECTION_ON_PITCH[player]))
    result = 0
    for connection in team:
        if team[connection]['position'] == connection[0:2]:
            CALCULATE_CHEMISTRY[connection] += CHEMISTRY_ON_GOOD_POSITION
        else:
            CALCULATE_CHEMISTRY[connection] += OTHER_ON_OTHER_POSITION

    for position, value in CALCULATE_CHEMISTRY.items():
        result += value if value < 10 else 10
    return result


def draw_pitch(team, team_chemistry):
    ImagePitch = Image.open(PITCH_PATH)
    ImagePitchCopy = ImageDraw.Draw(ImagePitch)

    for connection in CONNECTION_BETWEEN_PLAYERS:
        if team[connection[0]]['club'] == team[connection[1]]['club']:
            ImagePitchCopy.line(connection[2], fill=TEAM_CONNECTION, width=CONNECTION_WIDTH)
        elif team[connection[0]]['nationality'] == team[connection[1]]['nationality']:
            ImagePitchCopy.line(connection[2], fill=NATIONALITY_CONNECTION, width=CONNECTION_WIDTH)
        else:
            ImagePitchCopy.line(connection[2], fill=NO_CONNECTION, width=CONNECTION_WIDTH)

    rating = 0
    chemistry_teams = 0
    for connection in team:
        create_player(team[connection], connection[0:2])
        ImagePlayer = Image.open(PLAYER_CARD_TEMPORARILY)
        ImagePlayer = ImagePlayer.resize(CARD_SIZE)
        ImagePitch.paste(ImagePlayer, POSITION_ON_PITCH[connection], ImagePlayer)
        rating += int(team[connection]['rating'][connection[0:2]])

    chemistry_teams += int(math.ceil(team_chemistry))
    chemistry_teams = MAX_CHEMISTRY if chemistry_teams > MAX_CHEMISTRY else chemistry_teams
    ImagePitchCopy.text(RATING_TEXT_POSITION, 'RATING: ' + str(math.ceil(rating / NUMBER_OF_PLAYER_IN_PITCH))
                        , FONT_COLOR, align='left', font=PLAYER_FONT,
                        stroke_width=TEXT_STROKE_WIDTH)
    ImagePitchCopy.text(CHEMISTRY_TEXT_POSITION, 'CHEMISTRY: ' + str(chemistry_teams), FONT_COLOR, align='left',
                        font=PLAYER_FONT,
                        stroke_width=TEXT_STROKE_WIDTH)
    ImagePitch.save(RESULT_TEAM_PHOTO)


def create_team(team):
    team_chemistry = chemistry(team)
    draw_pitch(team, team_chemistry)

# create_team(testing_data_4)
