import tkinter as tk
root =tk.Tk()
root.title("text demo")
root.geometry("400x400")

label=tk.Label(root,text="feedback:")
label.pack()

text=tk.Text(root,height=5,width=10)
text.pack()


root.mainloop()