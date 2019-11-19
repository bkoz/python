#
# To start, define a function called strip_punctuation which takes one parameter, a 
# string which represents a word, and removes characters considered punctuation 
# from everywhere in the word. 
#

import string

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word):
    """Strips punctuation from the given word"""
    strippedWord = ""
    for c in word:
        if c in punctuation_chars:
            pass
        else:
            strippedWord = strippedWord + c
    
    return strippedWord




