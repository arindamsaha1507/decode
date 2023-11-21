"""Module to help construct long strings."""


class StringConstructor:
    """Class to help construct long strings."""

    @staticmethod
    def construct_string_contents(*args: str) -> str:
        """Construct a string from the given arguments."""
        return "\n\n".join(args)

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
