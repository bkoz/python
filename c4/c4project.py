name = 'Lilly'
prizeMoney = 99
category = 'category' 
obscured_phrase = 'obscured_phrase'
guessed = 'guessed'
prompt = """
{} has ${}

Category: {} \

Phrase:  {} \

Guessed: {} \


Guess a letter, phrase, or type 'exit' or 'pass': \
""".format(name, prizeMoney, category, obscured_phrase, guessed)

#print(prompt)
#move = input(prompt)
#print('move =', move)        

letters = 'abcde'
c = 'f'

print(c not in letters)