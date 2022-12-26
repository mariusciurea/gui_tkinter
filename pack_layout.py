import tkinter as tk


def print_stuff():
    print('ai apasat pe buton')
    user = user_text.get('1.0', tk.END)
    pwd = passwd_text.get()


root = tk.Tk()
root.title('User registration')
root.geometry('500x300')
# Widgets - label, text, button, checkbutton, frame, etc...
label_user = tk.Label(root, text='username', font=('Arial', 18))
label_user.pack(padx=10, pady=10)

user_text = tk.Text(root, width=20, height=1, font=('Arial', 14))
user_text.pack()

label_passwd = tk.Label(root, text='Password', font=('Arial', 18))
label_passwd.pack(padx=10, pady=10)

passwd_text = tk.Entry(root, width=20, show='*', font=('Arial', 14))
passwd_text.pack()

# atunci cand executam click pe buton se executa functia data ca valoare optiunii command
submit_button = tk.Button(root, text='Submit', font=('Arial', 18), command=print_stuff)
submit_button.pack(padx=10, pady=10)

root.mainloop()