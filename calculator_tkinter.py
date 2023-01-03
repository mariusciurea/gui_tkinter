import tkinter as tk


class Calculator:
    expression = ''

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Calculator')
        self.root.geometry('300x390')
        self.root.resizable(0, 0)
        self.root.config(bg='#45458B')

        self.str_var = tk.StringVar()

        self.frame = tk.Frame(self.root, width=500,
                              height=100,
                              bg='#45458B',
                              highlightcolor='black')
        self.frame.pack()

        self.text = tk.Entry(self.frame, width=30, bg='#83838B',
                             font=('Arial', 16, 'bold'),
                             textvariable=self.str_var,
                             justify=tk.RIGHT)
        self.text.pack(padx=10, pady=10, fill='both')

        self.clear_button = tk.Button(self.frame,
                                      text='C',
                                      font=('Arial', 16),
                                      bg='#7F7FFF',
                                      fg='white',
                                      activebackground='#8B8B83',
                                      command=self.clear_text
                                      )
        self.clear_button.pack(padx=5, pady=5, fill='both')

        self.frame.pack_propagate(False)

        self.frame_numbers = tk.Frame(self.root,
                                      bg='black',
                                      highlightcolor='black')
        self.frame_numbers.pack(padx=5, pady=5)

        self.numbers_grid()

        self.frame_numbers.pack_propagate(False)

        self.root.mainloop()

    def clear_text(self):
        Calculator.expression = ''
        self.str_var.set(Calculator.expression)

    def btn_click(self, strng):
        if strng == '=':
            Calculator.expression = str(eval(Calculator.expression))
            self.str_var.set(str(Calculator.expression))
        else:
            Calculator.expression += strng
            self.str_var.set(Calculator.expression)

    def add_numbers(self, btn_number):
        self.btn = tk.Button(self.frame_numbers,
                             text=btn_number,
                             width=5,
                             height=2,
                             font=('Arial', 16),
                             bg='#7F7FFF',
                             fg='white',
                             activebackground='#8B8B83',
                             command=lambda: self.btn_click(btn_number)
                             )
        return self.btn

    def numbers_grid(self):
        btn = self.add_numbers('7')
        btn.grid(row=0, column=0, padx=1, pady=1)

        btn = self.add_numbers('8')
        btn.grid(row=0, column=1, padx=1, pady=1)

        btn = self.add_numbers('9')
        btn.grid(row=0, column=2, padx=1, pady=1)

        btn = self.add_numbers('*')
        btn.grid(row=0, column=3, padx=1, pady=1)

        btn = self.add_numbers('4')
        btn.grid(row=1, column=0, padx=1, pady=1)

        btn = self.add_numbers('5')
        btn.grid(row=1, column=1, padx=1, pady=1)

        btn = self.add_numbers('6')
        btn.grid(row=1, column=2, padx=1, pady=1)

        btn = self.add_numbers('-')
        btn.grid(row=1, column=3, padx=1, pady=1)

        btn = self.add_numbers('1')
        btn.grid(row=2, column=0, padx=1, pady=1)

        btn = self.add_numbers('2')
        btn.grid(row=2, column=1, padx=1, pady=1)

        btn = self.add_numbers('3')
        btn.grid(row=2, column=2, padx=1, pady=1)

        btn = self.add_numbers('+')
        btn.grid(row=2, column=3, padx=1, pady=1)

        btn = self.add_numbers('+/-')
        btn.grid(row=3, column=0, padx=1, pady=1)

        btn = self.add_numbers('0')
        btn.grid(row=3, column=1, padx=1, pady=1)

        btn = self.add_numbers('/')
        btn.grid(row=3, column=2, padx=1, pady=1)

        btn = self.add_numbers('=')
        btn.grid(row=3, column=3, padx=1, pady=1)


if __name__ == '__main__':
    Calculator()
