# Question 4 - Reverse a string
p_phrase = "was it a car or a cat I saw"
r_phrase = ""
l = len(p_phrase)
for i in range(l, 0, -1):
    r_phrase = r_phrase + p_phrase[i-1]
print(r_phrase)