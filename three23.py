import os
import string
import itertools
import re

def get_bounds(raw):
    bounds = []
    bounds.append(len(raw))
    bounds.append(len(list(raw[0])))
    return bounds

def get_locations(raw):
    locations = dict()
    numbers = dict()
    answer = []
    for index, data in enumerate(raw):
        # Convert string to list
        row = list(data)
        # Create row in dict with a list
        locations[index] = list()
        # Get symbols in row
        # Generate all possible symbols
        symbols = list(string.punctuation)
        # Remove .
        symbols.remove(".")

        # Loop through the row searching for symbols
        for indexc, datac in enumerate(row):
            # Compare str in list to symbols
            if datac in symbols:
                # Add location of symbol to location set
                locations[index].append(indexc)
        
        if (len(locations[index])==0):
            del locations[index]

        
        # Create list object for current row
        numbers[index] = list()
        # Get all numbers from line
        for match in re.finditer(r'\d+', data):
            tmp = []
            tmp.append(int(match.group()))
            tmp.append(match.start())
            tmp.append(match.end())
            numbers[index].append(tmp)
        # Remove list object if empty
        if (len(numbers[index])==0):
            del numbers[index]
    answer.append(locations)
    answer.append(numbers)
    return answer

def strfy(row, col):
    tmpstr = ""
    tmpstr += str(row)
    tmpstr += ":"
    tmpstr += str(col)
    return tmpstr

def get_parts(fine, bounds):
    # Split up the input data back to the two dicts
    symbols = fine[0]
    numbers = fine[1]
    answer = 0

    for index, rownum in enumerate(numbers):
        for indexr, data in enumerate(numbers[rownum]):               
            # Create direction list, 1 up, 2 down, 3 left, 4 right
            drc = []
            # Create checks with row numbers as index and colums as list
            checks = {}
            # Set start and end of number for filling the checks later
            cstart = data[1]
            cend = data[2]-1
            # Check if above is possible
            if rownum-1>=0:
                checks[rownum-1] = []
                drc.append(1)
            # Check if down is possible
            if rownum+1<bounds[0]:
                checks[rownum+1] = []
                drc.append(2)
            # Check if left is possible
            if cstart-1>=0:
                # If so also set cstart to the new vaule
                cstart -= 1
                checks[rownum] = []
                drc.append(3)
            # Check if right is possible
            if data[2]+1<bounds[1]:
                cend += 1
                checks[rownum] = []
                drc.append(4)
            # Write all checks between the cstart and the cend to rowcheck
            rowcheck = list(range(cstart,cend+1,1))
            # Up allowed: Write all values from rowcheck in checks[rownum-1]
            if 1 in drc:
                for indexrc, datarc in enumerate(rowcheck):
                    checks[rownum-1].append(datarc) 
            # Down allowed: Write all values from rowcheck checks[rownum-1]
            if 2 in drc:
                for indexrc, datarc in enumerate(rowcheck):
                    checks[rownum+1].append(datarc)
            if 3 in drc:
                checks[rownum].append(cstart)     
            if 4 in drc:
                checks[rownum].append(cend)
            # Perform all checks if hit add to the result
            for indexc, datac in enumerate(checks):
                # Check if datac (the index of checks) is in symbols dict
                if datac in symbols:
                   # Check if checkpoint is in symbols[datac]
                   for item in range(len(checks[datac])):
                       if checks[datac][item] in symbols[datac]:
                           answer += data[0]
                           break
    return answer

def get_gears(raw):
    locations = {}
    for index, data in enumerate(raw):
        # Convert string to list
        row = list(data)
        # Create row in dict with a list
        locations[index] = list()
        # Loop through the row searching for gears
        for indexc, datac in enumerate(row):
            # Compare str in list to symbols
            if datac == "*":
                # Add location of gear to location set
                locations[index].append(indexc)
        if (len(locations[index])==0):
            del locations[index]      
    return locations

def make_matrix(numbers):
    matrix = {}
    for index, data in enumerate(numbers):
        matrix[data] = {}
        for indexc, datac in enumerate(numbers[data]):
            matrix[data][datac[0]] = [*range(datac[1],datac[2])]
            # Generate all positions with the number in it
    return matrix


def get_ratio(fine, gears, bounds):
    # Get Matrix of the numbers
    matrix = make_matrix(fine[1])     
    # Loop through gear rows
    for index, data in enumerate(gears):
        # Loop through gears in row
        for indexg, datag in enumerate(gears[data]):

            # Check current row left and right of gear (if legal)
            if datag-1 in matrix[:][data]:
                print("FOUND!")
                pass
            pass

if __name__ == "__main__":
    file = os.path.dirname(os.path.realpath(__file__))
    file += "\input323s"
    with open(file) as inputfile:
        raw = [line.rstrip() for line in inputfile]      
    
    # Task 1
    bounds = get_bounds(raw)
    fine = get_locations(raw)
    print (f"Task 1", get_parts(fine, bounds))
    gears = get_gears(raw)
    print (f"Task 2:", get_ratio(fine, gears, bounds))