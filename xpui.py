# Import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox

# Varibale for window

# New window function
def window(title, bg):
    """
    Create a root window, with **title** and **bg** as arguments
    """
    global root
    root = Tk()
    root.title(title)
    root.config(bg=bg)

    return root

# Create a button
def flat_button(text, command, bg, fg, width, height):
    """
    Create a button, with no border
    text, command, bg, fg, width, height
    """
    button = Button(root, bd=0, text=text, command=command, width=width, height=height, background=bg, foreground=fg)
    button.pack()

# Test function
def run():
    root.mainloop()
