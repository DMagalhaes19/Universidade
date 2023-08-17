class EmptyListException(Exception):
    """Executing non empty list methods on an empty list."""


class InvalidPositionException(Exception):
    """Accessing positions smaller or greater then the number of elements."""


class NoSuchElementException(Exception):
    """Reference to an element not present in the list."""


class EmptyStackException(Exception):
    """Trying to access an element in an empty stack."""


class FullStackException(Exception):
    """Trying to add an element in full stack."""


class EmptyQueueException(Exception):
    """Trying to access an element in an empty queue."""


class FullQueueException(Exception):
    """Trying to add an element in full queue."""


class DuplicatedKeyException(Exception):
    """Trying add a duplicated key to a dictionary."""


class EmptyDictionaryException(Exception):
    """Trying to access an element in an empty dictionary."""


class EmptyTreeException(Exception):
    """Trying to access an element in an empty tree."""