from source.game import points_won_round

def get_all_input_from_file(file_name :str) -> list:
	input = []

	with open(file=file_name, mode='r') as f:
		for line in f:
			input.append(line[0])
			input.append(line[2])

	return input

def main() -> None:
	input = get_all_input_from_file('./data/input.txt')

	your_total_score = 0

	opponent_index, player_index = 0, 1

	for h in range(0, int(len(input)/2)):
		your_total_score += points_won_round(input[opponent_index], input[player_index])

		opponent_index += 2
		player_index += 2

	print(f"Your total score is {your_total_score}")

	# for i in input:
		# print(f"opponent = {input}")
		# print(f"player = {input}")
		# your_total_score += points_won_round(input[opponent_index], input[player_index])

if __name__ == '__main__':
	main()
