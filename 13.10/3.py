f = open('1.txt', 'r')
newLine = []
for line in f:
    words = line.split(' ')
    for word in words:
        if(len(newLine) == 0):
            newLine.append(word)
        elif(newLine[-1] != word):
            print(word)
            print(newLine[-1])
            newLine.append(word)
newLine = " ".join(newLine)
f.close()
f = open('1.txt', 'w')
f.write(newLine)
f.close()