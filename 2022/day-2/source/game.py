from enum import Enum

class OutcomePoints(Enum):
	WON = 6
	LOST = 0
	DRAW = 3

class ShapePoints(Enum):
	X = 1
	Y = 2
	Z = 3

class WhoBeatsWho(Enum):
	X = 'C'
	Y = 'A'
	Z = 'B'

class Translate(Enum):
	X = 'A'
	Y = 'B'
	Z = 'C'

def play_result(opponent_play :str, your_play :str) -> OutcomePoints:
	if Translate[your_play].value == opponent_play:
		return OutcomePoints.DRAW

	if WhoBeatsWho[your_play].value == opponent_play:
		return OutcomePoints.WON
	else:
		return OutcomePoints.LOST

def points_won_round(opponent_play :str, your_play :str) -> int:
	game_result = play_result(opponent_play, your_play)

	return ShapePoints[your_play].value + game_result.value
		
