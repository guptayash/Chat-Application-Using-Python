from cx_Freeze import setup, Executable

setup(name='QuickFi',
      version='0.1',
      description='Chat Application',
      executables=[Executable("QuickFi.py")])
