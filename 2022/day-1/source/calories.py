def get_top_tree_most_calories(calories_list :list) -> list:
	calories_counter, calories_added = 0, []

	for calories in calories_list:
		if calories != None:
			calories_counter += int(calories)
			continue

		calories_added.append(calories_counter)
		calories_counter = 0

	calories_added.append(calories_counter) # Add the last one
	calories_added.sort(reverse=True)

	return calories_added[0:3]
