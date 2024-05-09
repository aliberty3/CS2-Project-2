# gui.py
import tkinter as tk
from game_file import DiceSimulator
from typing import List

class DiceRollingApp:
    def __init__(self, root: tk.Tk):
        """
        Initialize the GUI for the Dice Rolling Simulator.

        Args:
            root (tk.Tk): The Tkinter root window.
        """
        self.root = root
        self.root.title("Dice Rolling Simulator")

        self.simulator = DiceSimulator()

        # Start button
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack()

        # Entry fields for number of dice and sides (initially hidden)
        self.num_dice_label = tk.Label(self.root, text="Number of Dice:")
        self.num_dice_entry = tk.Entry(self.root)
        self.num_sides_label = tk.Label(self.root, text="Number of Sides:")
        self.num_sides_entry = tk.Entry(self.root)
        self.roll_button = tk.Button(self.root, text="Roll Dice", command=self.roll_dice)

        # Game Over button
        self.game_over_button = tk.Button(self.root, text="Game Over", command=self.game_over)

        # Roll history button
        self.roll_history_button = tk.Button(self.root, text="Roll History", command=self.show_roll_history)

        # Labels to display individual dice rolls
        self.roll_labels: List[tk.Label] = []
        self.roll_result_frame = tk.Frame(self.root)

        # Label to display total rolls, sum, and average
        self.stats_label = tk.Label(self.root, text="")

    def start_game(self) -> None:
        """
        Show entry fields for number of dice and sides, and roll button.
        """
        self.start_button.pack_forget()

        self.num_dice_label.pack()
        self.num_dice_entry.pack()
        self.num_sides_label.pack()
        self.num_sides_entry.pack()
        self.roll_button.pack()

        # Pack labels for displaying individual dice rolls and statistics
        self.roll_result_frame.pack()
        self.stats_label.pack()

        # Display the "Game Over" button
        self.game_over_button.pack()

    def roll_dice(self) -> None:
        """
        Roll the dice and display the results.
        """
        # Clear previous rolls
        for label in self.roll_labels:
            label.destroy()
        self.roll_labels.clear()

        # Get number of dice and sides from entry fields
        num_dice_str = self.num_dice_entry.get()
        num_sides_str = self.num_sides_entry.get()

        # Validate input
        if not num_dice_str or not num_sides_str:
            # Display error message if either field is empty
            error_label = tk.Label(self.root, text="Please enter values for number of dice and sides.")
            error_label.pack()
            return

        try:
            num_dice = int(num_dice_str)
            num_sides = int(num_sides_str)
        except ValueError:
            # Display error message if input is not a valid integer
            error_label = tk.Label(self.root, text="Please enter valid integer values.")
            error_label.pack()
            return

        # Roll the dice
        rolls = self.simulator.roll_dice(num_dice, num_sides)

        # Display individual dice rolls
        for roll in rolls:
            label = tk.Label(self.roll_result_frame, text=f"Roll: {roll}")
            label.pack()
            self.roll_labels.append(label)

        # Update statistics
        self.update_statistics()

    def update_statistics(self) -> None:
        """
        Update the statistics label with total rolls, sum, and average.
        """
        num_rolls, total_sum, average = self.simulator.get_statistics()
        self.stats_label.config(text=f"Total Rolls: {num_rolls}, Total Sum: {total_sum}, Average: {average:.2f}")

    def game_over(self) -> None:
        """
        Display the "Game Over" message and the "Roll History" button.
        """
        self.start_button.pack_forget()
        self.num_dice_label.pack_forget()
        self.num_dice_entry.pack_forget()
        self.num_sides_label.pack_forget()
        self.num_sides_entry.pack_forget()
        self.roll_button.pack_forget()
        self.game_over_button.pack_forget()

        # Display the "Roll History" button
        self.roll_history_button.pack()

        game_over_label = tk.Label(self.root, text="Game Over")
        game_over_label.pack()

    def show_roll_history(self) -> None:
        """
        Display the roll history.
        """
        roll_history = self.simulator.get_roll_history()
        history_window = tk.Toplevel(self.root)
        history_window.title("Roll History")

        for rolls in roll_history:
            rolls_str = ", ".join(map(str, rolls))
            label = tk.Label(history_window, text=rolls_str)
            label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollingApp(root)
    root.mainloop()
