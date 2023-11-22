"""The main file for the project."""

import subprocess

from decode.ai_handler import AIHandler
from decode.file_handler import FileHandler
from decode.string_constructor import StringConstructor


def main():
    """The main function for the project."""

    FileHandler.compose_files(
        ["prompt_header.txt", "equation.txt", "prompt_footer.txt"], "prompt.txt"
    )

    handler = AIHandler(
        settings_file_path="settings.txt",
        prompt_file_path="prompt.txt",
    )
    response = handler.get_completion()

    code = StringConstructor.trim_between_substrings(response, "```python\n", "```\n")
    code = code.replace("`", "")

    print(response)

    FileHandler.write_file_contents("ode_code.py", code)

    FileHandler.compose_files(["ode_header.txt", "ode_code.py"], "ode_code.py")

    subprocess.run(["black", "ode_code.py"], check=True)


if __name__ == "__main__":
    main()
