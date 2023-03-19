import tkinter as tk


class Calculator:

    expression = ''

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x330')
        self.root.resizable(False, False)
        self.root.configure(bg="#2399C9")

        self.frame = tk.Frame(self.root, width=300, height=400,
                              bg='#2399C9', highlightcolor='black')
        self.frame.grid(row=0, column=0)
        self.frame.grid_propagate(False)

        self.str_var = tk.StringVar()
        self.text = tk.Entry(self.frame, width=24, bg='#525759',
                             font=('Arial', 16, 'bold'),
                             fg='white', justify=tk.RIGHT,
                             textvariable=self.str_var)
        self.text.grid(row=0, column=0, padx=2, pady=10, sticky=tk.E + tk.W)

        self.clear = tk.Button(
            self.frame,
            text='C',
            font=('Arial', 16, 'bold'),
            bg='#044A66',
            fg='white',
            activebackground='gray',
            activeforeground='blue',
            command=self.clear_text
        )
        self.clear.grid(row=1, column=0, padx=2, pady=5, sticky=tk.E + tk.W)

        self.button_frame = tk.Frame(self.frame, width=300, height=400,
                              bg='#2399C9', highlightcolor='black')
        self.button_frame.grid(row=2, column=0)

        self.numbers_grid()
        self.root.mainloop()

    def clear_text(self):
        Calculator.expression = ''
        self.str_var.set(Calculator.expression)

    def btn_click(self, strng):
        if strng == '=':
            Calculator.expression = str(eval(Calculator.expression))
            self.str_var.set(Calculator.expression)
        else:
            Calculator.expression += strng
            self.str_var.set(Calculator.expression)

    def add_numbers(self, btn_number):
        self.btn = tk.Button(self.button_frame,
                             text=btn_number,
                             width=5,
                             height=1,
                             font=('Arial', 16),
                             bg='#044A66',
                             fg='white',
                             activebackground='gray',
                             activeforeground='blue',
                             command=lambda: self.btn_click(btn_number)
                            )
        return self.btn

    def numbers_grid(self):
        numbers = [('7', '8', '9', '*'), ('4', '5', '6', '-'), ('4', '5', '6', '-'), ('1', '2', '3', '+'),
                   ('%', '0', '/', '=')]
        for i, item in enumerate(numbers):
            for j, number in enumerate(item):
                btn = self.add_numbers(number)
                btn.grid(row=i, column=j, padx=1, pady=1)


if __name__ == '__main__':
    Calculator()