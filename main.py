from utils import file, factory

year = input("What year's puzzle do you want to solve? (2015 - 2021): ")
day = input("What day's puzzle do you want to solve? (1 - 25): ")
puzzle_name = f"{year}_{day.zfill(2)}"

runner = factory.create_puzzle_runner_module(puzzle_name)
input_path = file.create_input_path(puzzle_name)

data = runner.load_data(input_path)

print(f"The solution to puzzle one is {runner.solve_puzzle_one(data)}.")
print(f"The solution to puzzle two is {runner.solve_puzzle_two(data)}.")
