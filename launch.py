from tkinter import *
from tkinter.filedialog import askopenfilename
import runpy
import sys
import pathlib

Tk().withdraw()
filename = askopenfilename()

currentPath=pathlib.Path(__file__).parent.absolute() #current folder of launch.py
analysisPath=currentPath.joinpath('analyse.py')

sys.argv=['', '-s', filename]
runpy.run_path(analysisPath, run_name='__main__')
input()