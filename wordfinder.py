"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    """ Finds random words from a provided file 
    >>> wf = WordFinder("words.txt")
    235886 words read
    >>> wf.random() in wf.already_read_in
    True
    >>> wf.random() in wf.already_read_in
    True
    """
    def __init__(self, path):
        self.path = path
        self.already_read_in = []
        self.already_read_in = self.read_file()
        num_of_words = len(self.already_read_in)
        print(f"{num_of_words} words read")

    def read_file(self):
        file = open(self.path,'r')
        for line in file:
            self.already_read_in.append(line.strip())
            
        file.close()
        return self.already_read_in

    def random(self):
        """ Returns a random word from that list of words in the file """
        return choice(self.already_read_in)

class SpecialWordFinder(WordFinder):
    """ Finds random words from a provided file 
        Ignore the blank lines
        Ignore the comment lines start with '#'

    >>> swf = SpecialWordFinder("foods.txt")
    4 words read
    >>> swf.random() in swf.already_read_in
    True
    >>> swf.random() in swf.already_read_in
    True
    >>> swf.random() != ''
    True
    >>> '#' not in swf.random()
    True
    """

    def read_file(self):
        file = open(self.path,'r')
        for line in file:
            if (not line.strip() == "") and (not '#' in line):
                self.already_read_in.append(line.strip())
            
        file.close()
        return self.already_read_in