import pandas as pd

def input_from_console():
    """Entering text from console"""
    return input("Enter text: ")

def input_from_file_builtin(filename="data/sample.txt"):
    """Reading from a file using built-in Python tools"""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def input_from_file_pandas(filename="data/sample.txt"):
    """Reading from a file using the pandas library"""
    df = pd.read_csv(filename, header=None)
    return "\n".join(df[0].astype(str).tolist())
