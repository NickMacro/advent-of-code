from utils import file


def load_data(file_name):
    return None


def solve_puzzle_one(instructions):
    return None


def solve_puzzle_two(instructions):
    return None


if __name__ == "__main__":
    puzzle_name = file.get_puzzle_name_from_module_path(__file__)
    input_path = file.create_input_path(puzzle_name)
    data = load_data(input_path)
    print(solve_puzzle_one(data))
    print(solve_puzzle_two(data))
