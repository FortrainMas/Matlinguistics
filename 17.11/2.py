import nltk

text  = '''
Много лет прошло с тех пор,           
Когда в Союз проник раскол.
С перестройкой подло влился,
Когда занавес открылся. 
Но пришел Владимир Путин
И сказал: «Жить лучше будем!» 
'''

sentences = nltk.sent_tokenize(text)
max = ''
for sent in sentences:
    if(len(max) < len(sent)):
        max = sent

print(max)