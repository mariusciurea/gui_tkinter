import tkinter as tk


def press_keys(event):
    print(event.keysym)
    print(event.send_event)


def button_press():
    top = tk.Toplevel()
    top.geometry('200x200')
    label = tk.Label(top, text='test label')
    label.pack()
    top.mainloop()


root = tk.Tk()
root.title('Login user')
root.geometry('500x300')
root.config(bg='#CDCDC0')

frame = tk.Frame(root, width=500, height=300, bg='#CDCDC0')
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.grid()

user_label = tk.Label(frame, text='username', font=('Arial', 16), bg="#CDCDC0", fg='red')
user_label.grid(row=0, column=0, ipadx=10, ipady=10, sticky=tk.W + tk.E)

user_label = tk.Label(frame, text='password', font=('Arial', 16), bg='#CDCDC0', fg='red')
user_label.grid(row=1, column=0, ipadx=10, ipady=10)

user_text = tk.Text(frame, height=1, width=20, font=('Arial', 14))
user_text.bind('<KeyPress>', press_keys) # bind an event to a handler function
user_text.grid(row=0, column=1)

user_pass = tk.Entry(frame, show='*', width=20, font=('Arial', 14))
user_pass.grid(row=1, column=1)

button = tk.Button(frame, text='Submit', command=button_press)
button.grid(row=2, column=1, sticky=tk.W + tk.E)

root.mainloop()