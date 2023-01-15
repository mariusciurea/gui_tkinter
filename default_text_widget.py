import tkinter as tk


def delete_text(event):
    global text_deleted
    print(event)
    if not text_deleted:
        text_deleted = True
        text.delete(0, tk.END)



root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)

text = tk.Entry(root, width=40, font=('Arial', 16), justify=tk.RIGHT)
text.pack(padx=10, pady=10)
text.insert(0, 'email')
text_deleted = False
text.bind('<KeyPress>', lambda text_deleted: delete_text(text_deleted))


root.mainloop()