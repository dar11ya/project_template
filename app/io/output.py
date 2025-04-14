def output_to_console(data):
    """Outputting text to the console"""
    print("Result:")
    print(data)

def output_to_file_builtin(data):
    """Writing to a file using built-in Python tools"""
    with open("data/sample.txt", "a", encoding="utf-8") as file:
        file.write(data + "\n")
