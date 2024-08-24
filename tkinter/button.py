import tkinter as tk
import time

root = tk.Tk()

def hello():
    print("Hello welcome to my tkinter.")
def name():
    self = input("Enter your name: ")
    print(f"My name is {self}")
def current_time():
    local = time.localtime()
    print(f"The current time is {time.strftime("%H:%M:%S", local)}.")

def exit_now():
    exit()

root.title("BUttoms")
root.geometry("600x500")

frame = tk.Frame(root, bg="gray", borderwidth=5, relief="raised")
frame.pack(side="top", anchor="nw")

b1 = tk.Button(frame, fg="red", text="Click here", command=hello)
b1.pack(side="left", padx=23)
b2 = tk.Button(frame, fg="red",text="Name", command=name)
b2.pack(side="left", padx=23)
b3 = tk.Button(frame, fg="red", text="Current time", command=current_time)
b3.pack(side="left", padx=23)

b4 = tk.Button(frame, fg="red", text="exit", command=exit_now)
b4.pack(side="left", padx=23)

root.mainloop()
