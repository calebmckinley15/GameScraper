# Author: Caleb McKinley
# Date: 04/08/25
# File: sudoku_scraper.py
# Description: Web scrapes all the sudoku daily puzzles to solve, and previous solutions

import requests
from bs4 import BeautifulSoup
import json

def get_sudoku_game():
    url = "https://nine.websudoku.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    board = []
    for row in range(9):
        current_row = []
        for col in range(9):
            cell_id = f'f{row}{col}'
            cell = soup.find('input', {'id': cell_id})
            val = cell.get('value')
            current_row.append(int(val) if val else 0)
        board.append(current_row)

    with open("data/sudoku_puzzles.json", "w") as f:
        json.dump({"board": board}, f, indent=2)

    return board
