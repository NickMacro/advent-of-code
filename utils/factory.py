import importlib


def create_puzzle_runner_module(name):
    return importlib.import_module(f"puzzle_runner.{name}")
