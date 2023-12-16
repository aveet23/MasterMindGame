# MatserMindGame

## Overview
This program is an implementation of the classic game Mastermind, where the player attempts to guess a secret code. The code consists of a combination of colored pegs, and the player has a limited number of attempts to guess the correct sequence.

## How to Play
1. The game generates a random secret code at the beginning.
2. The player has to guess the code within a specified number of tries (default is 10).
3. After each guess, the program provides feedback on the correctness of the guess.
4. The player wins by correctly guessing the code within the given number of attempts.

## Instructions
1. **Running the Game:**
    - Ensure you have Python installed on your system.
    - Run the script by executing the command: `python mastermind.py`

2. **Making a Guess:**
    - Enter your guess as a space-separated sequence of colors (e.g., "R G B Y").
    - You have to guess the correct combination of colors within the specified number of tries.

3. **Feedback:**
    - After each guess, the program will provide feedback on the correctness of your guess.
    - "Correct Positions" indicates the number of colors that are in the correct position.
    - "Incorrect Positions" indicates the number of correct colors but in the wrong position.

4. **Winning:**
    - If you guess the correct code within the allotted number of tries, you win!
    - The game will display the number of attempts it took to guess the code.

5. **Losing:**
    - If you run out of attempts, the secret code will be revealed.

6. **Valid Colors:**
    - The valid colors are "R" (Red), "G" (Green), "B" (Blue), "Y" (Yellow), "W" (White), and "O" (Orange).

## Customization
- You can customize the number of tries and the length of the secret code by modifying the `TRIES` and `CODE_LENGTH` constants in the code.

```python
# Example: Set the number of tries to 15 and the code length to 6
TRIES = 15
CODE_LENGTH = 6
```

Feel free to modify the code and experiment with different settings to enhance your gaming experience.

Enjoy playing Mastermind!
