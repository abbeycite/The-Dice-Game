import random

def dice_game():
    high_score = 0
    while True:
        print("Current High score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        value = input("Enter your choice:")
        if value == "1":
            roll1 = random.randint(1,6)
            roll2 = random.randint(1,6)
            print("You rolled a ...", roll1)
            print("You rolled a ...", roll2)
            total_roll = roll1 + roll2
            print("You have rolled a total of :", total_roll)
            if total_roll > high_score:
                print("\n New high score!\n")
                print("high score =", total_roll)
        elif value == "2":
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice\n")

dice_game()
    