import pathlib


def get_project_directory():
    return pathlib.Path(__file__).parent.parent


def get_puzzle_name_from_module_path(path):
    return pathlib.Path(path).stem


def get_puzzle_name_from_test_path(path):
    return pathlib.Path(path).stem.split("_", maxsplit=1)[1]


def create_input_path(name):
    input_path = get_project_directory() / "inputs" / f"{name}.txt"
    return input_path



