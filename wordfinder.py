import random


class WordFinder:
    """Generate for finding random words in a file.

    >>> words in "simple.txt" are ["cat", "dog", "porcupine"]

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() 
    'cat'

    >>> wf.random() 
    'cat'

    >>> wf.random() 
    'dog'

    """

    def __init__(self, path):
        """Read the file and report # items read."""

        with open(path) as word_file:
            self.words = self.parse(word_file)
        print(f"{len(self.words)} words read")

    def parse(self, word_file):
        """Parse word_file -> list of words."""

        return [line.strip() for line in word_file]

    def random(self):
        """Return random word from file."""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.

    >>> words in "hashtagwords.txt" are:
    #veggies
    kale
    parsnips

    #fruits
    apple
    mango

    >>> swf = SpecialWordFinder("hashtagwords.txt")
    4 words read

    >>> swf.random() 
    'kale'

    >>> swf.random() 
    'mango'

    >>> swf.random() 
    'apple'
    """

    def parse(self, word_file):
        """Parse word_file -> list of words, skipping blanks/comments."""

        return [line.strip() for line in word_file if line.strip() and not line.startswith("#")]
