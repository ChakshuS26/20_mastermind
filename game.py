import random
from logic import feedback


class Mastermind:
    def __init__(self):
        self.code = [str(random.randint(1, 6)) for _ in range(4)]
        self.history = []
        self.turns = 10
        self.game_over = False
        self.won = False

    def show_history(self):
        if not self.history:
            print("No guesses yet.")
            return

        print("\nGuess History:")
        for number, (guess, exact, partial) in enumerate(self.history, start=1):
            print(
                f"{number}. {guess} -> "
                f"Exact: {exact}, Partial: {partial}"
            )

    def run(self):
        if self.game_over:
            print("The game has already ended.")
            return

        print("Mastermind — enter four digits from 1 to 6.")

        while self.turns > 0 and not self.game_over:
            raw = input(f"{self.turns} turns left > ").strip()

            # Allow the player to quit without consuming a turn.
            if raw.lower() == "q":
                self.game_over = True
                print("Game quit.")
                return

            # Invalid guesses do not consume a turn.
            if len(raw) != 4 or any(ch not in "123456" for ch in raw):
                print("Enter exactly four digits from 1 to 6.")
                continue

            guess = list(raw)

            exact, partial = feedback(self.code, guess)

            # Only accepted guesses are stored in history.
            self.history.append((raw, exact, partial))
            self.turns -= 1

            print("Exact:", exact, " Partial:", partial)

            # Win condition.
            if exact == 4:
                self.won = True
                self.game_over = True
                print("Cracked the code!")
                self.show_history()
                return

        # Loss condition.
        if not self.won and self.turns == 0:
            self.game_over = True
            print("Out of turns!")
            print("The code was", "".join(self.code))
            self.show_history()