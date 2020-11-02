import pymorphy2
import re
morth = pymorphy2.MorphAnalyzer()

FILENAME = 'text.txt'
f = open('text.txt', 'r', encoding='utf-8')

#Set file text to variable text
text = []
for line in f:
    ln = re.sub(r'[^\w\s]','',line) 
    text += ln.split(' ')
f.close()

for i in text:
    tags = []
    p  = morth.parse(i)
    for j in p:
        tags.append(str(j.tag))
    print(i,': ', ' '.join(tags))