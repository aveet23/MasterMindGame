import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    code = []

    # Loop through a range of the desired code length
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS) # Select a random color from the list of available colors
        code.append(color) # Add the selected color to the code list 

    return code

def guess_code():
    # Get guess from user
    while True:
        guess = input("Guess: ").upper().split(" ")
    
        # Check if guess has correct length
        if len(guess) != 4:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        # Check if all colors in guess are valid
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            break

    # Return guess            
    return guess  

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    # Count color frequency in real code
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    # Check for correct color and position
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1 
            color_counts[guess_color] -= 1   
    
    # Check for correct color but incorrect position
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    # Welcome message and rules
    print(f"Welcome to mastermind, you have {TRIES} to guess the code...")
    print("The valid colors are", *COLORS)

    # Generate and store secret code
    code = generate_code()
    # Attempt guessing loop
    for attempts in range(1, TRIES + 1):
        # Get guess from user
        guess = guess_code()
        # Check correct and incorrect positions
        correct_pos, incorrect_pos = check_code(guess, code)

        # Check if all positions are correct
        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        # Display result
        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")

    else:
        # If user ran out of tries, reveal the code
        print("You ran out of tries, the code was:", *code )


if __name__ == "__main__":
    game()


            

