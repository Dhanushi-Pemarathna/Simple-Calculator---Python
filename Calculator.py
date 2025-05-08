from tkinter import Tk, Entry, Button, StringVar
import math
from tkinter.font import Font

class Calculator:
    def __init__(self, master):
        master.title("Simple Calculator")
        master.geometry('350x500')
        master.configure(bg='#f0f0f0')
        master.resizable(False, False)

        # Custom font
        display_font = Font(family='Helvetica', size=24, weight='bold')
        button_font = Font(family='Helvetica', size=16, weight='bold')

        self.equation = StringVar()
        self.entry_value = ''
        
        # Display
        Entry(master, width=14, bg='#ffffff', fg='#333333', font=display_font, 
              bd=0, relief='flat', justify='right', textvariable=self.equation,
              insertwidth=0).place(x=20, y=20, height=60, width=310)
        
        # Button style parameters
        button_style = {
            'font': button_font,
            'bd': 0,
            'relief': 'flat',
            'height': 1,
            'width': 5,
            'activebackground': '#e0e0e0'
        }

        # Number buttons (light gray)
        num_style = {**button_style, 'bg': '#ffffff', 'fg': '#333333'}
        # Operator buttons (blue)
        op_style = {**button_style, 'bg': '#4285f4', 'fg': '#ffffff'}
        # Function buttons (light blue)
        func_style = {**button_style, 'bg': '#e8f0fe', 'fg': '#4285f4'}
        # Equals button (darker blue)
        eq_style = {**button_style, 'bg': '#3367d6', 'fg': '#ffffff'}
        # Clear button (red)
        clear_style = {**button_style, 'bg': '#ea4335', 'fg': '#ffffff'}

        # Button layout
        buttons = [
            # Row 1
            ('C', clear_style, 20, 100, self.clear),
            ('(', func_style, 95, 100, lambda: self.show('(')),
            (')', func_style, 170, 100, lambda: self.show(')')),
            ('⌫', func_style, 245, 100, self.backspace),
            
            # Row 2
            ('7', num_style, 20, 170, lambda: self.show(7)),
            ('8', num_style, 95, 170, lambda: self.show(8)),
            ('9', num_style, 170, 170, lambda: self.show(9)),
            ('/', op_style, 245, 170, lambda: self.show('/')),
            
            # Row 3
            ('4', num_style, 20, 240, lambda: self.show(4)),
            ('5', num_style, 95, 240, lambda: self.show(5)),
            ('6', num_style, 170, 240, lambda: self.show(6)),
            ('*', op_style, 245, 240, lambda: self.show('*')),
            
            # Row 4
            ('1', num_style, 20, 310, lambda: self.show(1)),
            ('2', num_style, 95, 310, lambda: self.show(2)),
            ('3', num_style, 170, 310, lambda: self.show(3)),
            ('-', op_style, 245, 310, lambda: self.show('-')),
            
            # Row 5
            ('0', num_style, 20, 380, lambda: self.show(0)),
            ('.', num_style, 95, 380, lambda: self.show('.')),
            ('π', func_style, 170, 380, lambda: self.show(math.pi)),
            ('+', op_style, 245, 380, lambda: self.show('+')),
            
            # Row 6
            ('√', func_style, 20, 450, self.square_root),
            ('%', func_style, 95, 450, lambda: self.show('%')),
            ('=', eq_style, 170, 450, self.solve),
        ]
        
        # Create buttons
        for text, style, x, y, command in buttons:
            Button(master, text=text, command=command, **style).place(x=x, y=y)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)
        
    def backspace(self):
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)

    def square_root(self):
        try:
            result = math.sqrt(eval(self.entry_value))
            self.entry_value = str(result)
            self.equation.set(result)
        except:
            self.equation.set("Error")

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.entry_value = str(result)
            self.equation.set(result)
        except:
            self.equation.set("Error")

root = Tk()
calculator = Calculator(root)
root.mainloop()