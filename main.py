from app.io.input import input_from_console, input_from_file_builtin, input_from_file_pandas
from app.io.output import output_to_console, output_to_file_builtin

def main():
    text_console = input_from_console()
    text_builtin = input_from_file_builtin("data/sample.txt")
    text_pandas = input_from_file_pandas("data/sample.txt")

    output_to_console(text_console)
    output_to_console(text_builtin)
    output_to_console(text_pandas)

    output_to_file_builtin("data/output.txt", text_console)
    output_to_file_builtin("data/output.txt", text_builtin)
    output_to_file_builtin("data/output.txt", text_pandas)

if __name__ == "__main__":
    main()
