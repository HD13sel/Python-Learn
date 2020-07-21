from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("autoformulav1.py", base=base)]

packages = ["tkinter"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Auto Formula M1",
    options = options,
    version = "1.0",
    description = 'Auto Fórmula Maquinário 1',
    executables = executables
)