"""The main file for the project."""

from decode.ai_handler import AIHandler
from decode.file_handler import FileHandler


def main():
    """The main function for the project."""

    FileHandler.compose_files(
        ["prompt_header.txt", "equation.txt", "prompt_footer.txt"], "prompt.txt"
    )

    handler = AIHandler(
        settings_file_path="settings.txt",
        prompt_file_path="prompt.txt",
    )
    print(handler.get_completion())


if __name__ == "__main__":
    main()
