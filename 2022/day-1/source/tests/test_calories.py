from source.calories import get_most_calories

def test_get_most_calories() -> None:
	day_1_example = [
		'1000', '2000', '3000',
		None,
		'4000',
		None,
		'5000', '6000',
		None,
		'7000', '8000', '9000',
		None,
		'10000'
	]

	expected = 24000

	assert get_most_calories(day_1_example) == expected
