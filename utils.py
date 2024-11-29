import os

import requests
from dotenv import load_dotenv

load_dotenv()


def read_input(day: int, year: int = 2024) -> str:
    response = requests.get(
        url=f"https://adventofcode.com/{year}/day/{day}/input",
        cookies={"session": os.getenv("SESSION")}
    )
    response.raise_for_status()
    return response.text


def download_input(day: int, year: int = 2023, path: str = "input.txt") -> None:
    with open(path, "w") as file:
        file.write(read_input(day, year))
