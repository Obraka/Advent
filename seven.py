import os
import copy
from itertools import permutations, product
from multiprocessing import Pool, cpu_count



def make_pretty(raw):
    result = []
    tmpresult = []
    for index, data in enumerate(raw):
        # Remove the : indicator
        tmpstr = data.replace(":", "")
        # Split it up in to one list
        tmpval = tmpstr.split(" ")
        # Make a new list [0] beeing in [0], rest as a list under it
        tmpresult.append(int(tmpval[0]))
        tmpresult.append(list(map(int, tmpval[1:])))

        result.insert(index, tmpresult.copy())
        tmpresult.clear()

    return result

def calc(data, row):
    # Set first numbers als tmpres   
    tmpres = row[1][0]
    for i in range(len(data)):
        match data[i]:
            case "*":
                tmpres *= row[1][i+1]
            case "+":
                tmpres += row[1][i+1]
            case "|":
            # Convert to list to add all digits alonge
                tmplis = list(map(int, str(row[1][i+1])))
                for i in range(len(tmplis)):
                    tmpres = (tmpres*10)+tmplis[i]
            
    return tmpres    

def checka(row):
    result = [0,0]
    
    # Task 1
    # Generate all operator variations
    oppos = list(product("+*", repeat=len(row[1])-1))
    # Check if any op possibility gives a valid result
   
    for index, data in enumerate(oppos):
        tmpres = calc(data, row)
        if tmpres == row[0]:
            result[0] += tmpres
            break
    

    # Task 2
    # Do it again, but with one more operator, but only if it didn't work before

    if (result[0] == 0):
        oppos.clear()
        # Adding | as new possibility (instead of stupid ||)
        oppos = list(product("|+*", repeat=len(row[1])-1))
        for index, data in enumerate(oppos):
            tmpres = calc(data, row)
            
            if tmpres == row[0]:
                result[1] += tmpres
                break

    return result


if __name__ == "__main__":
    tmpanswer = []
    answer = [0, 0]
    file = os.path.dirname(os.path.realpath(__file__))
    file += "\input7"

    with open(file) as inputfile:
        raw = [line.rstrip() for line in inputfile]  
    fine = make_pretty(raw)
    # Feed checka line for line
    for i in range(len(fine)):
        tmpanswer = checka(fine[i])
        answer[0] += tmpanswer[0]
        answer[1] += tmpanswer[1]

    print("Task 1: ", answer[0])
    print("Task 2: ", answer[0]+answer[1])
