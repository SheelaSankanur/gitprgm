import tkinter as tk

root=tk.Tk()
root.title("Toolbar")
root.geometry("400x200")

def open_str():
    print("open button clicked")

def close_str():
    print(" save button clicked")

def copy():
    print("copy clicked")

def pause():
    print("pause clicked")

#create toolbar using frame
toolbar=tk.Frame(root,bg="lightblue")
toolbar.pack(side=tk.TOP,fill=tk.X)

btn_open = tk.Button(toolbar, text="Open", command=open_str)
btn_open.pack(side=tk.LEFT, padx=2, pady=2)

btn_save = tk.Button(toolbar, text="Save", command=close_str)
btn_save.pack(side=tk.LEFT, padx=2, pady=2)

btn_copy = tk.Button(toolbar, text="Copy", command=copy)
btn_copy.pack(side=tk.LEFT, padx=2, pady=2)

btn_pause = tk.Button(toolbar, text="Pause", command=pause)
btn_pause.pack(side=tk.LEFT, padx=2, pady=2)
root.mainloop()