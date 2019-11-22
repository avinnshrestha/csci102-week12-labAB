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



