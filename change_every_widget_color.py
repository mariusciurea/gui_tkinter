import tkinter as tk


def change_bg(widget):
    widget['bg'] = 'blue'


if __name__ == '__main__':
    root = tk.Tk()

    frame = tk.Frame(root, height=100, width=100)
    label = tk.Label(frame, text='test', fg='red', font=('Arial', 18))
    label.pack()
    button = tk.Button(frame, text="Paint", command=lambda wgt=label: change_bg(wgt))
    # button['command'] = lambda wgt=label: change_bg(wgt)
    button.pack()
    frame.pack()

    root.mainloop()