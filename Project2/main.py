# main.py
import tkinter as tk
from gui import DiceRollingApp

def main() -> None:
    """
    Entry point of the program. Creates the Tkinter root window and initializes the DiceRollingApp.

    Returns:
        None
    """
    root = tk.Tk()
    app = DiceRollingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
