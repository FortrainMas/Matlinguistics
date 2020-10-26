FILENAME = '1.txt'
file = open(FILENAME)

def Task1(file):
    set1 = set()
    for line in file:
        elements = str(line).split()
        for i in elements:
            set1.add(i)
    print(len(set(set1)))

def Task2(file):
    seen = []
    arr = []
    for line in file:
        arr = arr + str(line).split()
    for i in arr:
        if(i in seen):
            print(i, 'YES')
        else:
            seen.append(i)
            print(i, 'NO')


def Task3(file):
    words = []
    for line in file:
        words = words + str(line).split()
    words = set(words)
    print(len(words))

Task3(file)

file.close()