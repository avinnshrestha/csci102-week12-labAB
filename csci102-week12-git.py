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

