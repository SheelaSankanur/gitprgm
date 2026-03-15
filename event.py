import tkinter as tk
root=tk.Tk()

def on_click(event):
    print(f"mouse clicked at({event.x},{event.y})")
root.title("mouse click event")
root.bind("<Button-1>",on_click)
root.mainloop()