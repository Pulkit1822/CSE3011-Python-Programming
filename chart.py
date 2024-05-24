import tkinter as tk

# Sample data for the bar chart (you can replace this with user-provided data)
data = [("Minecraft", 238), ("G.Theft Auto V", 185), ("Tetris (EA)", 100), ("Wii Sports", 82.9), ("PUBG", 75)]

# Constants for chart dimensions
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
BAR_WIDTH = 55
BAR_SPACING = 20
CHART_TOP_MARGIN = 30

def draw_bar_chart(canvas, data):
    max_value = max(data, key=lambda item: item[1])[1]

    # Calculate scaling factor to fit data within the canvas
    scale = (CANVAS_HEIGHT - CHART_TOP_MARGIN) / max_value

    x = BAR_SPACING

    for category, value in data:
        bar_height = value * scale
        canvas.create_rectangle(
            x, CANVAS_HEIGHT - bar_height, x + BAR_WIDTH, CANVAS_HEIGHT,
            fill="blue", outline="black"
        )
        canvas.create_text(
            x + BAR_WIDTH // 2, CANVAS_HEIGHT - bar_height - 10, text=category
        )
        x += BAR_WIDTH + BAR_SPACING

root = tk.Tk()
root.title("5 best-selling video games")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# Draw the bar chart on the canvas
draw_bar_chart(canvas, data)

root.mainloop()
