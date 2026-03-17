import tkinter as tk

root=tk.Tk()
root.geometry("400x400")
root.title("Scale Widget")

scale1=tk.Scale(root,from_=0,to=100,orient=tk.HORIZONTAL)
scale1.pack()
scale2=tk.Scale(root,from_=0,to=100,orient=tk.VERTICAL)
scale2.pack()

def submit():
    print("Horizontal Scale Value:",scale1.get())
    print("Vertical Scale Value:",scale2.get()) #scale1.get() and scale2.get() are used to get the value which is selected in the scale widget
button=tk.Button(root,text="Submit",command=submit).pack()

root.mainloop() 