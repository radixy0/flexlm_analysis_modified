from tkinter import *
from tkinter.filedialog import askopenfilename
import runpy
import sys

Tk().withdraw()

filename = askopenfilename()

sys.argv=['', '-s', filename]
runpy.run_path('./analyse.py', run_name='__main__')
input()