# Python Mastermind Code Breaker

A command-line code-breaking game built with Python and inspired by Mastermind. The game generates a secret four-color code, and players attempt to crack it within a limited number of tries.

## Features

- **Random code generation:** Generates a secret code containing four colors.
- **Three difficulty levels:**
  - Easy: 10 attempts
  - Medium: 7 attempts
  - Hard: 5 attempts
- **Input validation:** Checks that guesses contain four valid color codes.
- **Position feedback:** Shows how many colors are in the correct position and how many are correct but misplaced.
- **Win and lose conditions:** Announces victory or reveals the secret code when attempts run out.
- **Duplicate-aware checking:** Accounts for repeated colors when calculating feedback.

## Technologies Used

- Python
- `random` module
- Functions
- Lists and dictionaries
- Loops and conditional statements
- Input validation
- Basic game logic

## Available Colors

| Code | Color |
|---|---|
| R | Red |
| G | Green |
| B | Blue |
| Y | Yellow |
| W | White |
| O | Orange |

## How to Run

1. Install Python.
2. Save the code as `mastermind.py`.
3. Open a terminal in the project directory.
4. Run:

   ```bash
   python mastermind.py
   ```

No external libraries are required.

## How to Play

1. Choose a difficulty level.
2. Enter four color codes separated by spaces.
3. Read the feedback after each guess.
4. Continue guessing until you crack the code or run out of attempts.

Example guess:

```text
R G B Y
```

Example feedback:

```text
Correct Position: 2 | Incorrect Position: 1
```

- **Correct Position:** A color matches the secret code in both color and position.
- **Incorrect Position:** A color exists in the secret code but is in a different position.

## Learning Objectives

This project demonstrates Python skills in randomization, list processing, dictionaries, functions, loops, input validation, and duplicate-aware matching algorithms.


## Project Goal

Build problem-solving skills by implementing a code-breaking game with randomized secrets, validated user input, and logic for matching repeated colors correctly.
