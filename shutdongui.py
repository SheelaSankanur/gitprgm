import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.title("Shutdown GUI")
root.geometry("400x250")
root.configure(bg="lightgray")

def shutdown():
    if messagebox.askokcancel("Shutdown", "Are you sure you want to shutdown?"):
        os.system("shutdown /s /t 1")
def restart():
    if messagebox.askokcancel("Restart", "Are you sure you want to restart?"):
        os.system("shutdown /r /t 1")
def logout():
    if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
        os.system("shutdown /l") 
def cancel():
    if messagebox.askokcancel("Cancel Shutdown", "Are you sure you want to cancel the shutdown?"):
        os.system("shutdown /a")

title=tk.Label(root, text="Shutdown GUI", font=("Arial", 16), bg="gray")
title.pack(pady=10)

shutdown_button=tk.Button(root, text="Shutdown", command=shutdown, width=15)
shutdown_button.pack(pady=5)

restart_button=tk.Button(root, text="Restart", command=restart, width=15)
restart_button.pack(pady=5)

logout_button=tk.Button(root, text="Logout", command=logout, width=15)
logout_button.pack(pady=5)

cancel_button=tk.Button(root, text="Cancel Shutdown", command=cancel, width=15)
cancel_button.pack(pady=5)

root.mainloop()    