import os
import re

def read_file():
    file_path = 'C:\\Users\\rodle\\source\\repos\\Advent\\input3'
    file = open(file_path, 'r')
	
    values = file.read()
    file.close()
    return values

def one_star(input):
    re.purge
    result = 0
    cleaned = re.findall(r"mul\([0-9]+,[0-9]+\)",input)
    for i in range(len(cleaned)):
    # Remove mul and ()
        cleaned[i] = cleaned[i].replace("mul","")
        cleaned[i] = cleaned[i].replace("(","")
        cleaned[i] = cleaned[i].replace(")","") 
    # Split that bitch, calc that bitch
        tmp = cleaned[i].split(",")
        result = result+(int(tmp[0])*int(tmp[1]))
    return result

def two_star(input):
    re.purge
    input = re.sub(r"\n", "", input)
    dodorm = re.sub(r"don't\(\).*?do\(\)", "", input)
    return one_star(dodorm)
  

def main():
    raw = read_file()
    print("One star: ", one_star(raw))
    print("Two star: ", two_star(raw))

main()