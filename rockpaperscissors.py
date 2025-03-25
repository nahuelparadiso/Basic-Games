import random

def play():
    choices = ["rock", "paper", "scissors"]
    
    user = input("Choose rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid choice. Try again.")
        return play()
    
    computer = random.choice(choices)

    print(f"\nYou chose: {user}")
    print(f"The computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win! 🎉")
    else:
        print("You lose. 😢")

# Run the game
if __name__ == "__main__":
    play()
