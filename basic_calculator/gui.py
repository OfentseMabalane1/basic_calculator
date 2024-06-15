import tkinter as tk
from basic_calculator.calculator import Calculator

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")
        self.root.configure(bg="black")  # Set background color of the window
        self.calculator = Calculator()
        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        # Configure grid weights to make widgets expand with the window
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

        # Input field
        input_field = tk.Entry(self.root, textvariable=self.calculator.get_current_input(), font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, bg="black", fg="#FFDB58")
        input_field.grid(row=0, column=0, columnspan=4, sticky="nsew")
        
        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        for button in buttons:
            action = lambda x=button: self.calculator.update_input(x) if x != "=" else self.calculator.evaluate_input()
            tk.Button(self.root, text=button, font=("Arial", 18), command=action, bg="#FFDB58", fg="black").grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Clear button
        tk.Button(self.root, text='C', font=("Arial", 18), command=self.calculator.clear_input, bg="#FFDB58", fg="black").grid(row=row, column=col, sticky="nsew")

    def bind_keys(self):
        self.root.bind('<Return>', lambda event: self.calculator.evaluate_input())
        self.root.bind('<BackSpace>', lambda event: self.calculator.clear_input())
        for key in '0123456789':
            self.root.bind(key, lambda event, digit=key: self.calculator.update_input(digit))
        for key in '/*-+':
            self.root.bind(key, lambda event, operator=key: self.calculator.update_input(operator))
        self.root.bind('.', lambda event: self.calculator.update_input('.'))

if __name__ == "__main__":
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()
