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

# Write to a file.
filename = "squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
# Read 10 chars including '\n'
print(infile.read()[:10])

fname = "squared_numbers.txt"
with open(fname, 'r') as fileref:         # step 1
    for lin in lines:                     # step 2

