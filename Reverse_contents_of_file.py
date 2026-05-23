'''Write a python program that reverses the contents of a text file (character by
character) and writes the reversed text into another file.'''
with open('inp.txt', 'r') as infile:
    data = infile.read()
reverse = ""
index = len(data) - 1
while index >= 0:
    reverse += data[index]
    index -= 1
with open('outp.txt', 'w') as outfile:
    outfile.write(reverse)
