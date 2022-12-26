"""
this app reads the text entries (username and password) and
writes them in a separate frame within the main window (root)
"""

import tkinter as tk
from tkinter import messagebox


def create_frame(root, w=None, h=None):
    if w and h:
        frame = tk.Frame(root, width=w, height=h, bg='green')
    else:
        frame = tk.Frame(root, bg='green')
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)
    return frame


def load_main_frame(frame):
    frame.tkraise()
    clear_widget(details_frame)
    user_label = tk.Label(frame, text='username', font=('Arial', 16), bg='green')
    user_label.grid(row=0, column=0, padx=10, pady=30, sticky='nsew')
    passwd_label = tk.Label(frame, text='password', font=('Arial', 16), bg='green')
    passwd_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    # entries
    user_text = tk.Entry(frame, font=('Arial', 14))
    user_text.grid(row=0, column=1, padx=10, pady=30, sticky='nsew')
    passwd_text = tk.Entry(frame, font=('Arial', 14), show='*')
    passwd_text.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    button = tk.Button(
        frame, text='Sumbit',
        font=('Arial', 14),
        bg='#A5A52A',
        activebackground='#4B4B00',
        activeforeground='white',
        command=lambda: load_details_frame(details_frame, user_text, passwd_text)
    )

    button.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')


def load_details_frame(frame, user_text, passed_text):
    frame.tkraise()
    username, passwd = get_entry_data(user_text, passed_text)
    print(username, passwd)
    i = 0
    if username and passwd:
        for item in (username, passwd):
            label = tk.Label(frame, text=item, font=('Arial', 14), bg='green')
            label.grid(padx=10, pady=10, row=i, column=1, sticky='nesw')
            i += 1
        button = tk.Button(
            frame,
            text='Back',
            font=('Arial', 14),
            bg='#A5A52A',
            activebackground='#4B4B00',
            activeforeground='white',
            command=lambda: load_main_frame(main_frame)
        )

        button.grid(row=i+1, column=1, sticky='nesw')
    else:
        load_main_frame(main_frame)
        msg = messagebox.showwarning(title='warning!!!', message='Nu ai introdus user si parola')


def get_entry_data(user_text, passwd_text):
    username = user_text.get()
    passwd = passwd_text.get()
    return username, passwd


def clear_widget(widget):
    for item in widget.winfo_children():
        item.destroy()


if __name__ == '__main__':
    root = tk.Tk()

    root.title('ReadUserDetails')
    # root.geometry('500x200')
    root.eval('tk::PlaceWindow . center')
    main_frame = create_frame(root, w=500, h=300)
    main_frame.grid(row=0, column=0)
    main_frame.grid_propagate(False)  # we do not let the child widget to modify the parent attributes

    details_frame = create_frame(root, w=500, h=300)
    details_frame.grid(row=0, column=0)
    details_frame.grid_propagate(False)

    load_main_frame(main_frame)
    # labels

    root.mainloop()
