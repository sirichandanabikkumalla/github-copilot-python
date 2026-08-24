---
applyTo: "**"
description: "Workspace-wide coding guidance for the Sudoku Flask app."
---

# General Standards

- Write clean, modular, and maintainable code.
- Refactor legacy code into reusable functions.
- Keep functions small and focused.
- Follow Python best practices (PEP 8).
- Use descriptive variable and function names.

# Flask

- Keep routes simple.
- Separate game logic from UI logic.
- Avoid duplicate code.

# Error Handling

- Handle invalid input gracefully.
- Add meaningful error messages.
- Never crash on user input.

# Sudoku Rules

- Ensure every generated puzzle has exactly one solution.
- Lock prefilled cells.
- Validate every move.
- Keep puzzle generation efficient.

# Frontend

- Use responsive CSS.
- Alternate colors for each 3×3 box.
- Support Light and Dark mode.
- Keep UI clean and readable.

# JavaScript

- Use modern ES6+ syntax.
- Keep functions modular.
- Avoid global variables.

# Testing

- Generate pytest tests.
- Never remove existing tests.
- Explain every generated test.

# Comments

- Add comments only where they improve readability.
- Avoid unnecessary comments.

# Copilot

- Explain major architectural decisions before generating large code changes.
- Prefer incremental changes over rewriting the whole project.
