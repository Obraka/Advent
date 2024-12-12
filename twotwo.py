import os

def make_pretty(raw):
    pretty = []
    tmp: str
    for index, data in enumerate(raw):
        # Remove \n
        tmp = data.replace("\n", "")

        # Split row into list items
        pretty.append([int(x) for x in tmp.split(" ")])
    return pretty

def checka(values):
    invalid = 0
    asc = 0
    dsc = 0
    for index, data in enumerate(values):
        if index < len(values)-1:
            diff = abs(values[index+1] - values[index])
            # Check if diff is legal
            if not(diff > 0 and diff <= 3):
                invalid = 1
            # Check if diff is pos or neg
            if (values[index+1]-values[index])>0:
                asc += 1
            else:
                dsc += 1    
    # Check if all diffs are pos or all neg
    if asc > 0 and dsc > 0:
        invalid = 1 

    if (invalid == 0): 
        return 1

def main():
    file = os.path.dirname(os.path.realpath(__file__))
    file += "\listtwo"
    valid = 0
    with open(file) as inputfile:
        raw = inputfile.readlines()
    fine = make_pretty(raw)

    # Feed every line to the checka
    for index, data in enumerate(fine):
        if (checka(data)):
            valid += 1
    print(f"Task 1: ", valid)

    # Feed every line again, removing one item if check fails
    valid = 0
    tmpdata = []
    for index, data in enumerate(fine):
        if (checka(data)):
            valid += 1
        else:
            for i in range(len(data)):
                tmpdata = data[:]
                # Remove one object and try to feed it again
                tmpdata.pop(i)
                if (checka(tmpdata)):
                    valid += 1
                    break               
    print(f"Task 2: ", valid)    

main()