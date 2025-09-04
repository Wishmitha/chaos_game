import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import matplotlib.animation as animation
import random

class ChaosGame:
    def __init__(self):
        # --- Model/state ---
        self.vertices = [(0, 0), (1, 0), (0.5, 0.866)]  # equilateral
        self.x, self.y = random.random(), random.random()
        self.points_x, self.points_y = [], []
        self.running = False
        self.steps_per_frame = 1  # speed multiplier

        # --- Figure / axes ---
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        plt.subplots_adjust(bottom=0.2)
        self.ax.set_xlim(-0.1, 1.1)
        self.ax.set_ylim(-0.1, 1.1)
        self.ax.axis("off")

        # Static: vertices + triangle outline (optional)
        vx, vy = zip(*self.vertices)
        self.ax.scatter(vx, vy, s=50)  # triangle vertices
        self.ax.plot([vx[0], vx[1], vx[2], vx[0]],
                     [vy[0], vy[1], vy[2], vy[0]], linestyle=":")

        # Dynamic artists
        (self.points_plot,) = self.ax.plot([], [], "o", markersize=3)  # accumulated points
        (self.current_point_plot,) = self.ax.plot([], [], "o", markersize=6)  # current point
        (self.vertex_highlight,) = self.ax.plot([], [], "o", markersize=10, alpha=0.5)  # chosen vertex
        (self.line_plot,) = self.ax.plot([], [], "--", lw=1)  # dashed connector

        # Speed text
        self.speed_text = self.ax.text(
            0.02, 0.98, self._speed_label(), transform=self.ax.transAxes, va="top"
        )

        # --- Controls (buttons) ---
        ax_next = plt.axes([0.05, 0.06, 0.15, 0.08])
        ax_play = plt.axes([0.25, 0.06, 0.15, 0.08])
        ax_spup = plt.axes([0.45, 0.06, 0.15, 0.08])
        ax_spdown = plt.axes([0.65, 0.06, 0.15, 0.08])
        ax_reset = plt.axes([0.85, 0.06, 0.10, 0.08])  

        self.btn_next = Button(ax_next, "Next Step")
        self.btn_play = Button(ax_play, "Play")
        self.btn_spup = Button(ax_spup, "Speed +")
        self.btn_spdown = Button(ax_spdown, "Speed −")
        self.btn_reset = Button(ax_reset, "Reset")          

        self.btn_next.on_clicked(self.on_next)
        self.btn_play.on_clicked(self.on_play_pause)
        self.btn_spup.on_clicked(self.on_speed_up)
        self.btn_spdown.on_clicked(self.on_speed_down)
        self.btn_reset.on_clicked(self.on_reset)        

        # --- Animation loop ---
        self.ani = animation.FuncAnimation(
            self.fig, self._update, interval=40, blit=False
        )

    def _speed_label(self):
        return f"Speed: {self.steps_per_frame} step/frame"

    def step(self):
        """One chaos game iteration."""
        vx, vy = random.choice(self.vertices)

        # Show connector + chosen vertex
        self.line_plot.set_data([self.x, vx], [self.y, vy])
        self.vertex_highlight.set_data([vx], [vy])

        # Midpoint move
        self.x = (self.x + vx) / 2
        self.y = (self.y + vy) / 2

        # Log and draw point
        self.points_x.append(self.x)
        self.points_y.append(self.y)
        self.points_plot.set_data(self.points_x, self.points_y)
        self.current_point_plot.set_data([self.x], [self.y])

    # ---- Button callbacks ----
    def on_next(self, _event):
        self.step()
        self.fig.canvas.draw_idle()

    def on_play_pause(self, _event):
        self.running = not self.running
        self.btn_play.label.set_text("Pause" if self.running else "Play")

    def on_speed_up(self, _event):
        self.steps_per_frame = self.steps_per_frame * 2 if self.steps_per_frame < 64 else 64
        self.speed_text.set_text(self._speed_label())
        self.fig.canvas.draw_idle()

    def on_speed_down(self, _event):
        self.steps_per_frame = self.steps_per_frame // 2 if self.steps_per_frame > 1 else 1
        self.speed_text.set_text(self._speed_label())
        self.fig.canvas.draw_idle()

    def on_reset(self, _event): 
        # pause
        self.running = False
        self.btn_play.label.set_text("Play")
        # reset state
        self.x, self.y = random.random(), random.random()
        self.points_x, self.points_y = [], []
        # clear dynamic artists
        self.points_plot.set_data([], [])
        self.current_point_plot.set_data([], [])
        self.vertex_highlight.set_data([], [])
        self.line_plot.set_data([], [])
        # redraw
        self.fig.canvas.draw_idle()

    # ---- Animation tick ----
    def _update(self, _frame):
        if self.running:
            for _ in range(self.steps_per_frame):
                self.step()
        return (self.points_plot, self.current_point_plot,
                self.vertex_highlight, self.line_plot)

# Run it
ChaosGame()
plt.show()