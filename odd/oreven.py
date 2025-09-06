import random

class OddOrEvenGame:
    def __init__(self, player_number, player_choice, computer_number):
        self.player_number = player_number
        self.player_choice = player_choice
        self.computer_number = computer_number
        self.total = 0
        self.ctotal = 0
        self.player_role = None
        self.computer_role = None

        self.toss_result()
        self.play_game()

    def toss_result(self):
        if self.player_number == self.computer_number:
            print("Game is a tie. You bat first.")
            self.player_role = "b"
            self.computer_role = "bw"
        elif ((self.player_number + self.computer_number) % 2 == 0 and self.player_choice == "e") or \
             ((self.player_number + self.computer_number) % 2 != 0 and self.player_choice == "o"):
            print("You win the toss!")
            self.choose_role()
        else:
            print("You lose the toss. Computer chooses...")
            self.computer_chooses_role()

    def choose_role(self):
        choice = input("Choose batting or bowling (b or bw): ").strip().lower()
        if choice == "b":
            self.player_role = "b"
            self.computer_role = "bw"
        else:
            self.player_role = "bw"
            self.computer_role = "b"

    def computer_chooses_role(self):
        comp_choice = random.choice(["b", "bw"])
        self.computer_role = comp_choice
        self.player_role = "bw" if comp_choice == "b" else "b"
        print(f"Computer chooses {comp_choice}")

    def play_game(self):
        if self.player_role == "b":
            self.total = self.batting_phase("player")
            self.ctotal = self.chase_phase("computer", self.total)
        else:
            self.ctotal = self.batting_phase("computer")
            self.total = self.chase_phase("player", self.ctotal)

        self.declare_result()

    def batting_phase(self, who):
        score = 0
        print(f"\n{who.capitalize()} is batting...")
        while True:
            shoot = int(input("Enter a number from 1 to 10: "))
            comp_shoot = random.randint(1, 10)
            if shoot == comp_shoot:
                print(f"{who.capitalize()} is out! Total score: {score}")
                break
            else:
                score += shoot if who == "player" else comp_shoot
        return score

    def chase_phase(self, who, target):
        score = 0
        print(f"\n{who.capitalize()} is chasing a target of {target}...")
        while True:
            shoot = int(input("Enter a number from 1 to 10: "))
            comp_shoot = random.randint(1, 10)
            if shoot == comp_shoot:
                print(f"{who.capitalize()} is out! Total score: {score}")
                break
            else:
                score += shoot if who == "player" else comp_shoot
                if score > target:
                    print(f"{who.capitalize()} has chased successfully! Total score: {score}")
                    break
        return score

    def declare_result(self):
        print(f"\nFinal Scores:\nYou: {self.total}\nComputer: {self.ctotal}")
        if self.total == self.ctotal:
            print("The game is a tie!")
        elif self.total > self.ctotal:
            print("You won!")
        else:
            print("You lost!")

# Game Start
player_choice = input("Enter your choice: odd(o) or even(e): ").strip().lower()
player_number = int(input("Enter your chosen number between 1 to 10: "))
computer_number = random.randint(1, 10)

print(f"You chose: {player_number}")
print(f"Computer chose: {computer_number}")

game = OddOrEvenGame(player_number, player_choice, computer_number)