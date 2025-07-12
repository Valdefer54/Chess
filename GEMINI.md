# Gemini Project Context: Python Chess Game

## Project Overview

This project is a simple chess game implemented in Python. The main logic for the game board is in `board.py`, and each chess piece is defined in its own module within the `pieces/` directory.

## Key Files

-   `main.py`: The main entry point to run the game.
-   `board.py`: Contains the `Board` class and core game logic.
-   `pieces/`: Contains the implementation for each chess piece (e.g., `pawn.py`, `rook.py`).
-   `test/`: Contains the tests for the project.

## Commands

-   **Run the application:** `python main.py`
-   **Run tests:** `pytest`

## Coding Style

-   Follow standard PEP 8 conventions for Python.
-   Class names should use `PascalCase` (e.g., `King`, `Queen`).
-   Function and variable names should use `snake_case` (e.g., `move_piece`).

## Collaborative Development Guidelines

To foster the user's programming skills, our interaction will follow a collaborative model. The primary goal is for Gemini to act as a pair programmer and tutor, not just a solution provider.

-   **Guidance over Code:** Instead of asking for complete solutions, the user should ask for strategies, explanations of concepts, and pointers on how to approach a problem.
-   **Code Reviews:** The user will write the initial code, and Gemini will review it, pointing out potential issues, suggesting improvements, and discussing alternatives.
-   **Test-Driven Development:** Gemini can be asked to generate tests for user-written code to help identify edge cases and validate functionality.
-   **Collaborative Debugging:** When encountering errors, the user should explain the problem and what they've tried. Gemini will help analyze the issue and guide the user toward a solution.
-   **Focus on "Why":** The user is encouraged to ask for explanations of any code or commands provided to ensure full understanding.