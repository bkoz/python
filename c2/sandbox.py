#
# sandbox.py
#
# Write code to find out how many lines are in the file emotion_words.txt as shown above. 
# Save this value to the variable num_lines. Do not use the len method.
baseDir='/Users/koz/src/github/python/c2/'
fileref = open(baseDir+"./emotion_words.txt","r")
num_lines = 0
if fileref:
    for aline in fileref:
        num_lines += 1
fileref.close()
print('num_lines =', num_lines)




