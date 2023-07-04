from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab

tk = Tk()

tk.title("Painter APP")
tk.geometry("810x530")
tk.configure(background="#FFF")

pointer = "black"
erase = "white"


text = Text(tk)
text.tag_configure("tag_name", justify='center', font=('arial', 25), background='#292826', foreground='orange')
text.insert("1.0", "Drawing Application using Python")
text.tag_add("tag_name", "1.0", "end")
text.pack()

# Pick a color for drawing from color pannel
pick_color = LabelFrame(tk, text="Colors", font=('arial',15),bd=5, relief=RIDGE, bg="white")
pick_color.place(x=0, y=40, width=90, height=185)
colors = ["blue", "red", "green", "orange", "violet", "black", "yellow", "purple", "pink", "gold", "brown", "indigo"]






tk.mainloop()