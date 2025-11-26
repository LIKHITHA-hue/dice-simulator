import random

print("Dice Rolling Simulator 🎲")

while True:
    input("Press Enter to roll the dice...")

    dice = random.randint(1, 6)
    print(f"You rolled: {dice}")

    again = input("Roll again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye dawg!")
        break
