# CSE-Examination

## Python GPS Tracker Program

This repository contains a simple Python program (`Jhapniel.py`) that simulates a basic GPS tracker. The program allows a user to move a virtual player on a 2D grid using text commands.

### How the Program Works

- The player starts at the origin point (0, 0).
- The user can enter movement commands to move North, South, East, or West.
- The program accepts commands in various forms, such as `N`, `n`, `North`, or `north` (similarly for other directions).
- After each valid move, the program displays the current position.
- The user can type `STOP` (case-insensitive) to end the session.
- When the session ends, the program displays the final position and indicates whether the player returned to the origin.

### Input Handling

- The program normalizes user input to handle different cases and whitespace.
- If the user enters an invalid command, the program prompts them to try again.
