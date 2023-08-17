class EmptyListException(Exception):
    pass
    """Executing non empty list methods on an empty list."""


class InvalidPositionException(Exception):
    pass
    """Accessing positions smaller or greater then the number of elements."""


class NoSuchElementException(Exception):
    pass
    """Reference to an element not present in the list."""