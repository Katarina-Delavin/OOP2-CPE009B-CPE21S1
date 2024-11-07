import tkinter as tk

def change_color ():
    button.config(bg = 'yellow')

root = tk.Tk()
root.title("Special Midterm Exam in OOP")
root.geometry("300x300")

button = tk.Button(root, text="Click Me", command=change_color)
button.pack(expand=True)

root.mainloop()