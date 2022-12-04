from source.game import points_won_round

def test_points_won_round() -> None:
	day_2_example = {
		'A': 'Y',
		'B': 'X',
		'C': 'Z'
	}

	points_won, points_expected = 0, 15
	for opponent, you in day_2_example.items():
		points_won += points_won_round(opponent_play=opponent, your_play=you)

	assert points_won == points_expected
