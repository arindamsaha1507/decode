"""The main file for the project."""

from decode.ai_handler import AIHandler
from decode.file_handler import FileHandler
from decode.string_constructor import StringConstructor


def main():
    """The main function for the project."""

    header = FileHandler.read_file_contents("prompt_header.txt")
    equation = FileHandler.read_file_contents("equation.txt")
    footer = FileHandler.read_file_contents("prompt_footer.txt")

    prompt = StringConstructor.construct_string_contents(header, equation, footer)

    FileHandler.write_file_contents("prompt.txt", prompt)

    handler = AIHandler(
        settings_file_path="settings.txt",
        prompt_file_path="prompt.txt",
    )
    print(handler.get_completion())


if __name__ == "__main__":
    main()
