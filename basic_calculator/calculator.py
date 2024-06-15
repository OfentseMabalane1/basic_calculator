import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.current_input = tk.StringVar()

    def update_input(self, number):
        current = self.current_input.get()
        self.current_input.set(current + str(number))

    def clear_input(self):
        self.current_input.set("")

    def evaluate_input(self):
        try:
            result = eval(self.current_input.get())
            self.current_input.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            self.current_input.set("")

    def get_current_input(self):
        return self.current_input
