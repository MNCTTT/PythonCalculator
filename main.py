import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("/", 4, 2),
    ("(", 4, 3), (")", 4, 4)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, command=lambda value=text: button_click(value))
    button.grid(row=row, column=col, sticky="nsew")
    root.grid_columnconfigure(col, weight=1)

clear_button = tk.Button(root, text="Clear", padx=20, pady=20, command=clear)
clear_button.grid(row=5, column=3, sticky="nsew")

calc_button = tk.Button(root, text="Calculate", padx=57, pady=20, command=calculate)
calc_button.grid(row=5, column=0, columnspan=3, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
