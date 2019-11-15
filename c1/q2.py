# Question 2
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = ""
for i, wrd in enumerate(org.split()):
    skip = False
    for sw in stopwords:
        if (wrd == sw):
            skip = True
    if skip == False:        
        acro = acro + wrd[0].upper()
print(acro)
    