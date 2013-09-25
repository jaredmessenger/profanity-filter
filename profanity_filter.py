"""
Uses a line separated file listing bad words as it's source
to check if a user submitted something inappropriate

f = Filter('slut', clean_word='unicorn')
word = f.clean()
print word
>>slut
"""
import re

class Filter(object):
    """
    Replaces a bad word in a string with something more PG friendly
    
    Filter('you annoying prick', 'unicorn')
    
    """
    def __init__(self, original_string, clean_word='****'):
        
        bad_words_file = open('bad_words.txt', 'r')
        
        self.bad_words = set(line.strip('\n') for line in open('bad_words.txt'))
        self.original_string = original_string
        self.clean_word = clean_word
        
    def clean(self):
        exp = '(%s)' %'|'.join(self.bad_words)
        r = re.compile(exp, re.IGNORECASE)
        return r.sub(self.clean_word, self.original_string)
