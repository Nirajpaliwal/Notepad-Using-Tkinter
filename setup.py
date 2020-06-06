import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

# os.environ['TCL_LIBRARY'] = r"C:\Users\Admin\AppData\Local\Programs\Python\Python37\tcl\tcl8.6"
# os.environ['TK_LIBRARY'] = r"C:\Users\Admin\AppData\Local\Programs\Python\Python37\tcl\tk8.6"

executables = [cx_Freeze.Executable("npad.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "Text Editor By Neeraj",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'icons2']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
