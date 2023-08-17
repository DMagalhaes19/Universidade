class EmptyListException(Exception):
    """Executing non empty list methods on an empty list."""


class InvalidPositionException(Exception):
    """Accessing positions smaller or greater then the number of elements."""


class NoSuchElementException(Exception):
    """Reference to an element not present in the list."""


class EmptyStackException(Exception):
    """Accessing the next element from an empty stack."""


class FullStackException(Exception):
    """Trying to add elements to a full stack."""


class EmptyQueueException(Exception):
    """Accessing the next element from an empty queue."""


class FullQueueException(Exception):
    """Truing to add elements to a fill queue."""


class DuplicatedKeyException(Exception):
    """Trying to insert a pre-existing key."""


class EmptyDictionaryException(Exception):
    """Accessing content from an empty dictionary."""


class EmptyTreeException(Exception):
    """Accessing content from an empty tree."""