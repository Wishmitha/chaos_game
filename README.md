# Chaos Game — Sierpiński Triangle (Python + Matplotlib)

Interactive, step-by-step visualization of the **Chaos Game** that generates the **Sierpiński triangle**.  
Includes controls to **Next Step**, **Play/Pause**, **Faster**, and **Slower**, while showing the **selected vertex**, **dashed connector**, and **midpoint** each step.

---

## Preview

<!-- Placeholder: Add your simulation GIF here -->

![Chaos Game Simulation](docs/simulation.gif)
_(Add your simulation GIF at `docs/simulation.gif` or update the path above)_

---

## Features

- Draws the fractal **one step at a time** (great for teaching/learning).
- Highlights the **chosen vertex** and the **dashed line** to the current point.
- **Controls**:
  - **Next Step** — single iteration.
  - **Play/Pause** — toggle continuous animation.
  - **Faster** — increases speed (reduces delay and then ups steps/frame).
  - **Slower** — decreases speed (reduces steps/frame, then increases delay).
- Clean, dependency-light setup with **Pipenv**.

---

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

## Usage

1. **Launch the application** using the installation steps above.
2. **Use the controls** at the bottom of the window:
   - **Next Step**: Click to advance one iteration at a time
   - **Play/Pause**: Toggle continuous animation
   - **Speed +**: Increase animation speed (1→2→4→8→16→32→64 steps/frame)
   - **Speed −**: Decrease animation speed (64→32→16→8→4→2→1 steps/frame)
3. **Watch the visualization**:
   - **Blue dots**: Accumulated points forming the Sierpiński triangle
   - **Large orange dot**: Current point position
   - **Highlighted vertex**: Randomly chosen vertex for each step
   - **Dashed line**: Connection from current point to chosen vertex

---

## How It Works

The **Chaos Game** is a method for generating fractals using a simple set of rules:

1. **Start** with any point inside an equilateral triangle
2. **Choose** one of the three vertices randomly
3. **Move** halfway toward the chosen vertex
4. **Mark** the new position
5. **Repeat** steps 2-4 many times

**Mathematically**: If the current point is at `(x, y)` and the chosen vertex is at `(vx, vy)`, the new point becomes:

```
new_x = (x + vx) / 2
new_y = (y + vy) / 2
```

After thousands of iterations, the points form the **Sierpiński triangle** - a self-similar fractal with infinite detail at every scale.

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

## Troubleshooting

**Common issues:**

- **"No module named 'matplotlib'"**: Run `pipenv install --ignore-pipfile`
- **Python version error**: Ensure you're using Python 3.12 or compatible version
- **Display issues**: Some systems may need additional setup for matplotlib GUI backends

**For headless servers**: Add this before `plt.show()`:

```python
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
```

---

## License

This project is open source. Feel free to use, modify, and distribute as needed.
