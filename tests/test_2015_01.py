import pytest
from utils import factory, file

puzzle_name = file.get_puzzle_name_from_test_path(__file__)
runner = factory.create_puzzle_runner_module(puzzle_name)
input_path = file.create_input_path(puzzle_name)
data = runner.load_data(input_path)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("((()))", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ]
)
def test_basic_puzzle_one(test_input, expected):
    assert runner.solve_puzzle_one(test_input) == expected


def test_actual_puzzle_one():
    assert runner.solve_puzzle_one(data) == 74


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (")", 1),
        ("()())", 5),
    ]
)
def test_basic_puzzle_two(test_input, expected):
    assert runner.solve_puzzle_two(test_input) == expected


def test_actual_puzzle_two():
    assert runner.solve_puzzle_two(data) == 1795