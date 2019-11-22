#Avinn Shrestha
#CSCI 102 Section A
#Week 12 Part B

#1. PrintOutPut

def PrintOutput(statement):
    print('OUTPUT', statement)
    return statement
    
#PrintOutput('Hello World')

#2. LoadFile

def LoadFile(file):
    f = open(file, 'r')
    read_lines = f.readlines()
    read_lines = list(map(lambda x:x.strip(),read_lines))
    return read_lines

#3. UpdateString

def UpdateString(string1, string2, index):
    list1 = []
    for char in string1:
        list1 += char
    list1[index] = string2
    print('OUTPUT', ''.join(list1))

#UpdateString('Hello World', 'a', 3)

#4. FindWordCount

def FindWordCount(list1, string1):
    count = 0
    list1 = (''.join(list1))
    for string in list1:
        if string == string1:
            count += 1
    print(count)
    return count

FindWordCount(['cat', 'dogcat', 'caccacc'],'c')

'''Global Variables to test'''
players = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"]
players2 = ["Melvin", "Martian", "Baka", "Xai", "Cody"]
scores = [5, 8, 10, 6, 10, 4]
''''''

#5. ScoreFinder

def ScoreFinder(list1, list2, string1): #players, scores, name
    if string1 in list1:
        place = list1.index(string1)
        score = list2[place]
        print('OUTPUT ', string1, 'got a score of ', score)
    else:
        print('OUTPUT player not found')
ScoreFinder(players,scores,'Jill')

#6. Union

def Union(list1,list2):
    list3 = list1 + list2
    print('OUTPUT', list3)
    return list3
#Union(scores,players2)

#7. Intersection

def Intersection(list1, list2):
    list3 = []
    for string in list1:
        if string in list2:
            list3.append(string)
    return list3
print('OUTPUT', Intersection(players,players2))

