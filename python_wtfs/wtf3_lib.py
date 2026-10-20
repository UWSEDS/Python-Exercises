"""A module containing a class that is equal to everything."""


class Foo():
    """A class that creates objects that equal everything."""

    def __eq__(self, _):
        """Objects created from this class are equal to everything."""
        return True
