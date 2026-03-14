from secrets import choice
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x400")
root.title("radio button")

choice=tk.IntVar()
radio1=tk.Radiobutton(root,text="Accept terms",variable=choice,value=1).pack()
radio2=tk.Radiobutton(root,text="Accept conditions",variable=choice,value=2).pack()
radio3=tk.Radiobutton(root,text="Accept privacy policy",variable=choice,value=3).pack()

def submit():
    selected=choice.get()
    if selected==1:
        print("accept terms")
    elif selected==2:
        print("accept conditions")
    elif selected==3:
        print("accept privacy policy")
    
    print(choice.get())
    print("submitted")

button=tk.Button(root,text="submit",command=submit).pack()

root.mainloop()