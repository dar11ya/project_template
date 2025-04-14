def output_to_console(data):
    """
    Prints the given data to the console.

    Parameters:
        data (str): Text to be printed.
    """
    print("Output:")
    print(data)

def output_to_file_builtin(filename, data):
    """
    Appends the given data to a file.

    Parameters:
        filename (str): The path to the output file.
        data (str): The content to write to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(data + "\n")
