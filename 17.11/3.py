import nltk

text  = '''
Слова глубокие и осмысленные. Слова. Я люблю Cлова.
Брух. Что-то со словами. Брух
'''

words = nltk.word_tokenize(text)

smth = nltk.FreqDist(words).most_common(3)

print(smth)