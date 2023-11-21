"""Module for handling files."""

import os


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
