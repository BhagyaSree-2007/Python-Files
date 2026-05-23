'''Write a Python program to display the number of characters, words, vowels, lines
available in the provided file.'''
vowels = "aeiouAEIOU"
l=0
w=0
ch=0
v=0
with open('count.txt', 'r') as file:
    for line in file:
        l+= 1
        ch+= len(line)
        w+= len(line.split())
        for char in line:
            if char in vowels:
                v+=1
print("Characters:",ch)
print("Words:",w)
print("Vowels:",v)
print("Lines:",l)
