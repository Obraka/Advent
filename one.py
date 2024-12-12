import os	
listone = []
listtwo = []

def read_file():
    file_path = 'C:\\Users\\rodle\\source\\repos\\Advent\\list'
    file = open(file_path, 'r')
	
    values = file.read()
    file.close()
    return values

def splitter(input):
    for line in input.splitlines():
       tmp =  line.split('   ')
       listone.append(tmp[0])
       listtwo.append(tmp[1])
       del tmp

def diffcalc():
    result = 0
    for i in range(len(listone)):
        if (listone[i] > listtwo[i]):
            result = result+int(listone[i])-int(listtwo[i])
        else:
            result = result+int(listtwo[i])-int(listone[i])
    
    return result

def simcalc():
    result = 0
    for i in range(len(listone)):
        qty = listtwo.count(listone[i])
        result = result+(int(listone[i])*qty)
    
    print(result)

def one():
    raw = read_file()
    splitter(raw)
    listone.sort()
    listtwo.sort()
    print("Difference Score: ")
    print(diffcalc())
    print("Similarity Score: ")
    print(simcalc())
    
one()