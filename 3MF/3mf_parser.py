import stl
from tkinter import *
from tkinter import filedialog

path = filedialog.askopenfilename(title="Select a 3MF file", filetypes=[("3MF files", "*.3mf")])
print(path)
mesh = stl.mesh.Mesh.from_file(f"{path}")
