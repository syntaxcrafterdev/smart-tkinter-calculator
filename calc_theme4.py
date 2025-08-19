import tkinter as tk
from tkinter import messagebox
import math

class ThemedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator - Green + Aqua Theme")
        self.root.geometry("360x500")
        self.root.resizable(False, False)
        self.expression = ""

        # Colors - Green + Aqua theme
        self.bg_color = "#0a2e0a"    # Dark green background
        self.btn_color = "#1a5c1a"   # Medium green for buttons
        self.btn_text = "#ffffff"    # White text
        self.ac_color = "#00e6e6"    # Aqua for AC
        self.eq_color = "#00e6e6"    # Aqua for =

        self.root.configure(bg=self.bg_color)

        # Display
        self.entry = tk.Entry(root, font=("Consolas", 24), bg=self.bg_color,
                            fg="white", insertbackground="white", relief="flat", justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # Buttons layout
        buttons = [
            ["AC", "(", ")", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "√", "="]
        ]

        for row in buttons:
            frame = tk.Frame(root, bg=self.bg_color)
            frame.pack(expand=True, fill="both")
            for char in row:
                if char == "AC":
                    b = tk.Button(frame, text=char, font=("Segoe UI", 14, "bold"),
                                bg=self.ac_color, fg="black", relief="flat",
                                command=lambda ch=char: self.on_click(ch))
                elif char == "=":
                    b = tk.Button(frame, text=char, font=("Segoe UI", 14, "bold"),
                                bg=self.eq_color, fg="black", relief="flat",
                                command=self.calculate)
                else:
                    b = tk.Button(frame, text=char, font=("Segoe UI", 14, "bold"),
                                bg=self.btn_color, fg=self.btn_text, relief="flat",
                                command=lambda ch=char: self.on_click(ch))
                b.pack(side="left", expand=True, fill="both", padx=3, pady=3)

        # Keyboard binding
        self.root.bind("<Key>", self.key_input)

    def on_click(self, char):
        if char == "AC":
            self.expression = ""
            self.entry.delete(0, tk.END)
        elif char == "√":
            self.expression += "math.sqrt("
            self.entry.insert(tk.END, "√(")
        else:
            self.expression += str(char)
            self.entry.insert(tk.END, str(char))

    def calculate(self):
        try:
            result = str(eval(self.expression, {"__builtins__": None}, {"math": math}))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
            self.expression = result
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.expression = ""
            self.entry.delete(0, tk.END)

    def key_input(self, event):
        if event.keysym == "Return":
            self.calculate()
        elif event.keysym == "BackSpace":
            self.expression = self.expression[:-1]
            self.entry.delete(len(self.entry.get())-1, tk.END)
        elif event.char in "0123456789+-*/().":
            self.expression += event.char
            self.entry.insert(tk.END, event.char)


if __name__ == "__main__":
    root = tk.Tk()
    app = ThemedCalculator(root)
    root.mainloop()
