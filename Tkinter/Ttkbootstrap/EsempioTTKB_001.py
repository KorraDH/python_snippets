import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tk.Tk()

b1 = ttk.Button(root, text="Button 1", bootstyle=SUCCESS)
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO))
b2.pack(side=LEFT, padx=5, pady=10)

b3 = ttk.Button(root, text="Button 3", bootstyle=(DANGER))
b3.pack(side=LEFT, padx=5, pady=10)

b4 = ttk.Button(root, text="Button 4", bootstyle=(SUCCESS, OUTLINE))
b4.pack(side=LEFT, padx=5, pady=10)

b5 = ttk.Button(root, text="Button 5", bootstyle=(INFO, OUTLINE))
b5.pack(side=LEFT, padx=5, pady=10)

b6 = ttk.Button(root, text="Button 6", bootstyle=(DANGER, OUTLINE))
b6.pack(side=LEFT, padx=5, pady=10)

root.mainloop()
