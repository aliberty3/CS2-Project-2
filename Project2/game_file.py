# game_file.py
import random
import csv
from typing import List, Tuple

class DiceSimulator:
    def __init__(self):
        self.rolls: List[int] = []
        self.roll_history_file = "roll_history.csv"

    def roll_dice(self, num_dice: int, num_sides: int) -> List[int]:
        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        self.rolls.extend(rolls)
        self._save_roll_history(rolls)
        return rolls

    def get_statistics(self) -> Tuple[int, int, float]:
        num_rolls = len(self.rolls)
        total_sum = sum(self.rolls)
        average = total_sum / num_rolls if num_rolls > 0 else 0
        return num_rolls, total_sum, average

    def get_roll_history(self) -> List[List[int]]:
        with open(self.roll_history_file, "r", newline="") as file:
            reader = csv.reader(file)
            roll_history = [list(map(int, row)) for row in reader]
        return roll_history

    def _save_roll_history(self, rolls: List[int]) -> None:
        with open(self.roll_history_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(rolls)
