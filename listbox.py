import tkinter as tk

root=tk.Tk()
root.geometry("400x400")
root.title("listbox demo")

listbox=tk.Listbox(root)
listbox.insert(0,"python")
listbox.insert(1,"java")
listbox.insert(2,"c++")
listbox.pack() 
    
def show(event):
    print(listbox.get(tk.ACTIVE))
        
listbox.bind("<<ListboxSelect>>",show)
root.mainloop()