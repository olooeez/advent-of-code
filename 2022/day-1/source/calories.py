def get_most_calories(calories_list :list) -> int:
	calories_counter, max_calories = 0, 0

	for calories in calories_list:
		if calories != None:
			calories_counter += int(calories)
		else:
			if max_calories < calories_counter:
				max_calories = calories_counter

			calories_counter = 0

	return max_calories
