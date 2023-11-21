"""Module for handling files."""

import os

from decode.string_constructor import StringConstructor


class FileHandler:
    """Class for handling files."""

    @staticmethod
    def read_file_contents(file_path: os.PathLike) -> str:
        """Read the contents of the given file."""
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def write_file_contents(file_path: os.PathLike, contents: str) -> None:
        """Write the given contents to the given file."""
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(contents)

    @staticmethod
    def append_file_contents(file_path: os.PathLike, contents: str) -> None:
        """Append the given contents to the given file."""
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(contents)

    @staticmethod
    def file_exists(file_path: os.PathLike) -> bool:
        """Return whether or not the given file exists."""
        return os.path.isfile(file_path)

    @staticmethod
    def get_file_extension(file_path: os.PathLike) -> str:
        """Return the extension of the given file."""
        return os.path.splitext(file_path)[1]

    @staticmethod
    def compose_files(sources: os.PathLike, target: os.PathLike) -> None:
        """Compose the contents of the source file into the target file."""

        contents: list[str] = []

        for source in sources:
            contents.append(FileHandler.read_file_contents(source))

        FileHandler.write_file_contents(
            target, StringConstructor.construct_string_contents(*contents)
        )
