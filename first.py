import random

def guess_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            
            if guess == number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                if attempts < 5:
                    print("Wow, you're really good at this! You're in the top 1% of guessers.")
                elif attempts < 10:
                    print("Really, really good! Did you practice beforehand?")
                else:
                    print("Well, I guess you need some coffee.")
                break

            elif guess < number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
            
            attempts += 1
            
        except ValueError:
            print("Invalid input. Please enter a number.")
            
if __name__ == '__main__':
    guess_number()
