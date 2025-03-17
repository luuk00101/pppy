import doctest


def pig_latin(word):
    """
    Translates a word into Pig Latin.
    >>> pig_latin("hello")
    'ellohay'
    >>> pig_latin("world")
    'orldway'
    >>> pig_latin("apple")
    'appleway'
    >>> pig_latin("banana")
    'ananabay'
    >>> pig_latin("cherry")
    'herrycay'
    >>> pig_latin("eat")
    'eatway'
    >>> pig_latin("omelet")
    'omeletway'
    """

    if word[0].lower() in "aeiou":
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"


if __name__ == "__main__":
    doctest.testmod()
