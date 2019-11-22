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


