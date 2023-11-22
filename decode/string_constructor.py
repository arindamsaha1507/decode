"""Module to help construct long strings."""


class StringConstructor:
    """Class to help construct long strings."""

    @staticmethod
    def construct_string_contents(*args: str) -> str:
        """Construct a string from the given arguments."""

        final_string = ""
        for arg in args:
            arg = StringConstructor.remove_surrounding_newlines(arg)
            final_string += arg + "\n\n"

        return StringConstructor.remove_trailing_newlines(final_string)

    @staticmethod
    def remove_trailing_newlines(string: str) -> str:
        """Remove trailing newlines from the given string."""
        return string.rstrip("\n")

    @staticmethod
    def remove_leading_newlines(string: str) -> str:
        """Remove leading newlines from the given string."""
        return string.lstrip("\n")

    @staticmethod
    def remove_surrounding_newlines(string: str) -> str:
        """Remove surrounding newlines from the given string."""
        return StringConstructor.remove_leading_newlines(
            StringConstructor.remove_trailing_newlines(string)
        )

    @staticmethod
    def find_substring(string: str, substr: str) -> int:
        """Return the index of the first occurrence of the given substring in the given string."""
        return string.find(substr)

    @staticmethod
    def trim_string(string: str, start: int, end: int) -> str:
        """Return the given string trimmed from the given start and end indices."""
        return string[start:end]

    @staticmethod
    def trim_between_substrings(string: str, start: str, end: str) -> str:
        """Return the given string trimmed between the given start and end substrings."""
        return StringConstructor.trim_string(
            string,
            StringConstructor.find_substring(string, start) + len(start),
            StringConstructor.find_substring(string, end),
        )
