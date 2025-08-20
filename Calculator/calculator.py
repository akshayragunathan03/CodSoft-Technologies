import tkinter as tk
from tkinter import font

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("400x600")  # Larger window size
root.resizable(False, False)
root.configure(bg='#f0f0f0')

# Custom fonts
display_font = font.Font(size=28)
button_font = font.Font(size=18, weight='bold')

# Display
display = tk.Entry(root, width=12, font=display_font, borderwidth=4, 
                  justify="right", bg='#ffffff', fg='#333333')
display.grid(row=0, column=0, columnspan=4, padx=15, pady=20, ipady=15)

# Button layout
buttons = [
    ('7', '#f5f5f5'), ('8', '#f5f5f5'), ('9', '#f5f5f5'), ('/', '#e6e6e6'),
    ('4', '#f5f5f5'), ('5', '#f5f5f5'), ('6', '#f5f5f5'), ('*', '#e6e6e6'),
    ('1', '#f5f5f5'), ('2', '#f5f5f5'), ('3', '#f5f5f5'), ('-', '#e6e6e6'),
    ('0', '#f5f5f5'), ('C', '#ff9999'), ('=', '#ffcc99'), ('+', '#e6e6e6')
]

# Create and position buttons
row_val = 1
col_val = 0

for (button, color) in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, padx=25, pady=25, font=button_font,
                      command=button_equal, bg=color, activebackground='#ff9933')
        btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    elif button == 'C':
        btn = tk.Button(root, text=button, padx=25, pady=25, font=button_font,
                      command=button_clear, bg=color, activebackground='#ff6666')
        btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    else:
        btn = tk.Button(root, text=button, padx=25, pady=25, font=button_font,
                      command=lambda b=button: button_click(b), bg=color,
                      activebackground='#d9d9d9')
        btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure grid weights to make buttons expand
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Run the application
root.mainloop()