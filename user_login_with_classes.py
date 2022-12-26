import tkinter as tk


class Menu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('350x155')

        self.frame = tk.Frame(self.root, width=350, height=300, bg='#CDCDC0')
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.grid()

        self.register_btn = tk.Button(self.frame, text='Register', font=('Arial', 12), command=lambda m='Register': self.press_button(m))
        self.register_btn.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W + tk.E)

        self.login_btn = tk.Button(self.frame, text='Login', font=('Arial', 12), command=lambda m='Login': self.press_button(m))
        self.login_btn.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W + tk.E)

        self.exit_btn = tk.Button(self.frame, text='Exit', font=('Arial', 12), command=exit)
        self.exit_btn.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W + tk.E)

        self.frame.pack(fill='x')

        self.root.mainloop()

    def press_button(self, m):
        if m == 'Register':
            print('Ai apasat pe Register!!!')
            self.root.destroy()
            UserRegistration()

        elif m == 'Login':
            print('Ai apasat pe Login')


class UserRegistration:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('350x155')

        self.frame = tk.Frame(self.root, width=350, height=300, bg='#CDCDC0')
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)
        self.frame.columnconfigure(5, weight=1)
        self.frame.grid()

        self.label_name = tk.Label(self.frame, text='Nume')
        self.label_name.grid(row=0, column=1, padx=10, pady=10)
        self.frame.pack(fill='x')

        self.root.mainloop()

    # def get_data(self):
    #     name = self.text_name.get('1.0', tk.END)
    #
    #     self.write_to_file('file_name', [name, user, password, email])
    #
    # def write_to_file(self, file, data):
    #     try:
    #         with open(file)
    #     except FileNotFoundError as e:
    #         pass


if __name__ == '__main__':
    menu = Menu()
