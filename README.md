# Tic-Tac-Toe Game
This is a simple command-line implementation of the classic Tic-Tac-Toe game in Python. The game allows two players to take turns to input their moves until there is a winner or the game ends in a draw.

## Features
- Two-player game
- Board display after each move
- Input validation for row and column entries
- Checks for winning condition
- Detects draw condition

## How to Play
1. Players take turns to enter their move.
2. The board positions are indexed from 0 to 2 for both rows and columns.
3. Input the row and column numbers when prompted.
4. The game will announce the winner or if the game ends in a draw.

## Example
```
    |    |  
-------------
    |    |  
-------------
    |    |
  
Player X, enter the row (0, 1, 2): 1
Player X, enter the column (0, 1, 2): 1

    |    |  
-------------
    | X  |  
-------------
    |    |  

Player O, enter the row (0, 1, 2): 0
Player O, enter the column (0, 1, 2): 0

O   |    |  
-------------
    | X  |  
-------------
    |    |  
```
