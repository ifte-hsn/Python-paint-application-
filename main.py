from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab

tk = Tk()

tk.title("Painter APP")
tk.geometry("810x530")
tk.configure(background="#FFF")

text = Text(tk)
text.tag_configure("tag_name", justify='center', font=('arial', 25), background='#292826', foreground='orange')
text.insert("1.0", "Drawing Application using Python")
text.tag_add("tag_name", "1.0", "end")
text.pack()


tk.mainloop()