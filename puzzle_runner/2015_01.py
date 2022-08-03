from utils import file


def load_data(file_name):
    with open(file_name) as f:
        data = f.read()
    return data


def solve_puzzle_one(instructions):
    floor = 0
    for instruction in instructions:
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
    return floor


def solve_puzzle_two(instructions):
    floor = 0
    for instruction_number, instruction in enumerate(instructions, 1):
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1

        if floor < 0:
            break
    return instruction_number


if __name__ == "__main__":
    puzzle_name = file.get_puzzle_name_from_module_path(__file__)
    input_path = file.create_input_path(puzzle_name)
    data = load_data(input_path)
    print(solve_puzzle_one(data))
    print(solve_puzzle_two(data))
