import random
def attempt(num1):
    num = random.randint(1, 100)
    for i in range(num1,0,-1):
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            print(f"You have {i - 1} attempts remaining to guess the number.")
            continue  # Skip to the next iteration

        if guess==num:
            print("🎉 You Won!! 🎉")
            return
        elif guess<num:
            print("❌ Too Low.\nGuess again.")
        elif guess>num:
            print("❌ Too High.\nGuess again.")
        print(f"You have {i-1} attempts remaining to guess the number.")
        if i==1 and guess!=num:
            print(f"You've run out of guesses, you lose.\nThe correct number was {num}.")
print("""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\ \| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\_____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
""")
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level=input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
if level=="easy":
    turns=10
elif level=="hard":
    turns=5
else:
    print("❌ Invalid input. Please enter 'easy' or 'hard' next time.")
    exit()
attempt(turns)