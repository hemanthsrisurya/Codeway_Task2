import tkinter as tk
from tkinter import font

def add_to_display(character):
    display.insert(tk.END, character)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Basic Calculator")
root.configure(bg='#f0f0f0')

display_font = font.Font(family='Arial', size=20)
display = tk.Entry(root, width=25, borderwidth=5, font=display_font)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('+', 4, 3), ('=', 4, 2)
]

button_font = font.Font(family='Arial', size=16, weight='bold')
for button_text, row, col in buttons:
    if button_text == 'C':
        tk.Button(root, text=button_text, padx=40, pady=20, command=clear_display, font=button_font, bg='#ffcc00').grid(row=row, column=col)
    elif button_text == '=':
        tk.Button(root, text=button_text, padx=40, pady=20, command=calculate, font=button_font, bg='#add8e6').grid(row=row, column=col)
    else:
        tk.Button(root, text=button_text, padx=40, pady=20, command=lambda char=button_text: add_to_display(char), font=button_font, bg='#99ff99').grid(row=row, column=col)

root.mainloop()
