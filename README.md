🧠 Python Minesweeper Game with Auto-Solver
A full-featured, classic Minesweeper game built using Pygame, enhanced with a smart auto-solver!
This project replicates the strategic challenge of Minesweeper with clean object-oriented design and intelligent automation.

🎮 Features
🔲 Interactive grid-based Minesweeper game

💣 Dynamic mine generation with adjustable difficulty

🚩 Right-click flagging functionality

🧠 Auto-Solver that mimics human-like decision-making

🖼️ Graphical UI using Pygame with custom icons

🔊 Win sound effects for added fun

🛠️ Technologies Used
Python 3

Pygame — for GUI and game loop

OOP — well-structured modular code using classes like Board, Piece, Solver, and Game

🧩 Game Structure
main.py – Entry point to launch the game

game.py – Core game loop, rendering, and event handling

board.py – Minefield logic and state management

piece.py – Individual tile behavior and attributes

solver.py – Basic rule-based auto-solver

images/ – Grid tile icons (e.g., bombs, flags, numbers)

🧠 Auto Solver
Press any key to trigger the AI solver. It uses simple heuristics:

Flags cells when the number of neighboring mines equals the clue

Reveals safe cells when all adjacent bombs are flagged

This can be further expanded into a probabilistic or neural-net-based AI.

