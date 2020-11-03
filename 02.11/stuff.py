classes = {}

def doAction(string):
    main = string.split(' : ')
    if(len(main) == 1):
        addMainClasses(main[0])
    else:
        parents = main[1].split()
        addClass(main[0], {}, parents)

#Add class without parents
def addMainClasses(className):
    global classes
    classes[className] = {}

#Add class with parents >= 1 
def addClass(className, inited, parents):
    global classes
    if(len(parents) == 1):
        parent = findClass(classes, parents[0])
        parent[className] = inited
    else:
        for i in parents:
            addClass(className, inited, i)

#Find link to class by class name
def findClass(classes, className):
    if(not (classes.get(className) is None)):
        return classes[className]
    elif(len(classes) == 0):
        return None
    else:
        for i in classes.keys():
            d = findClass(classes[i], className)
            if not d is None:
                return d

def check(childrenName, parentName):
    global classes
    parent = findClass(classes, parentName)
    flag = findClass(parent, childrenName)
    if(flag is None):
        return "No"
    else:
        return "Yes"

n = int(input())
for i in range(0, n):
    str = input()
    doAction(str)
q = int(input())
for j in range(0, q):
    elements = input().split()
    print(check(elements[1], elements[0]))
