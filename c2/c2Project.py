#
# Part 1 of 4.
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

#
# Part 2 of 4
#
# Define a function called get_pos which takes one parameter, a string which represents a one or 
# more sentences, and calculates how many words in the string are considered positive words. 
# Use the list, positive_words to determine what words will count as positive. 
# The function should return a positive integer - how many occurances there are of positive 
# words in the text.
#

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    """Input: A word of type string
       Returns: The string stripped of punctuation chars.
    """
    strippedWord = ""
    for c in word:
        if c in punctuation_chars:
            pass
        else:
            strippedWord = strippedWord + c
    
    return strippedWord

def get_pos(str):
    """ Input: A string of words.
        Returns: An integer that represents how many
                 positive words are contained in 
                 the input string.
    """
    numPositiveWords = 0
    # Split the string into a list then strip each
    # word of punctuation and increment the positive
    # word counter if the word is contained in the 
    # list of positive words.
    words = str.split()
    for word in words:
        strippedWord = strip_punctuation(word)
        if strippedWord in positive_words:
            numPositiveWords += 1
    return numPositiveWords
    
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

#
# Part 3 of 4
#
# Define a function called get_neg which takes one parameter, a string which represents a 
# one or more sentences, and calculates how many words in the string are c
# onsidered negative words. Use the list, negative_words to determine what words will 
# count as negative. The function should return a positive integer - how many 
# occurances there are of negative words in the text.

#
# Part 4 of 4
#
# Write code that opens the file project_twitter_data.csv which has the fake generated twitter 
# data (the text of a tweet, the number of retweets of that tweet, and the number of replies 
# to that tweet). Your task is to build a sentiment classifier, which will detect how positive 
# or negative each tweet is. Copy the code from the code windows above, and put that in the top 
# of this code window. Now, you will write code to create a csv file called resulting_data.csv, 
# which contains the Number of Retweets, Number of Replies, Positive Score (which is how many 
# happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), 
# and the Net Score (how positive or negative the text is overall) for each tweet. The file 
# should have those headers in that order.
#
# CSV output format
#
# Retweets, Number_of_Replies, Positive_Score, Negative_Score, Net_Score
