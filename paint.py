import tkinter as tk

root=tk.Tk()
root.title("simple paint app")

current_color="black"

def set_color(color):
    global current_color
    current_color=color

def paint(event):
    x1,y1=(event.x-2),(event.y-2)
    x2,y2=(event.x+2),(event.y+2)
    canvas.create_oval(x1,y1,x2,y2,fill=current_color,outline=current_color)

color_frame=tk.Frame(root,bg="lightblue")
color_frame.pack(side=tk.LEFT,fill=tk.Y)

colors=["black","red","green","yellow","purple","orange","pink"]

for color in colors:
    btn=tk.Button(color_frame,bg=color,width=3,command=lambda c=color:set_color(c))
    btn.pack(pady=5)

# Create canvas
canvas = tk.Canvas(root, bg="white", width=500, height=400)
canvas.pack(side=tk.RIGHT)

# Bind mouse movement to paint
canvas.bind("<B1-Motion>", paint)

root.mainloop()