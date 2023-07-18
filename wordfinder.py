from random import choice

class WordFinder:
    """
    Word Finder: finds random words from a dictionary.
    
    >>>dictionary = WordFinder(/test.txt)
    4 word(s) read

    >>>dictionary.random() in ['This', 'is', 'a', 'test']
    True

    >>>dictionary.random() in ['This', 'is', 'a', 'test']
    True

    >>>dictionary.random() in ['This', 'is', 'a', 'test']
    True
    """
    
    def __init__(self, file_path) :
        """Upon initialization, the passed file is read and its contents are broken up by word and placed in a list attribute"""
        self.words = self.read_file(file_path)
        print(f"{len(self.words)} word(s) read")

    def read_file(self, file_path) :
        """Imports and returns the read file to a list while erasing /n from content"""
        file_req = open(file_path)
        return [ word.strip() for word in file_req ]
    
    def random(self) :
        """Returns random word"""
        return choice(self.words)


class SpecialWordFinder( WordFinder ) :
    """
    A child of WordFinder that has methods capable of ignoring comments and black lines in a file. 
    
    >>>swf = SpecialWordFinder(foods.txt)
    4 word(s) read

    >>>swf.random() in ['kale','pineapple','apple','mango']
    True

    >>>swf.random() in ['kale','pineapple','apple','mango']
    True

    >>>swf.random() in ['kale','pineapple','apple','mango']
    True
    """

    def read_file( self, file_path ) :
        file_req = open( file_path )
        return [ word.strip() for word in file_req if word.strip() and not word[0] == '#' ]
