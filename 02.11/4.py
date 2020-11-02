import pymorphy2
morth = pymorphy2.MorphAnalyzer()

FILENAME = 'text.txt'
f = open('text.txt', 'r', encoding='utf-8')

#Set file text to variable text
text = []
for line in f:
    text += line.split(' ')
f.close()

#Normalize
for i in range(0, len(text)):
    p = morth.parse(text[i])[0]
    text[i] = p.normal_form

f = open('normalized.txt', 'w', encoding='utf-8')
f.write(" ".join(text))