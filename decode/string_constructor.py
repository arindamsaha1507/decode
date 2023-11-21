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
