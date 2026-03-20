import tkinter as tk 

root=tk.Tk() 
root.title("tkinter")
root.geometry("400x400")
root.config(bg="lightblue")

frame=tk.Label(root,bg="pink",bd=10)
frame.grid(row=0,column=0) #geometry manager

def on_button_click1():
    print("Button Clicked1!")
def button_click2():
    print("Button Clicked2!")
def button_click3():
    print("Button Clicked3!")
def button_click4():
    print("Button Clicked4!")

button1=tk.Button(root,text="Click Me",command=on_button_click1)
button1.grid(row=1,column=0)
button2=tk.Button(root,text="Click Me",command=button_click2)
button2.grid(row=1,column=1)
button3=tk.Button(root,text="Click Me",command=button_click3)
button3.grid(row=2,column=0)
button4=tk.Button(root,text="Click Me",command=button_click4)
button4.grid(row=2,column=1)

frame.config(text="Button Clicked!")

root.mainloop()#to keep window 
