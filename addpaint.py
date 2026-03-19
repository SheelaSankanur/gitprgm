import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw

root = tk.Tk()
root.title("Paint App with Save & Undo")

current_color = "black"
brush_size = 3

# Store strokes for undo
strokes = []
current_stroke = []

# Create blank image for saving
canvas_width = 500
canvas_height = 400
image = Image.new("RGB", (canvas_width, canvas_height), "white")
draw = ImageDraw.Draw(image)

# Change color
def set_color(color):
    global current_color
    current_color = color

# Start stroke
def start_paint(event):
    global current_stroke
    current_stroke = []

# Draw
def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)

    shape = canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)
    current_stroke.append(shape)

    # Draw on image also
    draw.ellipse([x1, y1, x2, y2], fill=current_color)

# End stroke
def end_paint(event):
    strokes.append(current_stroke)

# Undo last stroke
def undo():
    if strokes:
        last_stroke = strokes.pop()
        for item in last_stroke:
            canvas.delete(item)

# Save image
def save():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if file_path:
        image.save(file_path)

# UI Layout
frame = tk.Frame(root, bg="lightgray")
frame.pack(side=tk.LEFT, fill=tk.Y)

# Color buttons
colors = ["black", "red", "blue", "green", "yellow", "purple"]
for c in colors:
    tk.Button(frame, bg=c, width=3, command=lambda col=c: set_color(col)).pack(pady=5)

# Undo button
tk.Button(frame, text="Undo", command=undo).pack(pady=10)

# Save button
tk.Button(frame, text="Save", command=save).pack(pady=10)

# Canvas
canvas = tk.Canvas(root, bg="white", width=canvas_width, height=canvas_height)
canvas.pack()

# Bind mouse
canvas.bind("<Button-1>", start_paint)
canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", end_paint)

root.mainloop()