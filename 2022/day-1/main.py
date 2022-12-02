from source.calories import get_top_tree_most_calories

def get_calories_from_file(file_name :str) -> list:
    calories = []

    with open(file=file_name, mode='r') as f:
        for calorie in f:
            if calorie == '\n': # The separator from one elf to another
                calories.append(None)
            else:
                calories.append(calorie[0:-1]) # The "[0:-1]" removes the '\n'

    return calories

def main():
    calories = get_calories_from_file(file_name='./data/input.txt')
    top_tree_calories = get_top_tree_most_calories(calories_list=calories)

    print(f"The top three Elves are carrying {sum(top_tree_calories)} Calories")

if __name__ == '__main__':
    main()
