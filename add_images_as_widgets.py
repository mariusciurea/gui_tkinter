import tkinter as tk
from PIL import ImageTk

root = tk.Tk()
root.geometry('700x500')
frame = tk.Frame(root, width=700, height=500, bg='yellow')
frame.grid()

label = tk.Label(frame, text='image', fg='black', font=('Arial', 18), bg='yellow')
label.pack()

# adaugarea unei imagini pe un label din cadrul frame-ului
image = ImageTk.PhotoImage(file='logo.png')
label_image = tk.Label(frame, image=image, bg='yellow')
label_image.image = image
label_image.pack()

frame.pack_propagate(False)
root.mainloop()
