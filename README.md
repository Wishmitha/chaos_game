# Chaos Game — Sierpiński Triangle (Python + Matplotlib)

Interactive, step-by-step visualization of the **Chaos Game** that generates the **Sierpiński triangle**.  
Includes controls to **Next Step**, **Play/Pause**, **Faster**, and **Slower**, while showing the **selected vertex**, **dashed connector**, and **midpoint** each step.

---

## Preview

<!-- Placeholder: Add your simulation GIF here -->

![Chaos Game Simulation](docs/simulation.gif)


## Requirements

- **Python 3.12**
- **Pipenv** (`pip install pipenv`)

---

## Installation

1. **Install Pipenv** (if not already installed):

   ```bash
   pip install pipenv
   ```

2. **Install dependencies using Pipfile.lock**:

   ```bash
   pipenv install --ignore-pipfile
   ```

3. **Run the application**:

   ```bash
   pipenv run python run.py
   ```

---

## Project Structure

```
chaos_game/
├── README.md          # This file
├── run.py            # Main application
├── Pipfile           # Pipenv dependencies
├── Pipfile.lock      # Locked dependency versions
└── docs/             # Documentation (create this folder)
    └── simulation.gif  # Simulation animation (add your own)
```

---
