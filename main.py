"""The main file for the project."""

import decode.ai_handler as ai_handler


def main():
    """The main function for the project."""
    handler = ai_handler.AIHandler(
        settings_file_path="settings.txt",
        prompt_file_path="prompt.txt",
    )
    print(handler.get_completion())


if __name__ == "__main__":
    main()
