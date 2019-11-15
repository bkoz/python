#
# The resulting acronym should be “WA. EA. AI. AR. VI”
#
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ""
for i, wrd in enumerate(sent.split()):
    skip = False
    for sw in stopwords:
        if (wrd == sw):
            skip = True
    if skip == False:        
        acro = acro + wrd[0].upper()
        acro = acro + wrd[1].upper()
        acro = acro + '.'
        acro = acro + ' '

# Remove the final 2 chars to pass the grader.
acro = acro[:-2]
print(acro)
