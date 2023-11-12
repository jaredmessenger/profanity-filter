"""
Uses a line separated file listing bad words as it's source
to check if a user submitted something inappropriate.
Code modified from: https://github.com/jared-mess/profanity-filter

Modified by: Jeremy Becnel
Date 1/2/2016

Example of Code in test_profanity_filter.py

Example Output---
Original:
Cassandra is a fuCking piece of shit_on_a_long_stick
Output from clean_anywhere:
CHAPPYandra is a HAPPYing piece of HAPPY_on_a_long_stick
Output from clean_start:
Cassandra is a HAPPYing piece of HAPPY_on_a_long_stick
Output from clean whole word:
Cassandra is a HAPPY piece of shit_on_a_long_stick
"""
import re

# bad word file location and and name
badwordfile = 'bad_words.txt'


class Filter(object):
    """
    Class is desigend to take a string and clean it up by replacing 
    instances of "bad" words with a more acceptable word.
    
    """

    # class variable containing all the bad words we are looking for
    bad_words = set(line.strip('\n') for line in open(badwordfile))

    def __init__(self, original_string, replacement_string='****'):
        
        #cls.bad_words = ['ass','fuck', 'shit' ] # used for testing
        self.original_string = original_string
        self.replacement_string = replacement_string
        self.profanity_found = None
        self.__has_been_cleaned = False
        self.clean_string = None

#===================================INSTANCE METHODS

#---------------------------standard get set methods with some error checking

    def get_original_string(self):
        return self.original_string

    def get_replacement_string(self):
        return self.replacement_string

    def is_profanity_found(self):
        # check to see if a cleaning has been performed.
        assert (self.__has_been_cleaned), "Word must be cleaned before this can be determined."
        # after a clean is performed this method can be used to to determine if 
        # profanity was found
        return self.profanity_found

    def get_clean_string(self):
        # check to see if a cleaning has been performed.        
        assert (self.__has_been_cleaned), "Word must be cleaned before a clean string can be returned."
        # after a clean is performed this method can be used to to determine if 
        # profanity was found
        return self.clean_string

#------------------------------cleaners

# The methods below are instance methods that cleans the given string according 
# to different rules. 

    def __clean(self,exp):
        r = re.compile(exp, re.IGNORECASE)
        # check for any profanity in the string
        self.profanity_found = (r.search(self.original_string) != None)
        # return the original string where the replacements string has been substituted for the profanity
        self.clean_string = r.sub(self.replacement_string, self.original_string)
        self.__has_been_cleaned = True        
        return self.clean_string

    # cleans profanity found anywhere in the word
    # example with #cls.bad_words = ['ass','fuck', 'shit' ] # used for testing:
    # cleans "Cassandra Fuck Off you shithead"
    # as 'C****andra **** Off you ****head'
    def clean_anywhere(self):
        exp = '(%s)' %'|'.join(Filter.bad_words)        
        return self.__clean(exp)


    # requires blank at beginning and end of word, i.e. word must start with profanity
    # example with #cls.bad_words = ['ass','fuck', 'shit' ] # used for testing:
    # cleans "Cassandra Fuck Off you shithead"
    # as 'Cassandra **** Off you ****head'
    def clean_start(self):
        exp = '(\\b%s)' %'|\\b'.join(Filter.bad_words)
        return self.__clean(exp)

    
    # requires blank at beginning and end of word, i.e. will match whole word only
    # example with #cls.bad_words = ['ass','fuck', 'shit' ] # used for testing:
    # cleans "Cassandra Fuck Off you shithead"
    # as 'Cassandra **** Off you shithead'
    def clean_whole_word(self):
        exp = '(\\b%s\\b)' %'\\b|\\b'.join(Filter.bad_words)
        return self.__clean(exp)

